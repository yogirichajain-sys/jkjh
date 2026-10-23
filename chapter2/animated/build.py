"""Render all scenes, join them, add subtitles.

    /opt/mvenv/bin/python build.py        # full HD (1920x1080, 30 fps)
    /opt/mvenv/bin/python build.py l      # quick low-quality check
    /opt/mvenv/bin/python build.py h S02Basics S07Trends   # only some scenes, then re-join

Voice: ElevenLabs if ELEVENLABS_API_KEY is set, else the Piper stand-in.
"""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from voice import engine  # noqa: E402

SCENES = ["S01Hook", "S02Basics", "S03Triads", "S04Mendeleev", "S05Moseley", "S06Modern", "S07Trends", "S08Quiz"]
QUALITY = {"l": (["-ql"], "480p15"), "m": (["-qm"], "720p30"), "h": (["-r", "1920,1080", "--fps", "30"], "1080p30")}
MANIM = os.environ.get("MANIM_BIN", "/opt/mvenv/bin/manim")
STUDENT_COLOUR = "#c084fc"


def render(scene, flags):
    log = os.path.join(HERE, "build", "logs", f"{scene}.log")
    os.makedirs(os.path.dirname(log), exist_ok=True)
    with open(log, "w") as f:
        r = subprocess.run([MANIM, *flags, "--disable_caching", "lesson.py", scene], cwd=HERE, stdout=f, stderr=subprocess.STDOUT)
    print(f"{scene}: {'ok' if r.returncode == 0 else 'FAILED, see ' + log}", flush=True)
    return r.returncode == 0


def duration(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", path]))


def chunks(text, limit=84):
    out = []
    for sent in re.split(r"(?<=[.!?])\s+", text.strip()):
        words, cur = sent.split(), ""
        for w in words:
            if len(cur) + len(w) + 1 > limit and cur:
                out.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            out.append(cur)
    return out


def ts(t):
    h, m = int(t // 3600), int(t % 3600 // 60)
    return f"{h:02d}:{m:02d}:{t % 60:06.3f}".replace(".", ",")


def write_srt(files, path):
    offset, n, lines = 0.0, 1, []
    for scene, f in files:
        with open(os.path.join(HERE, "build", "cues", f"{scene}.json")) as fh:
            cues = json.load(fh)
        for c in cues:
            parts = chunks(c["text"])
            total = sum(len(p) for p in parts)
            t = offset + c["start"]
            for p in parts:
                d = c["dur"] * len(p) / total
                txt = f'<font color="{STUDENT_COLOUR}">{p}</font>' if c.get("who") == "student" else p
                lines += [str(n), f"{ts(t)} --> {ts(t + d)}", txt, ""]
                n += 1
                t += d
        offset += duration(f)
    with open(path, "w") as fh:
        fh.write("\n".join(lines))


def main():
    args = sys.argv[1:]
    q = args[0] if args and args[0] in QUALITY else "h"
    only = [a for a in args if a in SCENES] or SCENES
    flags, folder = QUALITY[q]
    print(f"Voice: {engine()} · quality: {folder} · scenes: {len(only)}")
    with ThreadPoolExecutor(max_workers=int(os.environ.get("JOBS", "4"))) as ex:
        ok = list(ex.map(lambda s: render(s, flags), only))
    if not all(ok):
        sys.exit(1)

    files = [(s, os.path.join(HERE, "media", "videos", "lesson", folder, f"{s}.mp4")) for s in SCENES]
    missing = [f for _, f in files if not os.path.exists(f)]
    if missing:
        sys.exit(f"missing scene videos: {missing}")
    out_dir = os.path.join(HERE, "out")
    os.makedirs(out_dir, exist_ok=True)
    tag = "" if engine() == "elevenlabs" else "_preview"
    name = f"chapter2_periodic_classification_animated{tag}" + ("" if q == "h" else f"_{folder}")
    lst = os.path.join(HERE, "build", "concat.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{f}'\n" for _, f in files)
    joined = os.path.join(HERE, "build", "joined.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", joined], check=True)
    srt = os.path.join(out_dir, name + ".srt")
    write_srt(files, srt)
    style = ("FontName=Inter,FontSize=17,PrimaryColour=&H00FFFFFF,BackColour=&H99000000,"
             "BorderStyle=4,Outline=0,Shadow=0,MarginV=18,Bold=0")
    final = os.path.join(out_dir, name + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", joined, "-vf", f"subtitles={srt}:force_style='{style}'",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "copy", "-movflags", "+faststart", final], check=True)
    print(f"Done: {final} ({duration(final) / 60:.1f} min)")


if __name__ == "__main__":
    main()
