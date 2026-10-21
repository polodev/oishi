"""Turns physics101.CHAPTERS into deck pages."""
from engine import (DECK_BASE, BN_NAME, avatar, bn, cover, deck_page, esc, finish_slide, quiz_slide, seeded, slide, write)
from site_english import word_card
import physics101 as P


def story_slides(c):
    out = []
    for part, lo in enumerate((0, 4), 1):
        lines = "".join(f'<p class="pline">{esc(t)}</p>' for t in c["story"][lo:lo + 4])
        hero = (f'<div class="story-hero">{avatar(DECK_BASE, "ava")}<div><b>এই গল্পের নায়িকা: ঐশী — মানে তুমি!</b><span>{esc(c["en"])}</span></div></div>' if part == 1 else "")
        out.append(slide(f'<span class="chip">📖 গল্প {bn(part)}/২</span><h2>{esc(c["title"])}</h2>{hero}{lines}', "", "গল্প"))
    return out


def term_slides(c):
    out = []
    for part, lo in enumerate((0, 3), 1):
        cards = "".join(word_card(en, pr, bn_) for bn_, en, pr in c["terms"][lo:lo + 3])
        out.append(slide(f'<span class="chip">🔤 নতুন শব্দ {bn(part)}/২</span><h2>ইংরেজি নামও শিখে নাও</h2>{cards}', "", "শব্দ"))
    return out


def concept_slide(c):
    title, points = c["concept"]
    pts = "".join(f"<li>{p}</li>" for p in points)
    return slide(f'<span class="chip">💡 মূল কথা</span><h2>{esc(title)}</h2><ul class="pts">{pts}</ul>', "", "মূল কথা")


def activity_slide(c):
    title, steps = c["activity"]
    items = "".join(f"<li>{esc(s)}</li>" for s in steps)
    return slide(f'<span class="chip">🏠 নিজে করে দেখো</span><h2>{esc(title)}</h2><ol class="steps">{items}</ol>'
                 '<div class="callout">⚠️ আগুন, গরম পানি বা বিদ্যুৎ লাগলে বড়দের সাথে করবে।</div>', "", "পরীক্ষা")


def medical_slide(c):
    lines = "".join(f'<div class="med">{esc(t)}</div>' for t in c["medical"])
    return slide(f'<span class="chip">🩺 চিকিৎসার জগতে</span><h2>বিজ্ঞান কোথায় কাজে লাগে</h2>{lines}', "", "চিকিৎসা")


def quiz_for(c):
    rng = seeded("phy", c["n"])
    qs = []
    for q, opts, ans, why in c["quiz"]:
        o = list(opts)
        correct = o[ans]
        rng.shuffle(o)
        qs.append(dict(q=q, o=o, a=o.index(correct), why=why))
    return qs


def build_chapter(c):
    n = c["n"]
    key = f"physics/101/ch-{n:02d}"
    S = [cover(f"অধ্যায় {bn(n)}", esc(c["title"]), esc(c["intro"]),
               ["📖 ছোট্ট একটা গল্প", "🔤 ৬টি নতুন শব্দ (ইংরেজি নামসহ)", "💡 মূল কথা — সহজ ভাষায়", "🏠 ঘরে করার একটা পরীক্ষা", "🩺 চিকিৎসার জগতে যোগ", "📝 ৬টি প্রশ্নের কুইজ"])]
    S += story_slides(c) + term_slides(c)
    S += [concept_slide(c), activity_slide(c), medical_slide(c), quiz_slide(quiz_for(c))]
    chips = [esc(t[0]) for t in c["terms"]]
    if n == len(P.CHAPTERS):
        S.append(finish_slide(key, "Physics 101 সম্পূর্ণ! 🏆", f"২০টি অধ্যায়, শত শত ছোট ধারণা — {BN_NAME}, তুমি এখন বলতে পারো পদার্থবিজ্ঞান আসলে কী আর কোথায় কাজে লাগে।",
                              chips, None, back_href="../index.html", back_label="সব অধ্যায়",
                              extra='<div class="callout"><b>এরপর কী?</b><br>Physics 102 শীঘ্রই আসছে — আরও গভীরে, একই মজায়।</div>'))
    else:
        nxt = P.CHAPTERS[n]
        S.append(finish_slide(key, f"অধ্যায় {bn(n)} শেষ!", "আজ যা শিখলে, রাতে ঘুমানোর আগে একবার মনে করে দেখো।", chips,
                              f"../ch-{n + 1:02d}/index.html", f"অধ্যায় {bn(n + 1)}: {esc(nxt['title'])}", back_href="../index.html", back_label="সব অধ্যায়"))
    write(f"physics/101/ch-{n:02d}/index.html", deck_page(f"অধ্যায় {n} · {c['title']} — Physics 101", key, "sub", S, back_href="../index.html",
                                                     crumb=f"অধ্যায় {bn(n)} · {c['title']}", home_href="../../../index.html", has_bn=False, back_label="সব অধ্যায়"))
