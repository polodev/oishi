"""Turns english101.DAYS into deck pages."""
from engine import (DECK_BASE, BN_NAME, FULL_NAME, avatar, bn, chunks, cover, deck_page, esc, finish_slide, mcq, quiz_slide, say_btn, seeded, slide, write)
import english101 as E
from pron_en import build_line

LANG = "en-US"


def line(en, bn_text):
    return (f'<div class="line">{say_btn(en, LANG)}<div><p class="en">{esc(en)}</p><p class="pr">{esc(build_line(en))}</p><p class="bn">{esc(bn_text)}</p></div></div>')


def word_card(en, pr, meaning):
    return (f'<div class="wcard">{say_btn(en, LANG, big=True)}<div class="w-en">{esc(en)}</div>'
            f'<div class="w-pr pr">উচ্চারণ: {esc(pr)}</div><div class="bn w-bn">{esc(meaning)}</div></div>')


def grammar_slide(d):
    g = d["grammar"]
    pts = "".join(f"<li>{p}</li>" for p in g["points"])
    rows = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in g["table"])
    q, opts, ans, why = g["quiz"]
    opt_txt = " / ".join(f"<b>{esc(o)}</b>" for o in opts)
    return slide(f'<span class="chip">✏️ ব্যাকরণ টিপ</span><h2>{g["title"]}</h2><ul class="pts">{pts}</ul>'
                 f'<table class="tbl"><tr><th>শুরু</th><th>বসবে</th><th>উদাহরণ</th></tr>{rows}</table>'
                 f'<details class="q"><summary>🧠 নিজে চেষ্টা করুন: {esc(q)}</summary><div>{opt_txt}</div>'
                 f'<p>উত্তর: {esc(opts[ans])} — {esc(why)}</p></details>', "", "ব্যাকরণ")


def quiz_for(d):
    rng = seeded("en", d["n"])
    words, sents = d["words"], d["sentences"]
    qs = []
    for en, pr, meaning in rng.sample(words, 5):
        opts, a = mcq(rng, meaning, [w[2] for w in words])
        qs.append(dict(q=f"‘{en}’ মানে কী?", say=en, lang=LANG, o=opts, a=a, why=f"{en} = {meaning} (উচ্চারণ: {pr})"))
    for en, bn_text in rng.sample(sents, 3):
        opts, a = mcq(rng, bn_text, [s[1] for s in sents])
        qs.append(dict(q=f"“{en}” — এর বাংলা কোনটা?", say=en, lang=LANG, o=opts, a=a, why=f"{en} = {bn_text}"))
    g = d["grammar"]["quiz"]
    qs.append(dict(q=g[0], o=g[1], a=g[2], why=g[3]))
    return qs


def build_day(d):
    n = d["n"]
    key = f"english/101/day-{n:02d}"
    is_last = n == len(E.DAYS)
    S = [cover(f"অধ্যায় {bn(n)}", esc(d["en"]), f"<b>{esc(d['bn'])}</b> — {esc(d['intro'])}",
               ["📖 একটি ছোট গল্প (৮ লাইন)", "🔤 ১০টি নতুন শব্দ, বাংলা উচ্চারণসহ", "💬 ২০টি দরকারি বাক্য", "✏️ একটি ব্যাকরণ টিপ", "📝 ৯টি প্রশ্নের কুইজ"])]

    for part, grp in enumerate(chunks(d["story"], 4), 1):
        S.append(slide(f'<span class="chip">📖 গল্প {bn(part)}/২</span><h2>{esc(d["en"])}</h2>'
                       + (f'<div class="story-hero">{avatar(DECK_BASE, "ava")}<div><b>গল্পের নায়ক: Oishi — মানে তুমি!</b><span>{BN_NAME}-এর জীবনের গল্পেই ইংরেজি শিখছ।</span></div></div>'
                          '<p class="hint">🔊 চাপলে শুনতে পাবেন। 🔤 বাটনে উচ্চারণ আর 👁 বাটনে বাংলা অর্থ লুকিয়ে নিজেকে পরীক্ষা করুন।</p>' if part == 1 else "")
                       + '<div class="row-actions"><button class="btn" data-play>▶ পুরো অংশ শুনুন</button></div>'
                       + "".join(line(*x) for x in grp), "", "গল্প"))

    for part, grp in enumerate(chunks(d["words"], 5), 1):
        S.append(slide(f'<span class="chip">🔤 শব্দ {bn(part)}/২</span><h2>আজকের নতুন শব্দ</h2>'
                       + "".join(word_card(*w) for w in grp), "", "শব্দ"))

    parts = chunks(d["sentences"], 5)
    for part, grp in enumerate(parts, 1):
        S.append(slide(f'<span class="chip">💬 বাক্য {bn(part)}/{bn(len(parts))}</span><h2>বাক্য {bn((part - 1) * 5 + 1)}–{bn(part * 5)}</h2>'
                       + '<p class="hint">জোরে বলুন, তারপর শুনুন, তারপর আবার বলুন।</p>' + "".join(line(*x) for x in grp), "", "বাক্য"))

    S.append(grammar_slide(d))
    S.append(quiz_slide(quiz_for(d)))

    chips = [esc(w[0]) for w in d["words"]]
    if is_last:
        S.append(finish_slide(key, "English 101 সম্পূর্ণ! 🏆", "২০ দিনে ২০০টি শব্দ আর ৪০০টি বাক্য — তুমি এখন নিজের পরিচয়, পরিবার, পড়াশোনা, শরীর, জীববিজ্ঞান, হোমিওপ্যাথিক চিকিৎসা আর স্বপ্নের কথা ইংরেজিতে বলতে পারো।",
                              chips, None, back_href="../index.html", back_label="সব অধ্যায়",
                              extra='<div class="callout"><b>এখন কী করবেন?</b><br>প্রতিদিন ৫ মিনিট পুরনো অধ্যায়ের বাক্যগুলো জোরে বলো। English 102 শীঘ্রই আসছে।</div>'))
    else:
        S.append(finish_slide(key, f"অধ্যায় {bn(n)} শেষ!", "আজকের শব্দগুলো মনে রাখতে সারাদিন কয়েকবার বলুন।", chips,
                              f"../day-{n + 1:02d}/index.html", f"অধ্যায় {bn(n + 1)}: {esc(E.DAYS[n]['bn'])}", back_label="সব অধ্যায়"))

    html = deck_page(f"অধ্যায় {n} · {d['en']} — English 101", key, "en", S, back_href="../index.html",
                     crumb=f"অধ্যায় {bn(n)} · {d['bn']}", home_href="../../../index.html", has_bn=True, back_label="সব অধ্যায়")
    write(f"english/101/day-{n:02d}/index.html", html)
