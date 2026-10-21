"""Builds the whole site (static HTML).   python3 build.py

Content lives in english101.py; engine.py has the HTML pieces; assets/ holds CSS and JS.
Relative links everywhere, so it works at https://<user>.github.io/oishi/ and at a domain root.
Subjects: English (101 open, 102/103 locked) and Physics, Chemistry, Biology, Math, Bangla, ICT (all courses locked for now)."""
import shutil

from engine import BN_NAME, FULL_NAME, ROOT, avatar, bn, esc, page, write
import english101 as E
import site_english

# slug -> subject. `open` = courses that exist (slug of course -> module); every other course shows as locked.
SUBJECTS = {
    "english": dict(name="English", bn_name="ইংরেজি", badge="A", intro="গল্পে গল্পে ইংরেজি — তোমার নিজের জীবনের গল্প, বাংলা অর্থ ও উচ্চারণসহ।",
                    courses={"101": ("English 101", "গল্পে গল্পে ইংরেজি"), "102": ("English 102", "পরের ধাপ"), "103": ("English 103", "আরও এগিয়ে")}),
    "physics": dict(name="Physics", bn_name="পদার্থবিজ্ঞান", badge="⚛", intro="HSC পদার্থবিজ্ঞান — বাংলায়, ধাপে ধাপে।",
                    courses={"101": ("Physics 101", "শুরুর ধারণা"), "102": ("Physics 102", "পরের ধাপ"), "103": ("Physics 103", "আরও এগিয়ে")}),
    "chemistry": dict(name="Chemistry", bn_name="রসায়ন", badge="⚗", intro="HSC রসায়ন — বাংলায়, ধাপে ধাপে।",
                      courses={"101": ("Chemistry 101", "শুরুর ধারণা"), "102": ("Chemistry 102", "পরের ধাপ"), "103": ("Chemistry 103", "আরও এগিয়ে")}),
    "biology": dict(name="Biology", bn_name="জীববিজ্ঞান", badge="🧬", intro="তোমার প্রিয় বিষয়! কোষ থেকে মানবদেহ — বাংলায়, ধাপে ধাপে।",
                    courses={"101": ("Biology 101", "শুরুর ধারণা"), "102": ("Biology 102", "পরের ধাপ"), "103": ("Biology 103", "আরও এগিয়ে")}),
    "math": dict(name="Math", bn_name="গণিত", badge="∑", intro="HSC গণিত — বাংলায়, ধাপে ধাপে।",
                 courses={"101": ("Math 101", "শুরুর ধারণা"), "102": ("Math 102", "পরের ধাপ"), "103": ("Math 103", "আরও এগিয়ে")}),
    "bangla": dict(name="Bangla", bn_name="বাংলা", badge="অ", intro="বাংলা সাহিত্য ও ব্যাকরণ — ধাপে ধাপে।",
                   courses={"101": ("Bangla 101", "শুরুর ধারণা"), "102": ("Bangla 102", "পরের ধাপ"), "103": ("Bangla 103", "আরও এগিয়ে")}),
    "ict": dict(name="ICT", bn_name="তথ্য ও যোগাযোগ প্রযুক্তি", badge="💻", intro="HSC ICT — বাংলায়, ধাপে ধাপে।",
                courses={"101": ("ICT 101", "শুরুর ধারণা"), "102": ("ICT 102", "পরের ধাপ"), "103": ("ICT 103", "আরও এগিয়ে")}),
}
OPEN = {("english", "101")}
ENGLISH_META = "২০ Day · ২০০ শব্দ · ৪০০ বাক্য"


def subject_meta(k):
    return ENGLISH_META if k == "english" else "🔒 শীঘ্রই আসছে"


def home():
    cards = "".join(
        f'<a class="card lang s-{k}" href="{k}/index.html"><div class="badge">{v["badge"]}</div><div><b>{v["name"]} — {v["bn_name"]}</b>'
        f'<span>{v["intro"]}</span><br><span style="font-size:14px">{subject_meta(k)}</span></div></a>' for k, v in SUBJECTS.items())
    body = (f'<header class="hero"><div class="in hero-grid"><div><p class="eyebrow" data-greet>স্বাগতম, ঐশী! 👋</p><h1>{FULL_NAME}</h1>'
            f'<p>ইংরেজি, বিজ্ঞান, গণিত, বাংলা আর ICT — বাংলায়, ধাপে ধাপে, মোবাইলে সহজে।</p></div>{avatar("", "hero-ava", small=False)}</div></header>'
            f'<main class="wrap">{cards}<p class="note">🔊 প্রতিটি শব্দ আর বাক্য শুনতে পাবে · 👆 স্লাইডে বাঁ-ডানে swipe করো · ✅ তোমার অগ্রগতি এই ফোনেই জমা থাকে</p></main>')
    write("index.html", page(f"{FULL_NAME}-এর পড়ার ঘর", body, 0, "home",
                             "শুধু ঐশী দেবনাথের জন্য: ইংরেজি, পদার্থবিজ্ঞান, রসায়ন, জীববিজ্ঞান, গণিত, বাংলা ও ICT — বাংলায়।"))


def subject_page(k, v):
    cards = []
    for slug, (title, tag) in v["courses"].items():
        if (k, slug) in OPEN:
            c = E.COURSE
            cards.append(f'<a class="card course" href="{slug}/index.html"><span class="tag">{slug}</span><b>{c["title"]} — {c["tag"]}</b>'
                         f'<span class="sub">{c["sub"]}</span><span class="sub">{ENGLISH_META}</span></a>')
        else:
            cards.append(f'<div class="card course locked"><span class="tag">{slug}</span><b>{title}</b><span class="sub">🔒 শীঘ্রই আসছে</span></div>')
    body = (f'<header class="hero"><div class="in hero-grid"><div><a class="back" href="../index.html">← হোম</a><h1>{v["name"]} — {v["bn_name"]}</h1><p>{v["intro"]}</p></div>{avatar("../", "hero-ava sm")}</div></header>'
            f'<main class="wrap">{"".join(cards)}</main>')
    write(f"{k}/index.html", page(f"{v['name']} — {FULL_NAME}-এর পড়ার ঘর", body, 1, "sub" if k != "english" else "en"))


def course_page_english():
    v, c = SUBJECTS["english"], E.COURSE
    days = []
    for n in range(1, 21):
        d = E.DAYS[n - 1]
        days.append(f'<a class="day" data-deckkey="english/101/day-{n:02d}" href="day-{n:02d}/index.html"><span class="n">Day<b>{bn(n)}</b></span>'
                    f'<span class="t"><b>{esc(d["en"])}</b><span>{esc(d["bn"])} · ১০ শব্দ · ২০ বাক্য</span></span><span class="tick">✓</span></a>')
    body = (f'<header class="hero"><div class="in hero-grid"><div><a class="back" href="../index.html">← {v["name"]}</a><h1>{c["title"]}</h1><p>{c["lead"]}</p></div>{avatar("../../", "hero-ava sm")}</div></header>'
            f'<main class="wrap"><div class="card"><div class="bar"><i id="progress"></i></div>'
            f'<p class="note" id="streak"></p><p class="note" id="progress-text">০ / {bn(20)} দিন শেষ</p>'
            f'<p style="text-align:center;margin-top:10px"><a class="btn" id="continue" href="day-01/index.html">▶ শুরু করুন</a></p></div>'
            f'<div class="days">{"".join(days)}</div></main>')
    write("english/101/index.html", page(f"{c['title']} — {c['tag']}", body, 2, "en"))


def not_found():
    body = ('<header class="hero"><div class="in"><h1>পাতাটি পাওয়া যায়নি</h1><p>ঠিকানাটা ভুল হতে পারে।</p></div></header>'
            '<main class="wrap"><a class="card" href="/" style="text-align:center"><b>🏠 হোমে ফিরে যান</b></a></main>')
    html = page("404 — পাতা নেই", body, 0, "home")
    # 404.html is served from any depth, so work out the site root at run time (project page vs custom domain)
    html = html.replace('<link rel="stylesheet" href="assets/app.css">', "").replace('<script src="assets/app.js"></script>', "")
    html = html.replace('href="/"', 'href="/" id="home404"').replace("</body>", """<script>
var root = /\\.github\\.io$/.test(location.hostname) ? '/' + location.pathname.split('/')[1] + '/' : '/';
document.getElementById('home404').href = root;
var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = root + 'assets/app.css'; document.head.appendChild(l);
</script></body>""")
    write("404.html", html)


if __name__ == "__main__":
    for k in SUBJECTS:
        shutil.rmtree(ROOT / k, ignore_errors=True)
    home()
    for k, v in SUBJECTS.items():
        subject_page(k, v)
    course_page_english()
    for d in E.DAYS:
        site_english.build_day(d)
    not_found()
    print(f"built {sum(1 for _ in ROOT.rglob('index.html'))} pages")
