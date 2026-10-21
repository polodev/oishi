# Oishi — agent guide

Personal learning site for **Oishi Debnath** (HSC student, loves biology), taught in **Bangla**, mobile first.
Repo `polodev/oishi` → GitHub Pages `https://polodev.github.io/oishi/`.

Before writing any lesson read **SUBJECT_GUIDE.md** (audience, hidden motivational goal, wording rule "homeopathic doctor", course format, roadmap).

## Structure
Home → subject (English, Physics, Chemistry, Biology, Math, Bangla, ICT) → course (101 live for English, Physics, Chemistry, Biology, Math, Bangla and ICT; 102/103 and every other subject course show 🔒 coming soon) → Day 1…20 (swipeable slide deck).

## Files
- `english101.py` — data (`day(n, en, bn, intro, story, words, sentences, grammar)`); asserts 8/10/20 lines, no repeated word, no bare "doctor".
- `physics101.py`, `chemistry101.py`, `biology101.py`, `math101.py`, `bangla101.py`, `ict101.py` — chapter-course data (all share `coursekit.py` safety nets; physics predates it and keeps its own asserts). Shape: 20 chapters (story 8 lines, 6 terms, concept, home activity, 2 positive medical lines, 6-question quiz); asserts counts and bans bare "ডাক্তার". `site_subject.py` builds the decks (`<subject>/101/ch-NN/`). To add a subject module: write `<subject>101.py` with `COURSE, CHAPTERS`, then add it to `MODULES` in `build.py`.
- `pron_en.py` — Bangla pronunciation for every English word used in story/sentences; `build_line()`; the build fails on a missing word. Add new words to `_RAW`.
- `site_english.py`, `engine.py`, `build.py`, `assets/app.css`, `assets/app.js` (no frameworks). Photos in `assets/img/` (EXIF stripped).

## Build and verify
`python3 build.py` then check on an emulated phone (390×844, `isMobile`, `hasTouch`): no overflow, swipe, quiz, no console errors.

## Rules
Bangla prose; relative links; no AI attribution in commits; never commit secrets. Do not add personal details that the owner has not given.
