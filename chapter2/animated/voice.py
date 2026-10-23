"""Narration audio: ElevenLabs when ELEVENLABS_API_KEY is set, otherwise a local
Piper voice as a stand-in. Audio is cached, so re-renders are fast."""
import hashlib
import json
import os
import subprocess
import urllib.request
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "build", "voice")
PIPER_BIN = os.environ.get("PIPER_BIN", "/opt/mvenv/bin/piper")
PIPER_MODEL = os.environ.get("PIPER_MODEL", "/opt/piper/en_US-lessac-medium.onnx")
EL_VOICE = os.environ.get("ELEVENLABS_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")
EL_MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")


def engine():
    return "elevenlabs" if os.environ.get("ELEVENLABS_API_KEY", "").strip() else "piper"


def _eleven(text, out_wav):
    key = os.environ["ELEVENLABS_API_KEY"].strip()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{EL_VOICE}?output_format=mp3_44100_128",
        data=json.dumps({"text": text, "model_id": EL_MODEL,
                         "voice_settings": {"stability": 0.45, "similarity_boost": 0.75,
                                            "style": 0.3}}).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    mp3 = out_wav[:-4] + ".mp3"
    with urllib.request.urlopen(req, timeout=180) as r, open(mp3, "wb") as f:
        f.write(r.read())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-ar", "44100", "-ac", "1", out_wav],
                   check=True)


def _piper(text, out_wav):
    subprocess.run([PIPER_BIN, "-m", PIPER_MODEL, "-f", out_wav, "--length-scale", "0.95",
                    "--sentence-silence", "0.25"],
                   input=text.encode(), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def speak(text):
    """Return (wav_path, seconds) for this narration line."""
    eng = engine()
    tag = f"{eng}|{EL_VOICE}|{EL_MODEL}|{text}" if eng == "elevenlabs" else f"{eng}|{PIPER_MODEL}|{text}"
    h = hashlib.sha1(tag.encode()).hexdigest()[:16]
    os.makedirs(CACHE, exist_ok=True)
    wav = os.path.join(CACHE, f"{eng}_{h}.wav")
    if not os.path.exists(wav):
        tmp = wav + ".tmp.wav"
        (_eleven if eng == "elevenlabs" else _piper)(text, tmp)
        os.replace(tmp, wav)
    with wave.open(wav) as w:
        return wav, w.getnframes() / w.getframerate()
