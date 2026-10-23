# SSC Science basics — lesson videos

Lessons for Maharashtra SSC Class 10 Science, built "basics first": refresh what you learned in earlier classes, then the chapter's facts and rules, then the understanding behind them.

## Chapter 2 (Part 1): Periodic Classification of Elements
- `chapter2/chapter2_periodic_classification_preview.mp4` — the full lesson (about 15 min) with subtitles and no voice yet.
- `chapter2/script.md` — the narration script.
- `chapter2/notes.md` — one-page revision notes.
- `chapter2/scenes.py` — slides and narration (edit here); `chapter2/make_video.py` builds the video.

### Adding the ElevenLabs voice
1. Save your API key as the environment variable `ELEVENLABS_API_KEY` in the cloud environment settings (never paste it in chat). Optionally set `ELEVENLABS_VOICE_ID`.
2. Run `python3 chapter2/make_video.py`. It creates `chapter2/chapter2_periodic_classification.mp4` with the voice, and timing follows the speech.

Needs Python 3 with Pillow, ffmpeg, and the Inter font.
