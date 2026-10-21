"""HTML builders for the site: pages, deck chrome, slide components. No content lives here."""
import html
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_URL = "https://polodev.github.io/oishi"   # og:image needs an absolute URL; change if a custom domain is added
FULL_NAME = "Oishi Debnath"
BN_NAME = "ঐশী দেবনাথ"
DECK_BASE = "../../../"
DIG = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
esc = html.escape

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&family=Klee+One:wght@400;600'
         '&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">')


def bn(n):
    return str(n).translate(DIG)


def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def head_extra(base, title, description, url_path=""):
    return (f'<link rel="icon" type="image/png" href="{base}assets/img/favicon.png">'
            f'<link rel="apple-touch-icon" href="{base}assets/img/apple-touch-icon.png">'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{esc(title, quote=True)}">'
            f'<meta property="og:description" content="{esc(description, quote=True)}">'
            f'<meta property="og:image" content="{SITE_URL}/assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta name="twitter:card" content="summary_large_image">')


def avatar(base, cls="ava", small=True):
    f = "oishi-avatar-small.jpg" if small else "oishi-avatar.jpg"
    return f'<img class="{cls}" src="{base}assets/img/{f}" alt="{FULL_NAME}" width="96" height="96">'


def page(title, body, depth, theme="home", description=""):
    base = "../" * depth
    return f"""<!doctype html>
<html lang="bn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="theme-color" content="#0D9488">
{head_extra(base, title, description or "পড়াশোনার ঘর — শুধু ঐশীর জন্য, বাংলায়।")}
{FONTS}
<link rel="stylesheet" href="{base}assets/app.css">
</head>
<body class="t-{theme}">
{body}
<script src="{base}assets/app.js"></script>
</body>
</html>
"""


# ------------------------------------------------------------------ small components
def say_btn(text, lang, big=False):
    return f'<button class="say{" big" if big else ""}" data-say="{esc(text, quote=True)}" data-lang="{lang}" aria-label="শুনুন">🔊</button>'


def parse_pairs(block, parts=2):
    """'a | b | c' lines -> tuples (leading/trailing blank lines ignored)."""
    rows = []
    for line in block.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        cells = [c.strip() for c in line.split(" | ")]
        if len(cells) != parts:
            raise SystemExit(f"expected {parts} cells, got {len(cells)}: {line}")
        rows.append(tuple(cells))
    return rows


def chunks(seq, size):
    return [seq[i:i + size] for i in range(0, len(seq), size)]


def slide(inner, cls="", title=""):
    return f'<section class="slide {cls}" data-title="{esc(title, quote=True)}"><div class="inner">{inner}</div></section>'


def cover(chip, h1, lead, learn, hint=True):
    items = "".join(f"<li>{x}</li>" for x in learn)
    return slide(f'<div class="cover-top"><span class="chip">{esc(chip)}</span><span class="for-you">{avatar(DECK_BASE, "ava")} <span>{BN_NAME}-এর জন্য</span></span></div><h1>{h1}</h1><p class="lead">{lead}</p>'
                 f'<p class="five">⏱ আজকের লক্ষ্য: মাত্র ৫ মিনিট। পারলে আরও, না পারলে এটুকুই — আজকের মতো যথেষ্ট!</p><ul class="learn">{items}</ul>'
                 + ('<p class="hint">👉 ডান থেকে বামে swipe করে পরের স্লাইডে যান · উপর-নিচে স্ক্রল করে বাকিটা দেখুন</p>' if hint else ""), "cover", h1)


def quiz_slide(questions, title="কুইজ"):
    data = esc(json.dumps(questions, ensure_ascii=False), quote=True)
    return slide(f'<span class="chip">📝 {esc(title)}</span><div class="quiz" data-quiz="{data}"></div>', "", title)


def finish_slide(deck_key, heading, lead, chips, next_href=None, next_label="", back_href="../index.html", extra=""):
    nxt = f'<a class="btn" href="{next_href}">{next_label} →</a>' if next_href else ""
    chip_html = "".join(f"<span>{c}</span>" for c in chips)
    return slide(f'<div class="finish">{avatar(DECK_BASE, "ava-big", small=False)}<h2>{heading}</h2><p class="hint">শাবাশ, {BN_NAME}! 🎉</p><p class="lead">{lead}</p>'
                 f'<div class="wordlist">{chip_html}</div>{extra}'
                 f'<div class="btns">{nxt}<a class="btn ghost" href="{back_href}">সব Day</a></div></div>', "", "শেষ")


def deck_page(title, deck_key, theme, slides, back_href, crumb, home_href, has_bn=False, depth=3):
    nav = ('<div id="top"><a href="{back}">← সব Day</a><span class="crumb">{crumb}</span><a href="{home}" class="me" aria-label="হোম">{ava}</a></div><div id="bar"></div>'
           '<main id="deck">{slides}</main>'
           '<nav id="nav"><button id="prev" aria-label="আগের">‹</button><span id="count"></span><button id="next" aria-label="পরের">›</button>'
           '<button id="slow" title="ধীরে বলুন" aria-label="ধীরে">🐢</button>{bn}'
           '<button id="theme" title="Dark mode" aria-label="Theme">◐</button></nav>').format(
        back=back_href, crumb=esc(crumb), home=home_href, slides="\n".join(slides), ava=avatar('../' * depth, "ava"),
        bn=('<button id="prBtn" title="উচ্চারণ লুকান" aria-label="উচ্চারণ লুকান">🔤</button>'
            '<button id="bnBtn" title="বাংলা অর্থ লুকান" aria-label="বাংলা অর্থ লুকান">👁</button>') if has_bn else "")
    attrs = f'data-deck="{deck_key}"'
    cls = "deck" + (" has-bn" if has_bn else "")
    return f"""<!doctype html>
<html lang="bn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
{head_extra('../' * depth, title, "ঐশী দেবনাথ-এর জন্য — বাংলায়, গল্পে গল্পে ইংরেজি।")}
{FONTS}
<link rel="stylesheet" href="{'../' * depth}assets/app.css">
</head>
<body class="t-{theme} {cls}" {attrs}>
{nav}
<script src="{'../' * depth}assets/app.js"></script>
</body>
</html>
"""


# ------------------------------------------------------------------ quiz helpers
def mcq(rng, correct, pool, n=4):
    """Options list with `correct` at a random place; distractors drawn from pool (unique, != correct)."""
    others = [p for p in dict.fromkeys(pool) if p != correct]
    rng.shuffle(others)
    opts = others[:n - 1] + [correct]
    rng.shuffle(opts)
    return opts, opts.index(correct)


def seeded(*parts):
    return random.Random("|".join(map(str, parts)))
