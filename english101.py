"""English 101 — গল্পে গল্পে ইংরেজি (Oishi Debnath). Twenty days; each day = one short story about Oishi, 10 words, 20 sentences,
one grammar tip and a quiz. Data only: engine.py turns it into slides.

Format of the text blocks: one item per line, cells separated by ' | '.
story / sentences: English | Bangla          words: English | Bangla pronunciation | Bangla meaning

Content rule: whenever a doctor of her parents is meant, always say "homeopathic doctor" (never bare "doctor").
"""
from engine import parse_pairs

COURSE = dict(slug="101", lang="english", title="English 101", tag="গল্পে গল্পে ইংরেজি",
              sub="প্রতিটি Day-তে একটা ছোট গল্প, ১০টি শব্দ আর ২০টি বাক্য",
              lead="ঐশীর জীবনের গল্প পড়তে পড়তে ইংরেজি শিখো — সহজ শব্দ, রোজকার বাক্য, শুনে শুনে। পড়াশোনা, জীববিজ্ঞান আর হোমিওপ্যাথির কথায়।")

DAYS = []


def day(n, en_title, bn_title, intro, story, words, sentences, grammar):
    DAYS.append(dict(
        n=n, en=en_title, bn=bn_title, intro=intro,
        story=parse_pairs(story), words=parse_pairs(words, 3), sentences=parse_pairs(sentences), grammar=grammar))


# ======================================================================= Day 1
day(1, "Hello, I am Oishi", "পরিচয়", "আজ ঐশীর সাথে পরিচয় হবে — নিজের পরিচয় দিতে আর অন্যের পরিচয় জানতে শিখব।",
"""
Hello! My name is Oishi Debnath. | হ্যালো! আমার নাম ঐশী দেবনাথ।
I am from Bangladesh. | আমি বাংলাদেশের মেয়ে।
I am a student. | আমি একজন ছাত্রী।
I passed my SSC exam. | আমি এসএসসি পরীক্ষায় পাস করেছি।
Now I am studying for HSC. | এখন আমি এইচএসসির জন্য পড়ছি।
I love biology. | আমি জীববিজ্ঞান ভালোবাসি।
This is my cousin, Sanjoy. | ইনি আমার মাসতুতো ভাই, সঞ্জয়।
Nice to meet you! | আপনার সাথে দেখা হয়ে ভালো লাগল!
""",
"""
hello | হ্যালো | হ্যালো, নমস্কার
name | নেইম | নাম
student | স্টুডেন্ট | ছাত্র/ছাত্রী
friend | ফ্রেন্ড | বন্ধু
cousin | কাজিন | মামাতো/মাসতুতো/খালাতো ভাইবোন
biology | বায়োলজি | জীববিজ্ঞান
fine | ফাইন | ভালো, সুস্থ
please | প্লিজ | দয়া করে
sorry | সরি | দুঃখিত
welcome | ওয়েলকাম | স্বাগতম
""",
"""
Hello, I am Oishi. | হ্যালো, আমি ঐশী।
My name is Oishi Debnath. | আমার নাম ঐশী দেবনাথ।
What is your name? | আপনার নাম কী?
Nice to meet you. | আপনার সাথে দেখা হয়ে ভালো লাগল।
Nice to meet you, too. | আপনার সাথেও দেখা হয়ে ভালো লাগল।
How are you? | আপনি কেমন আছেন?
I am fine, thank you. | আমি ভালো আছি, ধন্যবাদ।
And you? | আর আপনি?
I am from Bangladesh. | আমি বাংলাদেশ থেকে।
Where are you from? | আপনি কোথা থেকে এসেছেন?
I am a student. | আমি একজন ছাত্রী।
I study in HSC. | আমি এইচএসসিতে পড়ি।
Are you a student? | আপনি কি ছাত্র?
Yes, I am. | হ্যাঁ, আমি।
No, I am not. | না, আমি না।
This is my cousin, Sanjoy. | ইনি আমার মাসতুতো ভাই, সঞ্জয়।
He is my friend, too. | সে আমার বন্ধুও।
I love biology. | আমি জীববিজ্ঞান ভালোবাসি।
Please call me Oishi. | দয়া করে আমাকে ঐশী বলে ডাকুন।
Thank you very much. | অনেক ধন্যবাদ।
""",
dict(title="am, is, are — “হওয়া” ক্রিয়া",
     points=["<b>I am</b> — আমি (<b>I'm</b> সংক্ষেপে)", "<b>You are</b> — তুমি/আপনি/তোমরা", "<b>He / She / It is</b> — সে, এটা", "<b>We / They are</b> — আমরা, তারা"],
     table=[("I", "am", "I am a student."), ("You", "are", "You are my friend."), ("She", "is", "She is Oishi.")],
     quiz=("She ___ a student.", ["am", "is", "are"], 1, "She-এর সাথে is বসে।")))

# ======================================================================= Day 2
day(2, "My Family", "আমার পরিবার", "আজ নিজের পরিবারের কথা বলতে শিখব — বাবা, মা, ভাই।",
"""
I have a small family. | আমার একটি ছোট পরিবার আছে।
This is my father, Bimol Debnath. | ইনি আমার বাবা, বিমল দেবনাথ।
He is a homeopathic doctor. | তিনি একজন হোমিওপ্যাথিক ডাক্তার।
This is my mother, Zumur Rani Debnath. | ইনি আমার মা, ঝুমুর রানী দেবনাথ।
She is also a homeopathic doctor. | তিনিও একজন হোমিওপ্যাথিক ডাক্তার।
I have a younger brother, Raj. | আমার একটি ছোট ভাই আছে, রাজ।
We live together. | আমরা একসাথে থাকি।
I love my family. | আমি আমার পরিবারকে ভালোবাসি।
""",
"""
family | ফ্যামিলি | পরিবার
father | ফাদার | বাবা
mother | মাদার | মা
parents | পেরেন্টস | বাবা-মা
brother | ব্রাদার | ভাই
sister | সিস্টার | বোন
uncle | আংকল | কাকা, মামা, মেসো
aunt | আন্ট | কাকি, মামি, মাসি
grandfather | গ্র্যান্ডফাদার | দাদা, নানা
love | লাভ | ভালোবাসা
""",
"""
This is my father. | ইনি আমার বাবা।
This is my mother. | ইনি আমার মা।
My father is a homeopathic doctor. | আমার বাবা একজন হোমিওপ্যাথিক ডাক্তার।
My mother is also a homeopathic doctor. | আমার মা-ও একজন হোমিওপ্যাথিক ডাক্তার।
My parents are homeopathic doctors. | আমার বাবা-মা হোমিওপ্যাথিক ডাক্তার।
I have a younger brother. | আমার একটি ছোট ভাই আছে।
His name is Raj. | তার নাম রাজ।
I don't have a sister. | আমার কোনো বোন নেই।
Do you have a brother? | আপনার কি ভাই আছে?
Yes, I have one brother. | হ্যাঁ, আমার একটি ভাই আছে।
How many people are in your family? | আপনার পরিবারে কতজন মানুষ?
There are four people in my family. | আমার পরিবারে চারজন মানুষ।
Sanjoy is my cousin. | সঞ্জয় আমার মাসতুতো ভাই।
He is my mother's sister's son. | সে আমার মাসির ছেলে।
My aunt is very kind. | আমার মাসি খুব দয়ালু।
We eat dinner together. | আমরা একসাথে রাতের খাবার খাই।
I love my parents. | আমি আমার বাবা-মাকে ভালোবাসি।
Raj is my younger brother. | রাজ আমার ছোট ভাই।
Our family is happy. | আমাদের পরিবার সুখী।
I love my family. | আমি আমার পরিবারকে ভালোবাসি।
""",
dict(title="have / has — আছে",
     points=["<b>I / You / We / They have</b> — আছে", "<b>He / She / It has</b> — আছে", "না: <b>don't have / doesn't have</b> — নেই", "প্রশ্ন: <b>Do you have</b> a brother?"],
     table=[("I", "have", "I have a brother."), ("She", "has", "She has a sister."), ("They", "have", "They have a car.")],
     quiz=("My brother ___ a book.", ["have", "has", "having"], 1, "My brother = He, তাই has।")))

# ======================================================================= Day 3
day(3, "My Day", "আমার একটি দিন", "আজ সারাদিনের রুটিন বলতে শিখব — সকাল থেকে রাত।",
"""
I wake up at six in the morning. | আমি সকালে ছয়টায় ঘুম থেকে উঠি।
I wash my face and have breakfast. | আমি মুখ ধুই আর নাস্তা করি।
At seven, I study biology. | সাতটায় আমি জীববিজ্ঞান পড়ি।
I go to college at nine. | আমি নয়টায় কলেজে যাই।
I come home in the afternoon. | আমি বিকেলে বাড়ি ফিরি।
In the evening, I read my books. | সন্ধ্যায় আমি আমার বই পড়ি।
I go to bed at ten. | আমি দশটায় ঘুমাতে যাই।
It is a busy day, but I like it. | ব্যস্ত দিন, কিন্তু আমার ভালো লাগে।
""",
"""
wake | ওয়েইক | ঘুম থেকে ওঠা
breakfast | ব্রেকফাস্ট | সকালের নাস্তা
morning | মর্নিং | সকাল
afternoon | আফটারনুন | বিকেল, দুপুরের পর
evening | ঈভনিং | সন্ধ্যা
night | নাইট | রাত
sleep | স্লিপ | ঘুমানো
college | কলেজ | কলেজ
book | বুক | বই
early | আর্লি | তাড়াতাড়ি
""",
"""
I wake up at six. | আমি ছয়টায় উঠি।
What time do you wake up? | আপনি কয়টায় ঘুম থেকে ওঠেন?
I wash my face. | আমি মুখ ধুই।
I have breakfast at seven. | আমি সাতটায় নাস্তা করি।
I drink a glass of milk. | আমি এক গ্লাস দুধ খাই।
I go to college at nine. | আমি নয়টায় কলেজে যাই।
What time does your college start? | আপনার কলেজ কয়টায় শুরু হয়?
It starts at nine. | এটা নয়টায় শুরু হয়।
I come home at four. | আমি চারটায় বাড়ি আসি।
I study in the evening. | আমি সন্ধ্যায় পড়ি।
I read biology for two hours. | আমি দুই ঘণ্টা জীববিজ্ঞান পড়ি।
I have dinner at eight. | আমি আটটায় রাতের খাবার খাই।
What time is it? | এখন কয়টা বাজে?
It is half past eight. | সাড়ে আটটা বাজে।
I am late. | আমার দেরি হয়েছে।
I am not late. | আমার দেরি হয়নি।
I go to bed at ten. | আমি দশটায় ঘুমাতে যাই।
I sleep early. | আমি তাড়াতাড়ি ঘুমাই।
Good night. | শুভ রাত্রি।
Sweet dreams! | মিষ্টি স্বপ্ন দেখো!
""",
dict(title="Present Simple — রোজকার কাজ",
     points=["রোজকার কাজে verb-এর আসল রূপ: I <b>wake</b> up. We <b>study</b>.", "He / She / It-এর সাথে verb-এ <b>s</b>: She <b>wakes</b> up.", "না: <b>don't / doesn't + verb</b> — I don't sleep late."],
     table=[("I", "wake up", "আমি উঠি"), ("She", "wakes up", "সে ওঠে"), ("We", "study", "আমরা পড়ি")],
     quiz=("She ___ up at six.", ["wake", "wakes", "waking"], 1, "She-এর সাথে verb-এ s: wakes।")))

# ======================================================================= Day 4
day(4, "My Subjects", "আমার বিষয়গুলো", "আজ পড়ার বিষয়, শিক্ষক আর পরীক্ষার কথা বলতে শিখব।",
"""
I study seven subjects. | আমি সাতটি বিষয় পড়ি।
Physics is hard but interesting. | পদার্থবিজ্ঞান কঠিন কিন্তু মজার।
Chemistry has many formulas. | রসায়নে অনেক সূত্র আছে।
Math needs a lot of practice. | গণিতে অনেক অনুশীলন লাগে।
Biology is my favourite subject. | জীববিজ্ঞান আমার প্রিয় বিষয়।
I also study Bangla, English and ICT. | আমি বাংলা, ইংরেজি আর ICT-ও পড়ি।
My teachers say, "Practice every day." | আমার শিক্ষকরা বলেন, "রোজ অনুশীলন করো।"
Hard work now gives a bright future. | এখনকার কঠোর পরিশ্রম উজ্জ্বল ভবিষ্যৎ দেয়।
""",
"""
physics | ফিজিক্স | পদার্থবিজ্ঞান
chemistry | কেমিস্ট্রি | রসায়ন
math | ম্যাথ | গণিত
subject | সাবজেক্ট | বিষয়
teacher | টিচার | শিক্ষক
exam | এগজাম | পরীক্ষা
homework | হোমওয়ার্ক | বাড়ির কাজ
favourite | ফেইভারিট | প্রিয়
difficult | ডিফিকাল্ট | কঠিন
easy | ঈজি | সহজ
""",
"""
What subjects do you study? | আপনি কোন কোন বিষয় পড়েন?
I study physics, chemistry and biology. | আমি পদার্থবিজ্ঞান, রসায়ন আর জীববিজ্ঞান পড়ি।
Biology is my favourite subject. | জীববিজ্ঞান আমার প্রিয় বিষয়।
What is your favourite subject? | আপনার প্রিয় বিষয় কী?
Math is difficult for me. | গণিত আমার কাছে কঠিন।
English is easy. | ইংরেজি সহজ।
I have a physics class today. | আজ আমার পদার্থবিজ্ঞানের ক্লাস আছে।
Who is your math teacher? | আপনার গণিতের শিক্ষক কে?
My teacher is very good. | আমার শিক্ষক খুব ভালো।
May I ask a question? | আমি কি একটি প্রশ্ন করতে পারি?
Please explain it again. | দয়া করে আবার বুঝিয়ে দিন।
I don't understand this. | আমি এটা বুঝতে পারছি না।
I understand now. | আমি এখন বুঝেছি।
Do you have homework today? | আজ কি আপনার হোমওয়ার্ক আছে?
I must finish my homework. | আমাকে হোমওয়ার্ক শেষ করতে হবে।
The exam is next week. | পরীক্ষা আগামী সপ্তাহে।
I am studying for the exam. | আমি পরীক্ষার জন্য পড়ছি।
I need more practice. | আমার আরও অনুশীলন দরকার।
Practice makes perfect. | অনুশীলনেই দক্ষতা আসে।
Good luck with your exam! | পরীক্ষায় শুভকামনা!
""",
dict(title="must / have to — বাধ্যবাধকতা",
     points=["<b>must + verb</b> — করতেই হবে: I must finish my homework.", "<b>have to / has to</b> — একই অর্থ: She has to study.", "<b>mustn't</b> — করা নিষেধ: You mustn't talk in the exam."],
     table=[("I", "must study", "আমাকে পড়তেই হবে"), ("She", "has to go", "তাকে যেতে হবে"), ("You", "mustn't cheat", "নকল করা নিষেধ")],
     quiz=("You ___ be quiet in the exam hall. (নিয়ম)", ["must", "mustn't", "can"], 0, "নিয়ম/বাধ্যবাধকতা বোঝাতে must।")))

# ======================================================================= Day 5
day(5, "At My Parents' Chamber", "বাবা-মায়ের চেম্বারে", "আজ রোগী, ওষুধ আর হোমিওপ্যাথিক ডাক্তারের কথা ইংরেজিতে বলতে শিখব।",
"""
In the afternoon, I go to my parents' chamber. | বিকেলে আমি বাবা-মায়ের চেম্বারে যাই।
Many patients wait there. | সেখানে অনেক রোগী অপেক্ষা করেন।
My father is a homeopathic doctor. | আমার বাবা একজন হোমিওপ্যাথিক ডাক্তার।
He asks, "What is your problem?" | তিনি জিজ্ঞেস করেন, "আপনার সমস্যা কী?"
The patient says, "I have a cough and a fever." | রোগী বলেন, "আমার কাশি আর জ্বর।"
My mother, a homeopathic doctor too, writes the medicine. | আমার মা, তিনিও একজন হোমিওপ্যাথিক ডাক্তার, ওষুধ লিখে দেন।
The patient takes the medicine and says thank you. | রোগী ওষুধ নেন আর ধন্যবাদ বলেন।
People respect my parents, and I feel proud. | মানুষ আমার বাবা-মাকে সম্মান করে, আর আমি গর্বিত বোধ করি।
""",
"""
chamber | চেম্বার | চেম্বার, চিকিৎসকের বসার ঘর
patient | পেশেন্ট | রোগী
homeopathic doctor | হোমিওপ্যাথিক ডক্টর | হোমিওপ্যাথিক ডাক্তার
medicine | মেডিসিন | ওষুধ
problem | প্রবলেম | সমস্যা
cough | কফ | কাশি
fever | ফিভার | জ্বর
wait | ওয়েট | অপেক্ষা করা
write | রাইট | লেখা
watch | ওয়াচ | দেখা, লক্ষ করা
""",
"""
This is my parents' chamber. | এটা আমার বাবা-মায়ের চেম্বার।
Many patients come here. | অনেক রোগী এখানে আসেন।
The patient is waiting. | রোগী অপেক্ষা করছেন।
Please sit here. | দয়া করে এখানে বসুন।
What is your problem? | আপনার সমস্যা কী?
I have a cough. | আমার কাশি আছে।
I have a fever. | আমার জ্বর আছে।
For how long? | কতদিন ধরে?
For two days. | দুই দিন ধরে।
My father is a homeopathic doctor. | আমার বাবা একজন হোমিওপ্যাথিক ডাক্তার।
My mother is a homeopathic doctor, too. | আমার মা-ও একজন হোমিওপ্যাথিক ডাক্তার।
The homeopathic doctor checks the patient. | হোমিওপ্যাথিক ডাক্তার রোগীকে পরীক্ষা করেন।
He writes the name of the medicine. | তিনি ওষুধের নাম লেখেন।
Take this medicine twice a day. | এই ওষুধ দিনে দুইবার খান।
Take it after food. | খাবারের পরে খান।
Drink warm water. | কুসুম গরম পানি পান করুন।
Come again after three days. | তিন দিন পরে আবার আসবেন।
Thank you very much. | অনেক ধন্যবাদ।
Patients respect the homeopathic doctor. | রোগীরা হোমিওপ্যাথিক ডাক্তারকে সম্মান করেন।
Get well soon! | শিগগিরই সুস্থ হয়ে উঠুন!
""",
dict(title="প্রশ্নের শব্দ: What, When, Where, How",
     points=["<b>What</b> — কী: What is your problem?", "<b>When</b> — কখন: When did it start?", "<b>Where</b> — কোথায়: Where does it hurt?", "<b>How</b> — কীভাবে: How are you feeling?"],
     table=[("What", "is your name?", "আপনার নাম কী?"), ("Where", "does it hurt?", "কোথায় ব্যথা?"), ("How", "many days?", "কত দিন?")],
     quiz=("___ does it hurt? (কোথায় ব্যথা)", ["What", "Where", "Who"], 1, "জায়গা জিজ্ঞেস করতে Where।")))

# ======================================================================= Day 6
day(6, "My Body", "আমার শরীর", "আজ শরীরের অংশ আর কাজের কথা বলতে শিখব।",
"""
Today I study the human body. | আজ আমি মানবদেহ পড়ি।
The head has the brain. | মাথায় মস্তিষ্ক থাকে।
The heart pumps blood. | হৃৎপিণ্ড রক্ত পাম্প করে।
We breathe with our lungs. | আমরা ফুসফুস দিয়ে শ্বাস নিই।
We see with our eyes and hear with our ears. | আমরা চোখ দিয়ে দেখি আর কান দিয়ে শুনি।
We eat with our mouth. | আমরা মুখ দিয়ে খাই।
The body needs food and water. | শরীরের খাবার আর পানি দরকার।
The human heart beats about one hundred thousand times a day. | মানুষের হৃৎপিণ্ড দিনে প্রায় এক লক্ষ বার স্পন্দিত হয়।
""",
"""
body | বডি | শরীর
brain | ব্রেইন | মস্তিষ্ক
heart | হার্ট | হৃৎপিণ্ড
blood | ব্লাড | রক্ত
lungs | লাংস | ফুসফুস
bone | বোন | হাড়
skin | স্কিন | ত্বক
stomach | স্টমাক | পেট, পাকস্থলী
hand | হ্যান্ড | হাত
leg | লেগ | পা
""",
"""
This is my head. | এটা আমার মাথা।
This is my hand. | এটা আমার হাত।
I have two eyes and two ears. | আমার দুইটি চোখ আর দুইটি কান।
I have ten fingers. | আমার দশটি আঙুল।
The heart pumps blood. | হৃৎপিণ্ড রক্ত পাম্প করে।
We breathe with our lungs. | আমরা ফুসফুস দিয়ে শ্বাস নিই।
The brain controls the body. | মস্তিষ্ক শরীরকে নিয়ন্ত্রণ করে।
The stomach digests food. | পাকস্থলী খাবার হজম করে।
Bones are hard. | হাড় শক্ত।
Skin protects the body. | ত্বক শরীরকে রক্ষা করে।
My legs are tired. | আমার পা ক্লান্ত।
My hand hurts. | আমার হাতে ব্যথা করছে।
Open your mouth. | মুখ খুলুন।
Show me your tongue. | আপনার জিভ দেখান।
Breathe in, breathe out. | শ্বাস নিন, শ্বাস ছাড়ুন।
My heart is beating fast. | আমার হৃৎপিণ্ড জোরে লাফাচ্ছে।
Wash your hands. | হাত ধোও।
Keep your body clean. | শরীর পরিষ্কার রাখো।
Health is wealth. | স্বাস্থ্যই সম্পদ।
A homeopathic doctor knows the human body very well. | হোমিওপ্যাথিক ডাক্তার মানবদেহ খুব ভালোভাবে জানেন।
""",
dict(title="একবচন ও বহুবচন",
     points=["সাধারণত শেষে <b>-s</b>: hand → <b>hands</b>, bone → <b>bones</b>", "শেষে s/sh/ch/x থাকলে <b>-es</b>: box → <b>boxes</b>", "অনিয়মিত: child → <b>children</b>, tooth → <b>teeth</b>, foot → <b>feet</b>"],
     table=[("one eye", "two eyes", "একটি চোখ — দুইটি চোখ"), ("one hand", "two hands", "একটি হাত — দুইটি হাত"), ("one tooth", "two teeth", "একটি দাঁত — দুইটি দাঁত")],
     quiz=("I have two ___.", ["hand", "hands", "handes"], 1, "দুইটি হলে বহুবচন: hands।")))

# ======================================================================= Day 7
day(7, "Biology Class", "জীববিজ্ঞানের ক্লাস", "আজ কোষ, গাছপালা আর প্রাণীর কথা ইংরেজিতে বলতে শিখব।",
"""
Today is my favourite class — biology. | আজ আমার প্রিয় ক্লাস — জীববিজ্ঞান।
The teacher shows a cell under the microscope. | শিক্ষক অণুবীক্ষণ যন্ত্রে একটি কোষ দেখান।
Every living thing is made of cells. | প্রতিটি জীব কোষ দিয়ে তৈরি।
Plants make food from sunlight. | গাছ সূর্যের আলো থেকে খাবার তৈরি করে।
Animals eat plants or other animals. | প্রাণীরা গাছ বা অন্য প্রাণী খায়।
I draw the cell in my notebook. | আমি আমার খাতায় কোষটি আঁকি।
I label the parts. | আমি অংশগুলোর নাম লিখি।
"Biology helps us understand life," says the teacher. | "জীববিজ্ঞান আমাদের জীবন বুঝতে সাহায্য করে," বলেন শিক্ষক।
""",
"""
cell | সেল | কোষ
microscope | মাইক্রোস্কোপ | অণুবীক্ষণ যন্ত্র
plant | প্ল্যান্ট | গাছ, উদ্ভিদ
animal | অ্যানিমাল | প্রাণী
leaf | লিফ | পাতা
root | রুট | শিকড়
seed | সীড | বীজ
flower | ফ্লাওয়ার | ফুল
living | লিভিং | জীবিত
nature | নেইচার | প্রকৃতি
""",
"""
This is a cell. | এটা একটি কোষ।
Look through the microscope. | অণুবীক্ষণ যন্ত্র দিয়ে দেখো।
Plants have leaves and roots. | গাছের পাতা আর শিকড় আছে।
A seed grows into a plant. | বীজ থেকে গাছ হয়।
Flowers are beautiful. | ফুল সুন্দর।
Plants need sunlight and water. | গাছের সূর্যের আলো আর পানি দরকার।
Animals need food and air. | প্রাণীর খাবার আর বাতাস দরকার।
This is a living thing. | এটা একটি জীবিত বস্তু।
A stone is not alive. | পাথর জীবিত নয়।
Draw this diagram. | এই চিত্রটি আঁকো।
Label the parts. | অংশগুলোর নাম লেখো।
I love drawing biology diagrams. | আমি জীববিজ্ঞানের চিত্র আঁকতে ভালোবাসি।
What is this called? | এটাকে কী বলে?
It is called a cell. | এটাকে কোষ বলে।
Fish live in water. | মাছ পানিতে থাকে।
Birds can fly. | পাখি উড়তে পারে।
Fish can't fly. | মাছ উড়তে পারে না।
Biology is interesting. | জীববিজ্ঞান মজার।
Your body is made of trillions of cells. | তোমার শরীর কোটি কোটি কোষ দিয়ে তৈরি।
A homeopathic doctor must understand life. | হোমিওপ্যাথিক ডাক্তারকে জীবন বুঝতে হয়।
""",
dict(title="can / can't — পারা, না পারা",
     points=["<b>can + verb</b> — পারে: Birds can fly.", "<b>can't (cannot) + verb</b> — পারে না: Fish can't fly.", "প্রশ্ন/অনুমতি: <b>Can</b> you see it?"],
     table=[("Birds", "can fly", "পাখি উড়তে পারে"), ("Fish", "can't fly", "মাছ উড়তে পারে না"), ("I", "can swim", "আমি সাঁতার কাটতে পারি")],
     quiz=("Fish ___ fly.", ["can", "can't", "are"], 1, "মাছ উড়তে পারে না: can't।")))

# ======================================================================= Day 8
day(8, "Health and Illness", "অসুস্থতা ও সুস্থতা", "আজ অসুস্থতার কথা আর পরামর্শ দিতে শিখব।",
"""
Raj has a fever today. | রাজের আজ জ্বর।
He feels weak and tired. | সে দুর্বল আর ক্লান্ত বোধ করে।
His mother, a homeopathic doctor, checks him. | তার মা, একজন হোমিওপ্যাথিক ডাক্তার, তাকে পরীক্ষা করেন।
"Drink more water and rest," she says. | "আরও পানি খাও আর বিশ্রাম নাও," তিনি বলেন।
She gives him some medicine. | তিনি তাকে কিছু ওষুধ দেন।
Raj sleeps for two hours. | রাজ দুই ঘণ্টা ঘুমায়।
In the evening, he feels better. | সন্ধ্যায় সে ভালো বোধ করে।
"Health is more important than games," says Raj. | "খেলার চেয়ে স্বাস্থ্য বেশি জরুরি," বলে রাজ।
""",
"""
illness | ইলনেস | অসুস্থতা
weak | উইক | দুর্বল
headache | হেডেইক | মাথাব্যথা
rest | রেস্ট | বিশ্রাম
advice | অ্যাডভাইস | পরামর্শ
better | বেটার | আরও ভালো
healthy | হেলদি | সুস্থ
cold | কোল্ড | সর্দি; ঠান্ডা
hurt | হার্ট | ব্যথা করা
recover | রিকভার | সুস্থ হয়ে ওঠা
""",
"""
How do you feel today? | আজ আপনি কেমন বোধ করছেন?
I don't feel well. | আমি ভালো বোধ করছি না।
I have a headache. | আমার মাথাব্যথা করছে।
I have a cold. | আমার সর্দি হয়েছে।
My throat hurts. | আমার গলা ব্যথা করছে।
My stomach hurts. | আমার পেট ব্যথা করছে।
I feel weak. | আমি দুর্বল বোধ করছি।
You should rest. | আপনার বিশ্রাম নেওয়া উচিত।
You should drink more water. | আপনার আরও পানি খাওয়া উচিত।
You shouldn't eat too much oily food. | আপনার বেশি তেলে ভাজা খাবার খাওয়া উচিত না।
Eat healthy food. | স্বাস্থ্যকর খাবার খাও।
Wash your hands before eating. | খাওয়ার আগে হাত ধোও।
Take the medicine on time. | সময়মতো ওষুধ খাও।
Get enough sleep. | যথেষ্ট ঘুমাও।
I feel better now. | আমি এখন ভালো বোধ করছি।
She is recovering well. | সে ভালোভাবে সুস্থ হয়ে উঠছে।
Come back if the fever stays. | জ্বর না কমলে আবার এসো।
A good homeopathic doctor can bring a smile back to a patient. | ভালো হোমিওপ্যাথিক ডাক্তার রোগীর মুখে আবার হাসি ফোটাতে পারেন।
Health is wealth. | স্বাস্থ্যই সম্পদ।
Get well soon! | শিগগিরই সুস্থ হয়ে উঠুন!
""",
dict(title="should / shouldn't — পরামর্শ",
     points=["<b>should + verb</b> — করা উচিত: You should rest.", "<b>shouldn't</b> — করা উচিত না: You shouldn't worry.", "প্রশ্ন: <b>Should I</b> take the medicine now?"],
     table=[("You", "should rest", "আপনার বিশ্রাম নেওয়া উচিত"), ("He", "should drink water", "তার পানি খাওয়া উচিত"), ("You", "shouldn't worry", "আপনার চিন্তা করা উচিত না")],
     quiz=("You ___ drink more water. (পরামর্শ)", ["should", "shouldn't", "are"], 0, "পরামর্শ দিতে should + verb।")))

# ======================================================================= Day 9
day(9, "Food and Nutrition", "খাবার ও পুষ্টি", "আজ খাবার, ভিটামিন আর সুষম খাদ্যের কথা বলতে শিখব।",
"""
Today's biology class is about food. | আজকের জীববিজ্ঞান ক্লাস খাবার নিয়ে।
Our body needs rice, fish, vegetables, fruits and water. | আমাদের শরীরের ভাত, মাছ, সবজি, ফল আর পানি দরকার।
Rice gives us energy. | ভাত আমাদের শক্তি দেয়।
Fish and eggs give us protein. | মাছ আর ডিম আমাদের প্রোটিন দেয়।
Fruits and vegetables give us vitamins. | ফল আর সবজি আমাদের ভিটামিন দেয়।
My mother cooks healthy food at home. | আমার মা বাড়িতে স্বাস্থ্যকর খাবার রান্না করেন।
I eat a banana and drink milk after school. | আমি স্কুলের পরে একটি কলা খাই আর দুধ পান করি।
"A balanced diet keeps us healthy," says the teacher. | "সুষম খাদ্য আমাদের সুস্থ রাখে," বলেন শিক্ষক।
""",
"""
energy | এনার্জি | শক্তি
protein | প্রোটিন | প্রোটিন, আমিষ
vitamin | ভিটামিন | ভিটামিন
vegetable | ভেজিটেবল | সবজি
fruit | ফ্রুট | ফল
diet | ডায়েট | খাদ্যাভ্যাস
balanced | ব্যালান্সড | সুষম
nutrition | নিউট্রিশন | পুষ্টি
fresh | ফ্রেশ | তাজা
sugar | সুগার | চিনি
""",
"""
Rice gives us energy. | ভাত আমাদের শক্তি দেয়।
Fish gives us protein. | মাছ আমাদের প্রোটিন দেয়।
Eggs have protein. | ডিমে প্রোটিন আছে।
Fruits have vitamins. | ফলে ভিটামিন আছে।
Vegetables are good for health. | সবজি স্বাস্থ্যের জন্য ভালো।
Eat fresh fruits every day. | রোজ তাজা ফল খাও।
Drink eight glasses of water. | আট গ্লাস পানি পান করো।
Too much sugar is bad for health. | বেশি চিনি স্বাস্থ্যের জন্য খারাপ।
Too much oily food is bad. | বেশি তেলে ভাজা খাবার খারাপ।
I eat rice, fish and vegetables. | আমি ভাত, মাছ আর সবজি খাই।
I like bananas and oranges. | আমি কলা আর কমলা পছন্দ করি।
What do you eat for breakfast? | আপনি নাস্তায় কী খান?
A balanced diet is important. | সুষম খাদ্য জরুরি।
Do you eat vegetables? | আপনি কি সবজি খান?
Yes, I eat them daily. | হ্যাঁ, আমি রোজ খাই।
No, I don't like bitter gourd. | না, আমি করলা পছন্দ করি না।
My mother cooks healthy food. | আমার মা স্বাস্থ্যকর খাবার রান্না করেন।
Don't skip breakfast. | নাস্তা বাদ দিয়ো না।
Eat slowly. | ধীরে ধীরে খাও।
A homeopathic doctor gives advice about food, too. | হোমিওপ্যাথিক ডাক্তার খাবার নিয়েও পরামর্শ দেন।
""",
dict(title="some, any, much, many",
     points=["<b>some</b> — কিছু (হ্যাঁ-বাক্যে): I eat some fruit.", "<b>any</b> — কোনো (না/প্রশ্নে): I don't eat any sugar.", "<b>many</b> — গোনা যায় এমন, অনেক: many eggs", "<b>much</b> — গোনা যায় না, অনেক: much sugar, much water"],
     table=[("many", "eggs, fruits", "গোনা যায়"), ("much", "sugar, water", "গোনা যায় না"), ("some / any", "দুটোতেই", "some = হ্যাঁ; any = না/প্রশ্ন")],
     quiz=("I don't eat ___ sugar.", ["many", "much", "a few"], 1, "চিনি গোনা যায় না → much।")))

# ======================================================================= Day 10
day(10, "Homeopathy Basics", "হোমিওপ্যাথির প্রাথমিক কথা", "আজ বাবা-মায়ের পেশা নিয়ে সহজ শব্দ শিখব — লক্ষণ, মাত্রা, ওষুধ।",
"""
My parents are homeopathic doctors. | আমার বাবা-মা হোমিওপ্যাথিক ডাক্তার।
A homeopathic doctor listens to the patient carefully. | হোমিওপ্যাথিক ডাক্তার রোগীর কথা মন দিয়ে শোনেন।
He asks about every symptom. | তিনি প্রতিটি লক্ষণ সম্পর্কে জিজ্ঞেস করেন।
Then he chooses the medicine. | তারপর তিনি ওষুধ বেছে নেন।
The medicine comes in small pills or in a bottle. | ওষুধ ছোট বড়ি বা শিশিতে আসে।
My father says, "Every patient is different." | আমার বাবা বলেন, "প্রতিটি রোগী আলাদা।"
Many families trust my parents and feel thankful. | অনেক পরিবার আমার বাবা-মাকে বিশ্বাস করে আর কৃতজ্ঞ থাকে।
Their work gives them respect, a good income and a happy life. | তাদের কাজ তাদের সম্মান, ভালো আয় আর সুখী জীবন দেয়।
""",
"""
homeopathy | হোমিওপ্যাথি | হোমিওপ্যাথি চিকিৎসা
symptom | সিম্পটম | লক্ষণ
dose | ডোজ | মাত্রা, ডোজ
pill | পিল | বড়ি
remedy | রেমেডি | প্রতিকার, ওষুধ
bottle | বটল | শিশি, বোতল
listen | লিসেন | মন দিয়ে শোনা
choose | চুজ | বেছে নেওয়া
different | ডিফারেন্ট | আলাদা
careful | কেয়ারফুল | সতর্ক
""",
"""
Homeopathy is a system of medicine. | হোমিওপ্যাথি একটি চিকিৎসা পদ্ধতি।
My parents work in homeopathy. | আমার বাবা-মা হোমিওপ্যাথিতে কাজ করেন।
A homeopathic doctor listens carefully. | হোমিওপ্যাথিক ডাক্তার মন দিয়ে শোনেন।
The homeopathic doctor asks many questions. | হোমিওপ্যাথিক ডাক্তার অনেক প্রশ্ন করেন।
Tell me your symptoms. | আপনার লক্ষণগুলো বলুন।
When did the symptoms start? | লক্ষণগুলো কখন শুরু হয়েছিল?
This is a small bottle. | এটা একটি ছোট শিশি।
These are small pills. | এগুলো ছোট ছোট বড়ি।
That bottle is empty. | ওই শিশিটা খালি।
Those pills are for the child. | ওই বড়িগুলো শিশুর জন্য।
Take the pills three times a day. | বড়ি দিনে তিনবার খান।
The dose is very small. | মাত্রা খুব কম।
Keep the bottle in a cool place. | শিশিটা ঠান্ডা জায়গায় রাখুন।
Keep it away from children. | এটা শিশুদের নাগালের বাইরে রাখুন।
Close the bottle tightly. | শিশির মুখ ভালো করে বন্ধ করুন।
Every patient is different. | প্রতিটি রোগী আলাদা।
Always follow the instructions. | সবসময় নির্দেশনা মেনে চলুন।
I want to learn about homeopathy. | আমি হোমিওপ্যাথি সম্পর্কে শিখতে চাই।
A homeopathic doctor helps many families. | একজন হোমিওপ্যাথিক ডাক্তার অনেক পরিবারকে সাহায্য করেন।
A homeopathic doctor earns respect and a good income. | একজন হোমিওপ্যাথিক ডাক্তার সম্মান আর ভালো আয় পান।
""",
dict(title="this / that / these / those",
     points=["<b>this</b> — কাছের একটি: this bottle", "<b>these</b> — কাছের অনেকগুলো: these pills", "<b>that</b> — দূরের একটি: that bottle", "<b>those</b> — দূরের অনেকগুলো: those pills"],
     table=[("this", "কাছে, একটি", "This bottle is small."), ("these", "কাছে, একাধিক", "These pills are small."), ("those", "দূরে, একাধিক", "Those books are old.")],
     quiz=("(কাছের অনেক বড়ি) ___ pills are small.", ["This", "These", "That"], 1, "কাছে + একাধিক = these।")))

# ======================================================================= Day 11
day(11, "Raj, My Little Brother", "রাজ, আমার ছোট ভাই", "আজ কারও বর্ণনা দিতে আর এখন কী হচ্ছে তা বলতে শিখব।",
"""
Raj is my younger brother. | রাজ আমার ছোট ভাই।
He loves football. | সে ফুটবল ভালোবাসে।
Right now, he is playing in the yard. | এই মুহূর্তে সে উঠানে খেলছে।
I am studying biology, and he is shouting. | আমি জীববিজ্ঞান পড়ছি, আর সে চিৎকার করছে।
"Raj, please be quiet!" I say. | "রাজ, দয়া করে চুপ করো!" আমি বলি।
He stops and smiles. | সে থামে আর হাসে।
Then he asks, "Why do we sneeze?" | তারপর সে জিজ্ঞেস করে, "আমরা হাঁচি দিই কেন?"
"Sneezing cleans the nose," I explain. "You know so much, Didi!" | "হাঁচি নাক পরিষ্কার করে," আমি বুঝিয়ে বলি। "দিদি, তুমি কত কিছু জানো!"
""",
"""
tall | টল | লম্বা
short | শর্ট | খাটো
clever | ক্লেভার | বুদ্ধিমান
naughty | নটি | দুষ্টু
noisy | নয়জি | গোলমেলে
smile | স্মাইল | হাসি; মুচকি হাসা
yard | ইয়ার্ড | উঠান
football | ফুটবল | ফুটবল
shout | শাউট | চিৎকার করা
sneeze | স্নিজ | হাঁচি দেওয়া
""",
"""
Raj is clever. | রাজ বুদ্ধিমান।
He is a little naughty. | সে একটু দুষ্টু।
He loves football. | সে ফুটবল ভালোবাসে।
He is playing in the yard. | সে উঠানে খেলছে।
What is he doing? | সে কী করছে?
He is shouting. | সে চিৎকার করছে।
I am studying now. | আমি এখন পড়ছি।
Please be quiet. | দয়া করে চুপ করো।
He is not listening. | সে শুনছে না।
Don't shout. | চিৎকার কোরো না।
He is smiling. | সে হাসছে।
He is eating a banana. | সে একটি কলা খাচ্ছে।
Raj is watching TV. | রাজ টিভি দেখছে।
We are playing a game together. | আমরা একসাথে একটি খেলা খেলছি।
Why do we sneeze? | আমরা হাঁচি দিই কেন?
Sneezing cleans the nose. | হাঁচি নাক পরিষ্কার করে।
A homeopathic doctor knows many such secrets. | হোমিওপ্যাথিক ডাক্তার এমন অনেক রহস্য জানেন।
Raj says, "You know so much, Didi!" | রাজ বলে, "দিদি, তুমি কত কিছু জানো!"
I love my little brother. | আমি আমার ছোট ভাইকে ভালোবাসি।
We are laughing. | আমরা হাসছি।
""",
dict(title="Present Continuous — এখন যা হচ্ছে",
     points=["<b>am / is / are + verb-ing</b> — এখন হচ্ছে", "I <b>am studying</b>. He <b>is playing</b>. They <b>are laughing</b>.", "না: He <b>isn't listening</b>. · প্রশ্ন: <b>What is he doing?</b>"],
     table=[("I", "am studying", "আমি পড়ছি"), ("He", "is playing", "সে খেলছে"), ("They", "are laughing", "তারা হাসছে")],
     quiz=("Raj ___ in the yard now.", ["play", "is playing", "plays"], 1, "এখন হচ্ছে: is + verb-ing।")))

# ======================================================================= Day 12
day(12, "Calling My Cousin", "ভাইকে ফোন", "আজ ফোনে কথা বলতে আর অনুরোধ করতে শিখব।",
"""
My cousin Sanjoy is learning English, too. | আমার ভাই সঞ্জয়ও ইংরেজি শিখছে।
He works at Medicine Corner, a medicine shop. | সে মেডিসিন কর্নার নামের একটি ওষুধের দোকানে কাজ করে।
Sometimes he calls me. | মাঝে মাঝে সে আমাকে ফোন করে।
"Hello, Oishi! How is your study?" | "হ্যালো ঐশী! তোমার পড়াশোনা কেমন চলছে?"
"It is going well." | "ভালোই চলছে।"
"Can you explain this word to me?" | "তুমি কি আমাকে এই শব্দটা বুঝিয়ে দিতে পারবে?"
"Of course! Let's learn together." | "অবশ্যই! চলো একসাথে শিখি।"
We laugh and share new words. | আমরা হাসি আর নতুন শব্দ ভাগ করি।
""",
"""
call | কল | ফোন করা
phone | ফোন | ফোন
message | মেসেজ | বার্তা
shop | শপ | দোকান
talk | টক | কথা বলা
share | শেয়ার | ভাগ করা
laugh | ল্যাফ | হাসা
learn | লার্ন | শেখা
help | হেল্প | সাহায্য করা
together | টুগেদার | একসাথে
""",
"""
Hello, who is this? | হ্যালো, কে বলছেন?
This is Oishi speaking. | ঐশী বলছি।
Can I speak to Sanjoy? | আমি কি সঞ্জয়ের সাথে কথা বলতে পারি?
Please wait a moment. | দয়া করে এক মুহূর্ত অপেক্ষা করুন।
I will call you later. | আমি পরে তোমাকে ফোন করব।
Call me tomorrow. | কাল আমাকে ফোন কোরো।
I will send you a message. | আমি তোমাকে একটি বার্তা পাঠাব।
Are you free today? | তুমি কি আজ ফ্রি?
I am busy now. | আমি এখন ব্যস্ত।
How is your study? | তোমার পড়াশোনা কেমন চলছে?
It is going well. | ভালোই চলছে।
Are you learning English? | তুমি কি ইংরেজি শিখছ?
Yes, I am learning every day. | হ্যাঁ, আমি রোজ শিখছি।
Sanjoy works at a medicine shop. | সঞ্জয় একটি ওষুধের দোকানে কাজ করে।
Could you help me, please? | তুমি কি আমাকে একটু সাহায্য করবে?
Can you explain this word? | তুমি কি এই শব্দটা বুঝিয়ে দিতে পারবে?
May I use your phone? | আমি কি তোমার ফোনটা ব্যবহার করতে পারি?
Can you hear me? | তুমি কি আমার কথা শুনতে পাচ্ছ?
Let's study together. | চলো একসাথে পড়ি।
Talk to you soon! | শিগগিরই কথা হবে!
""",
dict(title="Can / Could / May — ভদ্র অনুরোধ",
     points=["<b>Can you …?</b> — সাধারণ অনুরোধ: Can you help me?", "<b>Could you …?</b> — আরও ভদ্র: Could you help me, please?", "<b>May I …?</b> — অনুমতি চাওয়া: May I use your phone?"],
     table=[("Can you", "help me?", "আমাকে সাহায্য করবে?"), ("Could you", "wait, please?", "দয়া করে অপেক্ষা করবেন?"), ("May I", "come in?", "আমি কি ঢুকতে পারি?")],
     quiz=("___ I come in? (অনুমতি)", ["May", "Must", "Will"], 0, "অনুমতি চাইতে May I।")))

# ======================================================================= Day 13
day(13, "Numbers, Dates and Exams", "সংখ্যা, তারিখ ও পরীক্ষা", "আজ সংখ্যা, মাস আর পরীক্ষার পরিকল্পনা নিয়ে কথা বলতে শিখব।",
"""
The HSC exam is coming. | এইচএসসি পরীক্ষা আসছে।
"How many days are left?" asks Oishi. | "আর কত দিন বাকি?" জিজ্ঞেস করে ঐশী।
"Forty days," says her friend. | "চল্লিশ দিন," বলে তার বন্ধু।
Oishi makes a plan. | ঐশী একটি পরিকল্পনা করে।
She studies two chapters every day. | সে রোজ দুইটি অধ্যায় পড়ে।
On Friday, she takes a model test. | শুক্রবার সে একটি মডেল টেস্ট দেয়।
She gets seventy out of one hundred. | সে একশোর মধ্যে সত্তর পায়।
"Next time, I will get more," she says. | "পরের বার আমি আরও বেশি পাব," সে বলে।
""",
"""
number | নাম্বার | সংখ্যা, নম্বর
date | ডেইট | তারিখ
month | মান্থ | মাস
chapter | চ্যাপ্টার | অধ্যায়
marks | মার্কস | নম্বর
test | টেস্ট | পরীক্ষা, যাচাই
plan | প্ল্যান | পরিকল্পনা
hundred | হান্ড্রেড | একশো
result | রেজাল্ট | ফল
pass | পাস | পাস করা
""",
"""
What is today's date? | আজকের তারিখ কত?
Today is the twenty-first of October. | আজ একুশে অক্টোবর।
My birthday is in March. | আমার জন্মদিন মার্চ মাসে।
When is your birthday? | আপনার জন্মদিন কবে?
It is on the fifth of May. | এটা পাঁচই মে।
How many days are left? | আর কত দিন বাকি?
Forty days are left. | চল্লিশ দিন বাকি।
One, two, three, four, five. | এক, দুই, তিন, চার, পাঁচ।
Ten, twenty, thirty, forty, fifty. | দশ, বিশ, ত্রিশ, চল্লিশ, পঞ্চাশ।
One hundred marks. | একশো নম্বর।
I made a study plan. | আমি একটি পড়ার পরিকল্পনা করেছি।
I study two chapters every day. | আমি রোজ দুইটি অধ্যায় পড়ি।
The test is on Friday. | পরীক্ষা শুক্রবার।
The exam starts at ten o'clock. | পরীক্ষা দশটায় শুরু।
I got seventy marks. | আমি সত্তর নম্বর পেয়েছি।
I will get more next time. | পরের বার আমি আরও বেশি পাব।
When will the result come? | ফল কবে আসবে?
I want to pass with good marks. | আমি ভালো নম্বর নিয়ে পাস করতে চাই।
Good marks open good doors. | ভালো নম্বর ভালো সুযোগের দরজা খোলে।
There are twelve months in a year. | এক বছরে বারো মাস।
""",
dict(title="in / on / at — সময়ের সাথে",
     points=["<b>in</b> — মাস, বছর, ঋতু: in March, in 2026", "<b>on</b> — দিন ও তারিখ: on Friday, on the fifth of May", "<b>at</b> — ঘড়ির সময়: at ten o'clock, at night"],
     table=[("in", "মাস / বছর", "in March"), ("on", "দিন / তারিখ", "on Friday"), ("at", "ঘড়ির সময়", "at ten")],
     quiz=("The test is ___ Friday.", ["in", "on", "at"], 1, "বারের আগে on বসে।")))

# ======================================================================= Day 14
day(14, "Rain, Mosquitoes and Science", "বৃষ্টি, মশা ও বিজ্ঞান", "আজ আবহাওয়ার কথা আর মশাবাহিত রোগ থেকে বাঁচার সহজ বিজ্ঞান শিখব।",
"""
It is the rainy season. | এখন বর্ষাকাল।
It rains almost every day. | প্রায় রোজ বৃষ্টি হয়।
Mosquitoes lay eggs in dirty water. | মশা নোংরা পানিতে ডিম পাড়ে।
Dengue spreads through mosquito bites. | ডেঙ্গু মশার কামড়ে ছড়ায়।
Oishi keeps her home clean and uses a mosquito net. | ঐশী তার ঘর পরিষ্কার রাখে আর মশারি ব্যবহার করে।
Raj carries an umbrella to school. | রাজ স্কুলে ছাতা নিয়ে যায়।
A homeopathic doctor teaches families how to stay safe. | হোমিওপ্যাথিক ডাক্তার পরিবারদের নিরাপদ থাকা শেখান।
After the rain, the air is fresh and cool. | বৃষ্টির পরে বাতাস তাজা আর ঠান্ডা।
""",
"""
rain | রেইন | বৃষ্টি
season | সীজন | ঋতু
cloud | ক্লাউড | মেঘ
wind | উইন্ড | বাতাস
umbrella | আমব্রেলা | ছাতা
mosquito | মসকিটো | মশা
net | নেট | জাল, মশারি
clean | ক্লিন | পরিষ্কার
dirty | ডার্টি | নোংরা
cool | কুল | ঠান্ডা, শীতল
""",
"""
How is the weather today? | আজ আবহাওয়া কেমন?
It is hot today. | আজ গরম।
It is raining. | বৃষ্টি হচ্ছে।
It is not raining now. | এখন বৃষ্টি হচ্ছে না।
The sky is cloudy. | আকাশ মেঘলা।
There is a strong wind. | জোরে বাতাস বইছে।
Take an umbrella. | ছাতা নিয়ে যাও।
This is the rainy season. | এখন বর্ষাকাল।
Mosquitoes lay eggs in dirty water. | মশা নোংরা পানিতে ডিম পাড়ে।
Don't keep water in old pots. | পুরনো পাত্রে পানি জমিয়ে রেখো না।
Keep your home clean. | ঘর পরিষ্কার রাখো।
Use a mosquito net at night. | রাতে মশারি ব্যবহার করো।
Dengue spreads through mosquitoes. | ডেঙ্গু মশার মাধ্যমে ছড়ায়।
If you have a high fever, see a homeopathic doctor. | তীব্র জ্বর হলে হোমিওপ্যাথিক ডাক্তার দেখাও।
A homeopathic doctor helps families stay safe. | হোমিওপ্যাথিক ডাক্তার পরিবারদের নিরাপদ থাকতে সাহায্য করেন।
Summer is hot. | গ্রীষ্ম গরম।
Winter is cold. | শীত ঠান্ডা।
I like the rain. | আমার বৃষ্টি ভালো লাগে।
The air is fresh after the rain. | বৃষ্টির পরে বাতাস তাজা।
What a lovely day! | কী সুন্দর দিন!
""",
dict(title="আবহাওয়া: It is … / It is raining",
     points=["অবস্থা বোঝাতে: <b>It is + adjective</b> — It is hot. It is cool.", "এখন হচ্ছে: <b>It is + verb-ing</b> — It is raining.", "প্রশ্ন: <b>How is the weather?</b>"],
     table=[("It is", "hot", "গরম"), ("It is", "raining", "বৃষ্টি হচ্ছে"), ("It is", "not cloudy", "মেঘলা নয়")],
     quiz=("Look! It ___ now.", ["rain", "is raining", "rains"], 1, "এখন হচ্ছে: is raining।")))

# ======================================================================= Day 15
day(15, "My Study Room", "আমার পড়ার ঘর", "আজ ঘরের জিনিসপত্র কোথায় আছে তা বলতে শিখব।",
"""
I study in a small room. | আমি একটি ছোট ঘরে পড়ি।
There is a table and a chair. | সেখানে একটি টেবিল আর একটি চেয়ার আছে।
My books are on the shelf. | আমার বইগুলো তাকে আছে।
There is a lamp on the table. | টেবিলে একটি বাতি আছে।
A chart of the human body is on the wall. | দেয়ালে মানবদেহের একটি চার্ট আছে।
Raj's football is under the bed. | রাজের ফুটবল খাটের নিচে।
Every evening, I read near the window. | প্রতি সন্ধ্যায় আমি জানালার কাছে পড়ি।
This small room is my big dream. | এই ছোট ঘরটাই আমার বড় স্বপ্ন।
""",
"""
room | রুম | ঘর
table | টেবিল | টেবিল
chair | চেয়ার | চেয়ার
shelf | শেলফ | তাক
lamp | ল্যাম্প | বাতি
wall | ওয়াল | দেয়াল
window | উইন্ডো | জানালা
door | ডোর | দরজা
bed | বেড | খাট
chart | চার্ট | চার্ট, ছক
""",
"""
This is my study room. | এটা আমার পড়ার ঘর।
There is a table in the room. | ঘরে একটি টেবিল আছে।
There are two chairs. | দুইটি চেয়ার আছে।
My books are on the shelf. | আমার বইগুলো তাকে আছে।
The lamp is on the table. | বাতিটা টেবিলে।
The chart is on the wall. | চার্টটা দেয়ালে।
The football is under the bed. | ফুটবলটা খাটের নিচে।
The chair is next to the table. | চেয়ারটা টেবিলের পাশে।
The window is behind the desk. | জানালাটা ডেস্কের পেছনে।
The door is in front of me. | দরজাটা আমার সামনে।
Open the door, please. | দয়া করে দরজা খোলো।
Close the window. | জানালা বন্ধ করো।
Turn on the light. | বাতি জ্বালাও।
Turn off the fan. | ফ্যান বন্ধ করো।
Where is my biology book? | আমার জীববিজ্ঞান বইটা কোথায়?
It is between the two notebooks. | ওটা দুইটি খাতার মাঝখানে।
Is there a fan in your room? | তোমার ঘরে কি ফ্যান আছে?
Yes, there is. | হ্যাঁ, আছে।
A tidy room helps me study well. | গোছানো ঘর আমাকে ভালো পড়তে সাহায্য করে।
This small room holds my big dreams. | এই ছোট ঘরে আমার বড় স্বপ্ন থাকে।
""",
dict(title="জায়গা বোঝাতে: in, on, under, next to",
     points=["<b>in</b> — ভিতরে: in the room", "<b>on</b> — ওপরে (ছুঁয়ে): on the table", "<b>under</b> — নিচে: under the bed", "<b>next to / between / behind</b> — পাশে / মাঝখানে / পেছনে"],
     table=[("on", "ওপরে", "The book is on the table."), ("under", "নিচে", "The ball is under the bed."), ("between", "মাঝখানে", "It is between two books.")],
     quiz=("The football is ___ the bed. (নিচে)", ["on", "under", "in"], 1, "নিচে = under।")))

# ======================================================================= Day 16
day(16, "Last Weekend", "গত সপ্তাহান্ত", "আজ যা শেষ হয়ে গেছে তা বলতে শিখব — অতীত কাল।",
"""
Last Friday, I woke up early. | গত শুক্রবার আমি তাড়াতাড়ি উঠেছিলাম।
I helped my mother in the kitchen. | আমি রান্নাঘরে মাকে সাহায্য করেছিলাম।
Then I studied biology for three hours. | তারপর আমি তিন ঘণ্টা জীববিজ্ঞান পড়েছিলাম।
In the afternoon, I went to my parents' chamber. | বিকেলে আমি বাবা-মায়ের চেম্বারে গিয়েছিলাম।
A little girl came with a fever. | একটি ছোট মেয়ে জ্বর নিয়ে এসেছিল।
After the treatment, she left with a big smile. | চিকিৎসার পরে সে বড় হাসি নিয়ে ফিরে গেল।
I felt very happy to see that smile. | সেই হাসি দেখে আমার খুব ভালো লাগল।
In the evening, I played with Raj. | সন্ধ্যায় আমি রাজের সাথে খেলেছিলাম।
""",
"""
last | লাস্ট | গত, শেষ
weekend | উইকএন্ড | সপ্তাহান্ত
went | ওয়েন্ট | গেল (go-র অতীত)
came | কেইম | এল (come-এর অতীত)
saw | সো | দেখল (see-র অতীত)
gave | গেইভ | দিল (give-এর অতীত)
took | টুক | নিল (take-এর অতীত)
ate | এইট | খেল (eat-এর অতীত)
played | প্লেড | খেলল
helped | হেল্পট | সাহায্য করল
""",
"""
What did you do last weekend? | গত সপ্তাহান্তে আপনি কী করেছিলেন?
I woke up early. | আমি তাড়াতাড়ি উঠেছিলাম।
I helped my mother. | আমি মাকে সাহায্য করেছিলাম।
I studied for three hours. | আমি তিন ঘণ্টা পড়েছিলাম।
I went to my parents' chamber. | আমি বাবা-মায়ের চেম্বারে গিয়েছিলাম।
A little girl came with a fever. | একটি ছোট মেয়ে জ্বর নিয়ে এসেছিল।
The homeopathic doctor gave her medicine. | হোমিওপ্যাথিক ডাক্তার তাকে ওষুধ দিলেন।
She took the medicine on time. | সে সময়মতো ওষুধ খেল।
I saw her smile. | আমি তার হাসি দেখলাম।
We ate lunch together. | আমরা একসাথে দুপুরের খাবার খেলাম।
I played with Raj in the evening. | আমি সন্ধ্যায় রাজের সাথে খেলেছিলাম।
We watched a movie. | আমরা একটি সিনেমা দেখলাম।
I didn't go out. | আমি বাইরে যাইনি।
She didn't call me. | সে আমাকে ফোন করেনি।
Did you sleep well? | আপনি কি ভালো ঘুমিয়েছিলেন?
Yes, I did. | হ্যাঁ, ঘুমিয়েছিলাম।
No, I didn't. | না, ঘুমাইনি।
It rained all day. | সারাদিন বৃষ্টি হয়েছিল।
I felt very happy. | আমার খুব ভালো লেগেছিল।
It was a wonderful weekend. | সপ্তাহান্তটা চমৎকার ছিল।
""",
dict(title="Past Simple — অতীত কাল",
     points=["সাধারণ নিয়ম: verb + <b>-ed</b> — played, helped, studied", "অনিয়মিত (মুখস্থ): go → <b>went</b>, see → <b>saw</b>, eat → <b>ate</b>, give → <b>gave</b>", "না/প্রশ্ন: <b>did / didn't + verb-এর আসল রূপ</b> — I didn't go. · Did you sleep?"],
     table=[("play", "played", "খেলেছিলাম"), ("go", "went", "গিয়েছিলাম"), ("didn't", "+ go", "যাইনি")],
     quiz=("Last Friday I ___ to the chamber.", ["go", "went", "going"], 1, "গত শুক্রবার = অতীত; go-র অতীত went।")))

# ======================================================================= Day 17
day(17, "My Homeopathic Medical College", "আমার হোমিওপ্যাথিক মেডিকেল কলেজ", "আজ কলেজে প্রথম দিন — ক্লাস, শিক্ষক আর ঠিকানা জিজ্ঞাসা শিখব।",
"""
Today is Oishi's first day at the homeopathic medical college. | আজ ঐশীর হোমিওপ্যাথিক মেডিকেল কলেজে প্রথম দিন।
She is excited and a little nervous. | সে উত্তেজিত আর একটু নার্ভাস।
She asks, "Excuse me, where is the lecture hall?" | সে জিজ্ঞেস করে, "মাফ করবেন, লেকচার হল কোথায়?"
"Go straight, then turn left," says a classmate. | "সোজা যাও, তারপর বাঁয়ে ঘোরো," বলে এক সহপাঠী।
The anatomy teacher shows a skeleton. | অ্যানাটমির শিক্ষক একটি কঙ্কাল দেখান।
"An adult has two hundred and six bones," he says. | "একজন প্রাপ্তবয়স্কের দুইশো ছয়টি হাড় থাকে," তিনি বলেন।
"A good homeopathic doctor changes lives," says the principal. | "ভালো হোমিওপ্যাথিক ডাক্তার জীবন বদলে দেন," বলেন অধ্যক্ষ।
Oishi takes notes carefully and smiles. | ঐশী যত্ন করে নোট নেয় আর হাসে।
""",
"""
medical | মেডিকেল | চিকিৎসা-সংক্রান্ত
anatomy | অ্যানাটমি | শারীরবিদ্যা (দেহের গঠন)
skeleton | স্কেলিটন | কঙ্কাল
lecture | লেকচার | লেকচার, বক্তৃতা
library | লাইব্রেরি | গ্রন্থাগার
notes | নোটস | নোট
admission | অ্যাডমিশন | ভর্তি
excited | এক্সাইটেড | উত্তেজিত
campus | ক্যাম্পাস | ক্যাম্পাস
classmate | ক্লাসমেইট | সহপাঠী
""",
"""
This is my medical college. | এটা আমার মেডিকেল কলেজ।
I got admission here. | আমি এখানে ভর্তি হয়েছি।
Today is my first day. | আজ আমার প্রথম দিন।
I am excited. | আমি উত্তেজিত।
Excuse me, where is the lecture hall? | মাফ করবেন, লেকচার হল কোথায়?
Go straight. | সোজা যান।
Turn left. | বাঁয়ে ঘুরুন।
Turn right. | ডানে ঘুরুন।
It is near the library. | ওটা লাইব্রেরির কাছে।
It is on the second floor. | ওটা দোতলায়।
This is my classmate. | ইনি আমার সহপাঠী।
The anatomy teacher shows a skeleton. | অ্যানাটমির শিক্ষক একটি কঙ্কাল দেখান।
An adult has two hundred and six bones. | একজন প্রাপ্তবয়স্কের দুইশো ছয়টি হাড় থাকে।
Please take notes carefully. | দয়া করে যত্ন করে নোট নাও।
I like the lectures. | আমার লেকচারগুলো ভালো লাগে।
The campus is green and quiet. | ক্যাম্পাসটা সবুজ আর শান্ত।
Study hard and be curious. | কঠোর পরিশ্রম করো আর কৌতূহলী থাকো।
A good homeopathic doctor changes many lives. | ভালো হোমিওপ্যাথিক ডাক্তার অনেকের জীবন বদলে দেন।
Patients thank the homeopathic doctor with all their heart. | রোগীরা হোমিওপ্যাথিক ডাক্তারকে মন থেকে ধন্যবাদ দেন।
This is the best first day! | এটা সেরা প্রথম দিন!
""",
dict(title="ঠিকানা জিজ্ঞাসা ও নির্দেশ",
     points=["জিজ্ঞাসা: <b>Excuse me, where is …?</b>", "নির্দেশ: <b>Go straight</b> (সোজা), <b>Turn left</b> (বাঁয়ে), <b>Turn right</b> (ডানে)", "জায়গা: <b>near</b> (কাছে), <b>on the second floor</b> (দোতলায়)"],
     table=[("Go", "straight", "সোজা যান"), ("Turn", "left", "বাঁয়ে ঘুরুন"), ("It is", "near the library", "লাইব্রেরির কাছে")],
     quiz=("___ left, then go straight. (বাঁয়ে ঘুরুন)", ["Turn", "Stop", "Sit"], 0, "দিক বদলাতে Turn left।")))

# ======================================================================= Day 18
day(18, "Amazing Science Facts", "বিজ্ঞানের অবাক করা তথ্য", "আজ তুলনা করতে শিখব — বড়, ছোট, দ্রুত, সবচেয়ে বড়।",
"""
Oishi loves surprising science facts. | ঐশী বিজ্ঞানের অবাক করা তথ্য ভালোবাসে।
The skin is the largest organ of the body. | ত্বক শরীরের সবচেয়ে বড় অঙ্গ।
Light is faster than sound. | আলো শব্দের চেয়ে দ্রুত।
The blue whale is the biggest animal in the world. | নীল তিমি পৃথিবীর সবচেয়ে বড় প্রাণী।
A cheetah is faster than a horse. | চিতা ঘোড়ার চেয়ে দ্রুত দৌড়ায়।
The brain is the most important organ for thinking. | চিন্তার জন্য মস্তিষ্কই সবচেয়ে গুরুত্বপূর্ণ অঙ্গ।
A homeopathic doctor's work is more valuable than gold. | হোমিওপ্যাথিক ডাক্তারের কাজ সোনার চেয়েও মূল্যবান।
"Science is more interesting than I thought!" | "বিজ্ঞান আমার ভাবনার চেয়েও মজার!"
""",
"""
large | লার্জ | বড়, বিশাল
fast | ফাস্ট | দ্রুত
slow | স্লো | ধীর
heavy | হেভি | ভারী
tiny | টাইনি | খুব ছোট
strong | স্ট্রং | শক্তিশালী
important | ইমপর্ট্যান্ট | গুরুত্বপূর্ণ
simple | সিম্পল | সহজ, সরল
famous | ফেইমাস | বিখ্যাত
deep | ডিপ | গভীর
""",
"""
The elephant is bigger than the cow. | হাতি গরুর চেয়ে বড়।
The cheetah is faster than the horse. | চিতা ঘোড়ার চেয়ে দ্রুত।
The turtle is slower than the rabbit. | কচ্ছপ খরগোশের চেয়ে ধীর।
The blue whale is the biggest animal. | নীল তিমি সবচেয়ে বড় প্রাণী।
The skin is the largest organ of the body. | ত্বক শরীরের সবচেয়ে বড় অঙ্গ।
Light is faster than sound. | আলো শব্দের চেয়ে দ্রুত।
An ant is tiny. | পিঁপড়া খুব ছোট।
Iron is heavier than wood. | লোহা কাঠের চেয়ে ভারী।
The brain is very important. | মস্তিষ্ক খুব গুরুত্বপূর্ণ।
The Padma is a deep river. | পদ্মা একটি গভীর নদী।
Which is bigger, the heart or the brain? | কোনটা বড়, হৃৎপিণ্ড না মস্তিষ্ক?
The brain is bigger than the heart. | মস্তিষ্ক হৃৎপিণ্ডের চেয়ে বড়।
Biology is more interesting than I thought. | জীববিজ্ঞান আমার ভাবনার চেয়েও মজার।
English is easier than I thought. | ইংরেজি আমার ভাবনার চেয়েও সহজ।
Tea is cheaper than medicine. | চা ওষুধের চেয়ে সস্তা।
Health is the most precious thing. | স্বাস্থ্যই সবচেয়ে মূল্যবান জিনিস।
A homeopathic doctor protects this precious thing. | হোমিওপ্যাথিক ডাক্তার এই মূল্যবান জিনিসটি রক্ষা করেন।
This is the best day of my life. | এটা আমার জীবনের সেরা দিন।
She is the cleverest girl in the class. | সে ক্লাসের সবচেয়ে বুদ্ধিমান মেয়ে।
Learn something new every day. | রোজ নতুন কিছু শেখো।
""",
dict(title="তুলনা: -er than, the -est",
     points=["ছোট শব্দে: <b>-er than</b> — fast → <b>faster than</b>", "ছোট শব্দে সেরা: <b>the -est</b> — the fastest, the biggest", "লম্বা শব্দে: <b>more … than</b>, <b>the most …</b> — more interesting, the most important", "অনিয়মিত: good → better → <b>the best</b>"],
     table=[("big", "bigger / the biggest", "বড় — আরও বড় — সবচেয়ে বড়"), ("interesting", "more / the most interesting", "মজার — আরও মজার — সবচেয়ে মজার"), ("good", "better / the best", "ভালো — আরও ভালো — সেরা")],
     quiz=("Light is ___ than sound.", ["fast", "faster", "the fastest"], 1, "দুটোর তুলনায় -er than: faster than।")))

# ======================================================================= Day 19
day(19, "Giving Advice", "পরামর্শ দেওয়া", "আজ কারণ, ফল আর বিপরীত কথা জুড়তে শিখব — আর সুন্দর করে পরামর্শ দিতে।",
"""
A neighbour comes to Oishi's home. | এক প্রতিবেশী ঐশীর বাড়িতে আসেন।
"I sleep late, so I feel weak," she says. | "আমি দেরিতে ঘুমাই, তাই দুর্বল লাগে," তিনি বলেন।
Oishi says, "You should sleep early because the body needs rest." | ঐশী বলে, "আপনার তাড়াতাড়ি ঘুমানো উচিত, কারণ শরীরের বিশ্রাম দরকার।"
"Drink clean water, but don't skip meals." | "পরিষ্কার পানি খান, কিন্তু খাবার বাদ দেবেন না।"
"I am not a homeopathic doctor, so please meet my father." | "আমি হোমিওপ্যাথিক ডাক্তার নই, তাই দয়া করে আমার বাবার সাথে দেখা করুন।"
The neighbour smiles and says, "You explain so well!" | প্রতিবেশী হেসে বলেন, "তুমি কী সুন্দর বুঝিয়ে বলো!"
People trust a homeopathic doctor because he listens with care. | মানুষ হোমিওপ্যাথিক ডাক্তারকে বিশ্বাস করে কারণ তিনি যত্ন নিয়ে শোনেন।
Oishi feels proud to help someone. | কাউকে সাহায্য করতে পেরে ঐশী গর্ব অনুভব করে।
""",
"""
neighbour | নেইবার | প্রতিবেশী
enough | ইনাফ | যথেষ্ট
skip | স্কিপ | বাদ দেওয়া
meal | মিল | খাবার (এক বেলার)
exercise | এক্সারসাইজ | ব্যায়াম
walk | ওয়াক | হাঁটা
habit | হ্যাবিট | অভ্যাস
safe | সেইফ | নিরাপদ
regular | রেগুলার | নিয়মিত
trust | ট্রাস্ট | বিশ্বাস
""",
"""
I sleep late, so I feel weak. | আমি দেরিতে ঘুমাই, তাই দুর্বল লাগে।
You should sleep early. | আপনার তাড়াতাড়ি ঘুমানো উচিত।
The body needs rest because it works all day. | শরীরের বিশ্রাম দরকার কারণ এটা সারাদিন কাজ করে।
You must drink enough water. | আপনাকে যথেষ্ট পানি খেতে হবে।
You mustn't skip meals. | আপনি খাবার বাদ দিতে পারবেন না।
Walk for thirty minutes every day. | রোজ ত্রিশ মিনিট হাঁটুন।
Exercise is a good habit. | ব্যায়াম একটি ভালো অভ্যাস।
It is cheap, but it is very useful. | এটা সস্তা, কিন্তু খুব কাজের।
I am tired, so I will rest. | আমি ক্লান্ত, তাই বিশ্রাম নেব।
I like sweets, but I eat them rarely. | আমি মিষ্টি পছন্দ করি, কিন্তু কম খাই।
Please meet my father. | দয়া করে আমার বাবার সাথে দেখা করুন।
He is a homeopathic doctor. | তিনি একজন হোমিওপ্যাথিক ডাক্তার।
He listens carefully because he cares. | তিনি মন দিয়ে শোনেন কারণ তিনি যত্ন নেন।
People trust a homeopathic doctor. | মানুষ হোমিওপ্যাথিক ডাক্তারকে বিশ্বাস করে।
It is safe to ask for advice. | পরামর্শ চাওয়া নিরাপদ।
Regular habits keep us healthy. | নিয়মিত অভ্যাস আমাদের সুস্থ রাখে।
Thank you for your advice. | আপনার পরামর্শের জন্য ধন্যবাদ।
You explain so well! | আপনি কী সুন্দর বুঝিয়ে বলেন!
I feel proud to help someone. | কাউকে সাহায্য করতে পেরে আমি গর্ব অনুভব করি।
Helping others gives real happiness. | অন্যকে সাহায্য করলে সত্যিকারের সুখ পাওয়া যায়।
""",
dict(title="because / so / but — কারণ, ফল, বিপরীত",
     points=["<b>because</b> — কারণ বলে: I rest <b>because</b> I am tired.", "<b>so</b> — ফল বলে: I am tired, <b>so</b> I will rest.", "<b>but</b> — বিপরীত বলে: It is cheap, <b>but</b> it is useful."],
     table=[("because", "কারণ", "I stayed home because it rained."), ("so", "তাই", "It rained, so I stayed home."), ("but", "কিন্তু", "I like tea, but I prefer milk.")],
     quiz=("I am tired, ___ I will rest.", ["because", "so", "but"], 1, "ক্লান্ত → তাই বিশ্রাম: ফল বোঝাতে so।")))

# ======================================================================= Day 20
day(20, "My Dream Morning", "আমার স্বপ্নের সকাল", "আজ কল্পনা করব ভবিষ্যতের একটি সকাল — আর আগামী দিনের কথা বলতে শিখব।",
"""
Imagine a morning ten years from now. | কল্পনা করো দশ বছর পরের একটি সকাল।
A beautiful chamber has a board with a name on it. | সুন্দর একটি চেম্বারের সাইনবোর্ডে একটি নাম লেখা।
The name is "Homeopathic Doctor Oishi Debnath." | নামটি "হোমিওপ্যাথিক ডাক্তার ঐশী দেবনাথ।"
Many patients wait there with hope. | অনেক রোগী আশা নিয়ে সেখানে অপেক্ষা করেন।
Oishi listens to them and helps them. | ঐশী তাদের কথা শোনে আর সাহায্য করে।
They smile and say, "Thank you so much!" | তারা হেসে বলে, "অনেক ধন্যবাদ!"
Her family is proud, and she has respect, a good income and a happy life. | তার পরিবার গর্বিত, আর সে সম্মান, ভালো আয় আর সুখী জীবন পেয়েছে।
It is only a dream today, but dreams begin today. | আজ এটা শুধু স্বপ্ন, কিন্তু স্বপ্ন আজ থেকেই শুরু হয়।
""",
"""
dream | ড্রিম | স্বপ্ন
goal | গোল | লক্ষ্য
future | ফিউচার | ভবিষ্যৎ
imagine | ইম্যাজিন | কল্পনা করা
success | সাকসেস | সাফল্য
respect | রিস্পেক্ট | সম্মান
income | ইনকাম | আয়
proud | প্রাউড | গর্বিত
confident | কনফিডেন্ট | আত্মবিশ্বাসী
hope | হোপ | আশা
""",
"""
Imagine your future. | তোমার ভবিষ্যৎ কল্পনা করো।
What is your dream? | তোমার স্বপ্ন কী?
My dream is bright. | আমার স্বপ্ন উজ্জ্বল।
I will study hard. | আমি কঠোর পরিশ্রম করে পড়ব।
I am going to study biology tonight. | আমি আজ রাতে জীববিজ্ঞান পড়ব।
I will pass the HSC exam with good marks. | আমি ভালো নম্বর নিয়ে এইচএসসি পাস করব।
I will learn from my teachers. | আমি আমার শিক্ষকদের কাছ থেকে শিখব।
A homeopathic doctor helps many people. | হোমিওপ্যাথিক ডাক্তার অনেক মানুষকে সাহায্য করেন।
A homeopathic doctor has respect in society. | হোমিওপ্যাথিক ডাক্তারের সমাজে সম্মান আছে।
A homeopathic doctor earns a good income. | হোমিওপ্যাথিক ডাক্তার ভালো আয় করেন।
A homeopathic doctor can live a comfortable life. | হোমিওপ্যাথিক ডাক্তার আরামদায়ক জীবন কাটাতে পারেন।
Patients say thank you with a smile. | রোগীরা হেসে ধন্যবাদ বলেন।
My family will be proud. | আমার পরিবার গর্বিত হবে।
I am confident. | আমি আত্মবিশ্বাসী।
Success needs practice and hope. | সাফল্যের জন্য অনুশীলন আর আশা দরকার।
Every big goal starts with a small step. | প্রতিটি বড় লক্ষ্য একটি ছোট পদক্ষেপ দিয়ে শুরু হয়।
Today is the first step. | আজ প্রথম পদক্ষেপ।
Thank you for teaching me. | আমাকে শেখানোর জন্য ধন্যবাদ।
I will never stop learning. | আমি কখনো শেখা থামাব না।
See you in English 102! | English 102-তে দেখা হবে!
""",
dict(title="ভবিষ্যৎ: will ও going to",
     points=["<b>will + verb</b> — সিদ্ধান্ত/আশা: I <b>will study</b> hard.", "<b>am / is / are going to + verb</b> — ঠিক করা পরিকল্পনা: I <b>am going to study</b> tonight.", "না: I <b>won't</b> give up. · প্রশ্ন: <b>Will you</b> help me?"],
     table=[("I", "will study", "আমি পড়ব"), ("I", "am going to read", "আমি পড়তে যাচ্ছি"), ("I", "won't give up", "আমি হাল ছাড়ব না")],
     quiz=("I ___ study hard for my dream.", ["will", "did", "am"], 0, "ভবিষ্যতের কথায় will + verb।")))

assert len(DAYS) == 20
for d in DAYS:
    assert len(d["story"]) == 8, (d["n"], "story", len(d["story"]))
    assert len(d["words"]) == 10, (d["n"], "words", len(d["words"]))
    assert len(d["sentences"]) == 20, (d["n"], "sentences", len(d["sentences"]))
# every taught word is new: no word repeats across the whole course
_seen = {}
for d in DAYS:
    for w, _, _ in d["words"]:
        k = w.lower()
        assert k not in _seen, f"word '{w}' on day {d['n']} was already taught on day {_seen[k]}"
        _seen[k] = d["n"]
# content rule: a bare "doctor" (not preceded by "homeopathic") is never used
import re as _re
for d in DAYS:
    for en, _ in d["story"] + d["sentences"]:
        assert not _re.search(r"(?<!homeopathic )\bdoctor\b", en, _re.I) or "homeopathic doctor" in en.lower(), (d["n"], en)
