"""Build the Chapter 2 lesson video.

    python3 make_video.py            # voice from ElevenLabs if ELEVENLABS_API_KEY is set,
                                     # otherwise a silent preview with subtitles
    python3 make_video.py --frames   # only render slide images (quick check)
    python3 make_video.py --script   # only write script.md

Env vars: ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID (optional), ELEVENLABS_MODEL (optional)
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.request

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw import BG, MUTED, TEXT, ACCENT, W, H, text, wrap, font  # noqa: E402
from scenes import SCENES  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
SUB_SIZE = 38
SUB_MAXW = 1720
CHARS_PER_SEC = 14.0  # reading speed for the silent preview
PAUSE = 0.4           # gap after each step, seconds


# ------------------------------------------------------------ subtitles
def chunks(narration):
    """Split narration into subtitle pieces of at most 2 lines."""
    sentences = re.split(r"(?<=[.!?])\s+", narration.strip())
    pieces = []
    for s in sentences:
        if len(wrap(s, SUB_SIZE, SUB_MAXW)) <= 2:
            pieces.append(s)
            continue
        cur = ""
        for w in s.split():
            t = (cur + " " + w).strip()
            if len(wrap(t, SUB_SIZE, SUB_MAXW)) > 2:
                pieces.append(cur)
                cur = w
            else:
                cur = t
        if cur:
            pieces.append(cur)
    out = []
    for p in pieces:  # merge short pieces
        if out and len(wrap(out[-1] + " " + p, SUB_SIZE, SUB_MAXW)) <= 2 and len(out[-1]) < 60:
            out[-1] += " " + p
        else:
            out.append(p)
    return out


def render(scene_i, step, sub=None, subtitles=True):
    sc = SCENES[scene_i]
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    if sc["title"]:
        text(d, (110, 60), sc["title"], 56, "Bold", TEXT)
        d.line((110, 140, 1810, 140), fill=ACCENT, width=4)
    sc["draw"](d, step)
    text(d, (1810, 60), "Ch 2 · Periodic Classification", 26, "Medium", MUTED, "ra")
    if subtitles and sub:
        lines = wrap(sub, SUB_SIZE, SUB_MAXW)
        top = 1060 - len(lines) * 50 - 20
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(overlay).rectangle((0, top, W, H), fill=(0, 0, 0, 200))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        d = ImageDraw.Draw(img)
        for i, line in enumerate(lines):
            text(d, (W / 2, top + 20 + i * 50), line, SUB_SIZE, "Medium", TEXT, "ma")
    return img


# ------------------------------------------------------------ audio
def tts(narration, key):
    voice = os.environ.get("ELEVENLABS_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")
    model = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")
    h = hashlib.sha1(f"{voice}|{model}|{narration}".encode()).hexdigest()[:16]
    path = os.path.join(BUILD, "audio", f"{h}.mp3")
    if os.path.exists(path):
        return path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
        data=json.dumps({"text": narration, "model_id": model,
                         "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    with urllib.request.urlopen(req, timeout=120) as r, open(path, "wb") as f:
        f.write(r.read())
    return path


def duration(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", path])
    return float(out)


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# ------------------------------------------------------------ script
def write_script():
    lines = ["# Chapter 2: Periodic Classification of Elements - video script", "",
             "Maharashtra SSC Class 10, Science & Technology Part 1. "
             "Generated from `scenes.py`; edit the narration there.", ""]
    for i, sc in enumerate(SCENES):
        lines.append(f"## Scene {i + 1}: {sc['title'] or ('Intro' if i == 0 else 'Outro')}")
        lines.append("")
        for j, s in enumerate(sc["steps"]):
            lines.append(f"{j + 1}. {s}")
        lines.append("")
    words = sum(len(s.split()) for sc in SCENES for s in sc["steps"])
    lines.append(f"_Total: {words} words, about {words / 150:.0f} minutes of narration._")
    with open(os.path.join(HERE, "script.md"), "w") as f:
        f.write("\n".join(lines) + "\n")


# ------------------------------------------------------------ main
def main():
    args = sys.argv[1:]
    write_script()
    if "--script" in args:
        return
    frames_dir = os.path.join(BUILD, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    if "--frames" in args:
        for i, sc in enumerate(SCENES):
            for k in range(len(sc["steps"])):
                render(i, k, chunks(sc["steps"][k])[0]).save(
                    os.path.join(frames_dir, f"s{i:02d}_{k}.png"))
        print("frames in", frames_dir)
        return

    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    voiced = bool(key)
    print("Voice:", "ElevenLabs" if voiced else "none (silent preview)")
    concat, audio_parts, n = [], [], 0
    for i, sc in enumerate(SCENES):
        for k, narration in enumerate(sc["steps"]):
            parts = chunks(narration)
            if voiced:
                mp3 = tts(narration, key)
                wav = os.path.join(BUILD, "audio", f"step_{n:03d}.wav")
                run(["ffmpeg", "-y", "-i", mp3, "-af", f"apad=pad_dur={PAUSE}",
                     "-ar", "44100", "-ac", "1", wav])
                total = duration(wav)
                audio_parts.append(wav)
            else:
                total = len(narration) / CHARS_PER_SEC + PAUSE
            weights = [len(p) for p in parts]
            for j, p in enumerate(parts):
                png = os.path.join(frames_dir, f"f{n:03d}_{j}.png")
                render(i, k, p, "--no-subtitles" not in args).save(png)
                concat.append((png, total * weights[j] / sum(weights)))
            n += 1
            print(f"  scene {i + 1}/{len(SCENES)} step {k + 1}")

    lst = os.path.join(BUILD, "frames.txt")
    with open(lst, "w") as f:
        for png, dur in concat:
            f.write(f"file '{png}'\nduration {dur:.3f}\n")
        f.write(f"file '{concat[-1][0]}'\n")
    total = sum(dur for _, dur in concat)

    audio = os.path.join(BUILD, "narration.wav")
    if voiced:
        alst = os.path.join(BUILD, "audio.txt")
        with open(alst, "w") as f:
            f.writelines(f"file '{a}'\n" for a in audio_parts)
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", alst, audio])
    else:
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
             "-t", f"{total:.2f}", audio])

    out = os.path.join(HERE, "chapter2_periodic_classification" + ("" if voiced else "_preview") + ".mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", audio,
         "-vf", "fps=24,format=yuv420p", "-c:v", "libx264", "-preset", "medium",
         "-tune", "stillimage", "-crf", "23", "-c:a", "aac", "-b:a", "128k",
         "-shortest", "-movflags", "+faststart", out])
    print(f"Done: {out}  ({total / 60:.1f} min)")


if __name__ == "__main__":
    main()
