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

## Chapter 2 — animated version (recommended)
`chapter2/animated/` is a fully animated lesson (Manim): atoms fill their shells, the periodic table builds itself, and a student asks "Doubt!" questions that get answered (why mass and not atomic number, why 2,8,8,1 and not 2,8,9, why atoms shrink across a period, and more).

- `chapter2/animated/out/chapter2_periodic_classification_animated_preview.mp4` — full HD, about 16.5 min, stand-in voice.
- `lesson.py` — scenes and narration; `build.py` renders, joins and adds subtitles.
- With `ELEVENLABS_API_KEY` set (optionally `ELEVENLABS_VOICE_ID` for the teacher and `ELEVENLABS_STUDENT_VOICE_ID` for the student), run `/opt/mvenv/bin/python chapter2/animated/build.py` to make the final voiced video. Animation timing follows the voice automatically.
