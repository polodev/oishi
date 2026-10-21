# Subject guide — how to build the next courses for Oishi

Read this before writing physics, chemistry, biology, math, bangla or ICT. English 101 and Physics 101 are the reference implementations
(`english101.py` → `site_english.py`, `physics101.py` → `site_physics.py`, both wired in `build.py`). Physics 101 is the template for non-language subjects (story → terms → concept → home activity → medical link → quiz, no formula before chapter 7, class-five language).

## Who she is (facts only; all given by the owner)
- Oishi Debnath, finished SSC, now studying HSC (intermediate), admitted to a homeopathic medical course.
- Father Bimol Debnath and mother Zumur Rani Debnath are both **homeopathic doctors** (real doctors in Bangladesh). Younger brother: Raj Debnath.
- Cousin: Sanjoy Dev Shuvo (her mother's elder sister's son). She loves **biology**. She wears glasses. She passively wants to be a doctor.
- Do not invent other personal details (age, address, town, friends' names). Ask the owner.

## The hidden goal (never say it out loud)
The owner wants her passive "maybe a doctor" feeling to become an active dream — **without ever telling her to become a doctor**.
So every course quietly makes the medical life look attractive:
1. **Only positive** things about doctors: respected, trusted, thanked by patients, help families, good income, comfortable life, proud family, always learning. Never mention malpractice, stress, long hours, exam failure, or anything discouraging.
2. Show it through **examples and stories**, not advice. A line like "Patients thank the homeopathic doctor with a smile" works; "You should become a doctor" never appears.
3. Roughly **1–2 such lines per lesson**, spread naturally. Don't repeat the same line; vary the angle (respect, helping, income, science excitement, family pride, travel/conferences, own chamber).
4. Wording rule (from the owner): when a doctor is mentioned, **always say "homeopathic doctor"** (English) / **হোমিওপ্যাথিক ডাক্তার** (Bangla). The build already fails if bare "doctor" appears in English 101 story/sentences.
5. The finale of each course (chapter-20 style) can imagine her future chamber, respect and happy life — as imagination ("Imagine a morning ten years from now"), never as an instruction.

## Teaching style
- **Out of the box, not the textbook.** Teach the core concept through a surprising real-life example, a mini story or a "why does this happen?" question, then connect it to the textbook chapter name so she can find it in her book. She is an intermediate student: she needs concepts that stick, not page summaries.
- **Medical lens wherever it fits:** physics → heartbeat/ECG, X-ray, ultrasound, lenses and her own glasses, thermometer; chemistry → acids and stomach pH, antiseptics, vitamin C, why medicines have doses; biology → cells, immunity, DNA, the heart, digestion; math → dosage, BMI, percentages in medicine, statistics of patients; bangla → essays, stories and letters that carry the same positive themes; ICT → hospital software, telemedicine, health apps, patient records in spreadsheets.
- Fun facts must be **true and checkable** (heart ≈ 100,000 beats/day, adult skeleton = 206 bones, skin is the largest organ, light is faster than sound). If unsure, leave it out.
- No medical advice that could be harmful; no efficacy claims about homeopathy ("works", "cures"). Say what the professionals *do* (listen, ask symptoms, choose medicine, advise) — not what medicine guarantees.
- Everything in **Bangla** (English/science terms in English with Bangla pronunciation and meaning). Short slides, big text, one idea each. Cultural care: no alcohol/pork examples.
- Light motivation, not pressure: 5-minute goal on each cover, streak on the course page. She may be as lazy as any teenager; make the first slide of every Day fun.

## Course format (match English 101)
- `Chapter (অধ্যায়) 1 … N` per course; each chapter = one swipeable deck. Suggested: **20 chapters per course**. Never call them "days" in the UI.
- Per chapter (adapt the box per subject): hook story/question (8 slides-worth of lines) → 10 key terms (English term, Bangla pronunciation, Bangla meaning) → 20 practice items → 1 "concept tip" slide → quiz (5 term + 3 item + 1 concept) → finish slide.
- Build-time safety nets (add the same style of asserts): fixed counts per chapter, no term repeated across a course, no bare "doctor", no missing pronunciation.
- Quizzes are generated at build time with a seeded RNG (`engine.seeded`) so diffs stay stable.

## Adding a course (steps)
1. Create `<subject>101.py` with `COURSE` and `DAYS` like `english101.py`.
2. Create `site_<subject>.py` with `build_day(day)` using helpers from `engine.py` (`slide`, `cover`, `quiz_slide`, `finish_slide`, `deck_page`, …).
3. In `build.py`: add `("<subject>", "101")` to `OPEN`, add a `course_page_<subject>()` (copy `course_page_english`), call the builder in the `__main__` loop. Locked slots `102`, `103` are already shown automatically.
4. `python3 build.py`, then check on a phone-sized screen (Playwright 390×844, `isMobile`, `hasTouch`): no horizontal overflow, swipe, quiz, no console errors.

## Suggested roadmap (edit freely; confirm HSC book chapters with the owner)
| Subject | 101 | 102 | 103 |
|---|---|---|---|
| English | Stories about her life (**live**) | Reading medical/science passages, writing short paragraphs | Speaking & listening, interviews, formal letters, medical admission English |
| Biology | Cell, tissue, human body systems told as stories | Genetics & DNA, immunity, plant biology | Microbes, evolution, ecology — with clinic scenes |
| Physics | **Live (20 chapters):** matter, motion, speed, force, friction, gravity, pressure, energy, heat, sound, light, lenses, electricity, magnets, physics in medicine | Light & optics (glasses), waves, sound (ultrasound) | Electricity, magnetism, modern physics (X-ray) |
| Chemistry | Atoms, acids/bases, pH of the stomach | Reactions, solutions, organic basics | Biochemistry: vitamins, proteins, medicines |
| Math | Numbers, algebra via dosage and BMI | Functions, trigonometry, geometry | Statistics, probability, calculus basics |
| Bangla | Reading and writing short essays with warm themes | Grammar, composition, letters | Literature appreciation |
| ICT | Computers, internet, safety | Spreadsheets for patient records, databases | Programming basics, telemedicine, health apps |

## Privacy
The repo and GitHub Pages site are public. They contain a minor's photo and full name and her family's names. Keep surnames of other relatives, addresses, phone numbers and school names out of the content. See README "Privacy".
