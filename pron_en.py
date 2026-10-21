"""Bangla pronunciation for every English word used in the English 101 stories and sentences.
build_line() joins them so each line can show 'English / উচ্চারণ / বাংলা'. Validated at import time."""
import re

_RAW = """
a=আ about=অ্যাবাউট add=অ্যাড afraid=অ্যাফ্রেইড after=আফটার afternoon=আফটারনুন again=অ্যাগেন ago=অ্যাগো agree=অ্যাগ্রি all=অল allergy=অ্যালার্জি aloud=অ্যালাউড also=অলসো am=অ্যাম an=অ্যান and=অ্যান্ড angry=অ্যাংগ্রি answer=আন্সার answers=আন্সার্স any=এনি are=আর arrive=অ্যারাইভ as=অ্যাজ ask=আস্ক asks=আস্ক্স at=অ্যাট ate=এইট
bad=ব্যাড bag=ব্যাগ bananas=বানানাজ bangladesh=বাংলাদেশ bazar=বাজার be=বি beach=বিচ beautiful=বিউটিফুল because=বিকজ becomes=বিকামস bed=বেড before=বিফোর best=বেস্ট better=বেটার big=বিগ bigger=বিগার bill=বিল bird=বার্ড birthday=বার্থডে black=ব্ল্যাক blue=ব্লু boil=বয়েল book=বুক booking=বুকিং books=বুকস bought=বট boy=বয় bread=ব্রেড breakfast=ব্রেকফাস্ট bright=ব্রাইট brother=ব্রাদার brown=ব্রাউন brush=ব্রাশ bus=বাস busy=বিজি but=বাট buy=বাই by=বাই
cake=কেইক call=কল calm=কাম calmer=কামার came=কেইম can=ক্যান can't=ক্যান্ট card=কার্ড careful=কেয়ারফুল ceiling=সিলিং chair=চেয়ার change=চেঞ্জ cheap=চিপ cheaper=চিপার checks=চেক্স chicken=চিকেন city=সিটি class=ক্লাস clean=ক্লিন cleaner=ক্লিনার close=ক্লোজ cloudy=ক্লাউডি coffee=কফি cold=কোল্ড colour=কালার come=কাম comes=কামস comfortable=কমফর্টেবল coming=কামিং confidence=কনফিডেন্স confident=কনফিডেন্ট cook=কুক cooks=কুক্স cool=কুল costs=কস্টস could=কুড counter=কাউন্টার cox's=কক্স cricket=ক্রিকেট crowded=ক্রাউডেড cup=কাপ cups=কাপস curry=কারি cut=কাট cuts=কাটস
dal=ডাল dark=ডার্ক date=ডেইট daughter=ডটার day=ডে days=ডেজ delicious=ডেলিশাস dev=দেব dhaka=ঢাকা dhanmondi=ধানমন্ডি did=ডিড didn't=ডিডন্ট dinner=ডিনার discount=ডিসকাউন্ট do=ডু doctor=ডক্টর does=ডাজ don't=ডোন্ট door=ডোর down=ডাউন dream=ড্রিম drink=ড্রিংক drinks=ড্রিংকস
early=আর্লি easier=ইজিয়ার eat=ইট egg=এগ eggs=এগস eid=ঈদ eight=এইট eighty=এইটি english=ইংলিশ evening=ঈভনিং every=এভরি everything=এভরিথিং exam=এগজাম excited=এক্সাইটেড exciting=এক্সাইটিং excuse=এক্সকিউজ expensive=এক্সপেনসিভ eyes=আইজ
face=ফেইস family=ফ্যামিলি famous=ফেইমাস fan=ফ্যান far=ফার father=ফাদার favourite=ফেভারিট feel=ফিল feels=ফিলস fever=ফিভার fifth=ফিফথ fifty=ফিফটি finally=ফাইনালি fine=ফাইন finish=ফিনিশ first=ফার্স্ট fish=ফিশ fits=ফিটস fitting=ফিটিং five=ফাইভ flat=ফ্ল্যাট food=ফুড football=ফুটবল for=ফর forget=ফরগেট forty=ফোর্টি four=ফোর free=ফ্রি fresh=ফ্রেশ friday=ফ্রাইডে friend=ফ্রেন্ড friends=ফ্রেন্ডস fries=ফ্রাইজ from=ফ্রম fruits=ফ্রুটস fry=ফ্রাই future=ফিউচার
gave=গেইভ get=গেট gift=গিফট give=গিভ gives=গিভস glass=গ্লাস go=গো goal=গোল goes=গোজ going=গোয়িং good=গুড grandfather=গ্র্যান্ডফাদার grandmother=গ্র্যান্ডমাদার grandmother's=গ্র্যান্ডমাদারস great=গ্রেইট
had=হ্যাড half=হাফ hand=হ্যান্ড happy=হ্যাপি hard=হার্ড has=হ্যাজ have=হ্যাভ he=হি headache=হেডেক health=হেলথ healthy=হেলদি hear=হিয়ার heat=হিট hello=হ্যালো her=হার here=হিয়ার hi=হাই him=হিম his=হিজ holiday=হলিডে home=হোম homework=হোমওয়ার্ক hospital=হসপিটাল hot=হট hotel=হোটেল hour=আওয়ার house=হাউস how=হাউ hundred=হান্ড্রেড hungry=হাংগ্রি hurry=হারি hurting=হার্টিং hurts=হার্টস
i=আই idea=আইডিয়া important=ইমপর্ট্যান্ট improving=ইমপ্রুভিং in=ইন instead=ইনস্টেড into=ইনটু introduce=ইনট্রোডিউস is=ইজ it=ইট it's=ইটস
job=জব journey=জার্নি
khichuri=খিচুড়ি kilo=কিলো kilos=কিলোজ kind=কাইন্ড kindest=কাইন্ডেস্ট kitchen=কিচেন know=নো knows=নোজ
last=লাস্ট late=লেইট later=লেইটার learn=লার্ন learned=লার্নড learning=লার্নিং leave=লিভ leaves=লিভস left=লেফট let's=লেটস library=লাইব্রেরি life=লাইফ light=লাইট like=লাইক little=লিটল live=লিভ lives=লিভস long=লং longest=লংগেস্ট look=লুক lot=লট love=লাভ lovely=লাভলি luck=লাক luggage=লাগেজ lunch=লাঞ্চ
makes=মেইকস man=ম্যান mango=ম্যাংগো mangoes=ম্যাংগোজ many=মেনি march=মার্চ market=মার্কেট may=মে me=মি mean=মিন medicine=মেডিসিন medium=মিডিয়াম meet=মিট message=মেসেজ met=মেট milk=মিল্ক mine=মাইন minutes=মিনিটস mirpur=মিরপুর mom=মম moment=মোমেন্ট money=মানি months=মান্থস more=মোর morning=মর্নিং most=মোস্ট mother=মাদার mouth=মাউথ movie=মুভি much=মাচ must=মাস্ট my=মাই myself=মাইসেলফ
name=নেইম near=নিয়ার nearest=নিয়ারেস্ট need=নিড needs=নিডস network=নেটওয়ার্ক never=নেভার new=নিউ newer=নিউয়ার next=নেক্সট nice=নাইস night=নাইট nine=নাইন no=নো not=নট notebook=নোটবুক notes=নোটস now=নাউ number=নাম্বার nusrat=নুসরাত
o'clock=ও-ক্লক october=অক্টোবর of=অব off=অফ office=অফিস oil=অয়েল oily=অয়েলি okay=ওকে old=ওল্ড older=ওল্ডার on=অন one=ওয়ান onion=অনিয়ন onions=অনিয়নস only=ওনলি open=ওপেন opinion=ওপিনিয়ন or=অর our=আওয়ার out=আউট over=ওভার
page=পেইজ pain=পেইন pan=প্যান paratha=পরোটা park=পার্ক passed=পাস্ড past=পাস্ট patience=পেশেন্স pay=পে pays=পেজ people=পিপল per=পার person=পার্সন phone=ফোন photos=ফটোজ pieces=পিসেজ place=প্লেইস plan=প্ল্যান plans=প্ল্যান্স platform=প্ল্যাটফর্ম play=প্লে played=প্লেড please=প্লিজ pond=পন্ড practice=প্র্যাকটিস prefer=প্রিফার progress=প্রোগ্রেস proud=প্রাউড
question=কোয়েশ্চেন quiet=কোয়াইট quieter=কোয়াইটার
rahim=রহিম rain=রেইন rained=রেইন্ড raining=রেইনিং raises=রেইজেস reach=রিচ read=রিড reads=রিডস ready=রেডি receipt=রিসিট recipe=রেসিপি recommend=রেকমেন্ড repeat=রিপিট rest=রেস্ট restaurant=রেস্টুরেন্ট result=রেজাল্ট returns=রিটার্নস rice=রাইস richest=রিচেস্ট rickshaw=রিকশা right=রাইট rings=রিংস river=রিভার road=রোড room=রুম rooms=রুমস
sad=স্যাড safe=সেইফ salt=সল্ট sanjoy=সঞ্জয় sanjoy's=সঞ্জয়স saturday=স্যাটারডে saw=সো say=সে says=সেজ sea=সি second=সেকেন্ড see=সি send=সেন্ড seven=সেভেন seventy=সেভেন্টি shall=শ্যাল she=শি shirt=শার্ট shoes=শুজ shop=শপ shopkeeper=শপকিপার shopping=শপিং should=শুড shouldn't=শুডন্ট shower=শাওয়ার shuvo=শুভ simple=সিম্পল sister=সিস্টার sisters=সিস্টার্স sit=সিট six=সিক্স size=সাইজ sky=স্কাই sleep=স্লিপ sleeps=স্লিপস slowly=স্লোলি small=স্মল so=সো some=সাম son=সান soon=সুন sorry=সরি speak=স্পিক speaking=স্পিকিং spices=স্পাইসেস spicy=স্পাইসি start=স্টার্ট starts=স্টার্টস station=স্টেশন stay=স্টে stir=স্টির stomach=স্টমাক stop=স্টপ story=স্টোরি stove=স্টোভ straight=স্ট্রেইট strong=স্ট্রং strongest=স্ট্রংগেস্ট stuck=স্টাক student=স্টুডেন্ট studied=স্টাডিড studies=স্টাডিজ study=স্টাডি studying=স্টাডিইং subject=সাবজেক্ট success=সাকসেস sugar=সুগার summer=সামার sun=সান sunday=সানডে surprised=সারপ্রাইজড sweet=সুইট swim=সুইম
table=টেবিল taka=টাকা take=টেইক takes=টেইকস talk=টক tall=টল taller=টলার taste=টেইস্ট tastes=টেইস্টস tea=টি teacher=টিচার teaches=টিচেজ teaching=টিচিং teeth=টিথ ten=টেন test=টেস্ট than=দ্যান thank=থ্যাংক that=দ্যাট the=দ্য their=দেয়ার then=দেন there=দেয়ার these=দিজ they=দে think=থিংক third=থার্ড thirty=থার্টি this=দিস those=দোজ thought=থট thousand=থাউজেন্ড three=থ্রি throat=থ্রোট thursday=থার্সডে ticket=টিকেট tickets=টিকেটস time=টাইম tired=টায়ার্ড to=টু today=টুডে today's=টুডেজ together=টুগেদার tomorrow=টুমরো too=টু took=টুক town=টাউন traffic=ট্রাফিক train=ট্রেইন travel=ট্র্যাভেল tries=ট্রাইজ trip=ট্রিপ trousers=ট্রাউজারস try=ট্রাই turn=টার্ন twelve=টুয়েলভ twenty=টুয়েন্টি twice=টোয়াইস two=টু
umbrella=আমব্রেলা under=আন্ডার understand=আন্ডারস্ট্যান্ড university=ইউনিভার্সিটি until=আনটিল up=আপ
vegetables=ভেজিটেবলস very=ভেরি view=ভিউ village=ভিলেজ visit=ভিজিট visited=ভিজিটেড
wait=ওয়েট waiter=ওয়েটার wake=ওয়েইক wakes=ওয়েইকস walk=ওয়াক want=ওয়ান্ট wants=ওয়ান্টস was=ওয়াজ wash=ওয়াশ watched=ওয়াচ্ড water=ওয়াটার waves=ওয়েইভস way=ওয়ে we=উই wear=ওয়্যার weather=ওয়েদার week=উইক weekend=উইকএন্ড weeks=উইকস welcome=ওয়েলকাম well=ওয়েল went=ওয়েন্ট were=ওয়ার what=হোয়াট when=হোয়েন where=হোয়্যার which=হুইচ who=হু why=হোয়াই will=উইল wind=উইন্ড window=উইন্ডো winter=উইন্টার with=উইথ woke=ওয়োক won't=ওন্ট wonderful=ওয়ান্ডারফুল words=ওয়ার্ডস work=ওয়ার্ক worked=ওয়ার্কড world=ওয়ার্ল্ড worry=ওয়ারি would=উড write=রাইট writes=রাইটস
year=ইয়ার yes=ইয়েস yesterday=ইয়েস্টারডে you=ইউ young=ইয়াং youngest=ইয়াংগেস্ট your=ইয়োর yourself=ইয়োরসেলফ
business=বিজনেস businessman=বিজনেসম্যান care=কেয়ার homemaker=হোমমেইকার poddar=পোদ্দার rajib=রাজীব sukumar=সুকুমার nupur=নুপুর works=ওয়ার্ক্স younger=ইয়াংগার
 graduate=গ্র্যাজুয়েট
 hajiganj=হাজীগঞ্জ chandpur=চাঁদপুর
 corner=কর্নার biggest=বিগেস্ট customers=কাস্টমার্স
 back=ব্যাক
 box=বক্স help=হেল্প sold=সোল্ড

admission=অ্যাডমিশন adult=অ্যাডাল্ট advice=অ্যাডভাইস air=এয়ার alive=অ্যালাইভ almost=অলমোস্ট always=অলওয়েজ anatomy=অ্যানাটমি animal=অ্যানিমাল animals=অ্যানিমালস ant=অ্যান্ট aunt=আন্ট away=অ্যাওয়ে
balanced=ব্যালান্সড banana=বানানা bangla=বাংলা beating=বিটিং beats=বিটস begin=বিগিন behind=বিহাইন্ড between=বিটুইন bimol=বিমল biology=বায়োলজি birds=বার্ডস bites=বাইটস bitter=বিটার blood=ব্লাড board=বোর্ড body=বডি bones=বোনস bottle=বটল brain=ব্রেইন breathe=ব্রিদ bring=ব্রিং
called=কল্ড calls=কলস campus=ক্যাম্পাস carefully=কেয়ারফুলি cares=কেয়ার্স carries=ক্যারিজ cell=সেল cells=সেলস chairs=চেয়ার্স chamber=চেম্বার changes=চেঞ্জেস chapters=চ্যাপ্টার্স chart=চার্ট cheetah=চিতা chemistry=কেমিস্ট্রি child=চাইল্ড children=চিলড্রেন chooses=চুজেস classmate=ক্লাসমেইট cleans=ক্লিনস clever=ক্লেভার cleverest=ক্লেভারেস্ট college=কলেজ controls=কন্ট্রোলস cough=কফ course=কোর্স cousin=কাজিন cow=কাউ curious=কিউরিয়াস
daily=ডেইলি debnath=দেবনাথ deep=ডিপ dengue=ডেঙ্গু desk=ডেস্ক diagram=ডায়াগ্রাম diagrams=ডায়াগ্রামস didi=দিদি diet=ডায়েট different=ডিফারেন্ট difficult=ডিফিকাল্ট digests=ডাইজেস্টস dirty=ডার্টি doctor's=ডক্টরস doctors=ডক্টরস doing=ডুইং doors=ডোর্স dose=ডোজ draw=ড্র drawing=ড্রয়িং dreams=ড্রিমস
earns=আর্নস ears=ইয়ার্স easy=ঈজি eating=ইটিং elephant=এলিফ্যান্ট empty=এমটি energy=এনার্জি enough=ইনাফ exercise=এক্সারসাইজ explain=এক্সপ্লেইন
facts=ফ্যাক্টস families=ফ্যামিলিজ fast=ফাস্ট faster=ফাস্টার felt=ফেল্ট fingers=ফিংগার্স floor=ফ্লোর flowers=ফ্লাওয়ার্স fly=ফ্লাই follow=ফলো formulas=ফর্মুলাস front=ফ্রন্ট
game=গেইম games=গেইমস gets=গেটস girl=গার্ল glasses=গ্লাসেস gold=গোল্ড got=গট gourd=গোর্ড green=গ্রিন grows=গ্রোজ
habit=হ্যাবিট habits=হ্যাবিটস hall=হল hands=হ্যান্ডস happiness=হ্যাপিনেস head=হেড heart=হার্ট heavier=হেভিয়ার helped=হেল্পড helping=হেল্পিং helps=হেল্পস high=হাই holds=হোল্ডস homeopathic=হোমিওপ্যাথিক homeopathy=হোমিওপ্যাথি hope=হোপ horse=হর্স hours=আওয়ার্স hsc=এইচএসসি human=হিউম্যান
ict=আইসিটি if=ইফ imagine=ইম্যাজিন income=ইনকাম instructions=ইনস্ট্রাকশনস interesting=ইন্টারেস্টিং iron=আয়রন
keep=কিপ keeps=কিপস
label=লেইবেল lamp=ল্যাম্প largest=লার্জেস্ট laugh=ল্যাফ laughing=ল্যাফিং lay=লে lecture=লেকচার lectures=লেকচার্স legs=লেগস listening=লিসেনিং listens=লিসেন্স living=লিভিং loves=লাভস lungs=লাংস
made=মেইড make=মেইক marks=মার্কস math=ম্যাথ meals=মিলস medical=মেডিকেল microscope=মাইক্রোস্কোপ model=মডেল mosquito=মসকিটো mosquitoes=মসকিটোজ mother's=মাদারস mustn't=মাসন্ট
naughty=নটি neighbour=নেইবার nervous=নার্ভাস net=নেট nose=নোজ notebooks=নোটবুকস
oishi=ঐশী oishi's=ঐশীর oranges=অরেঞ্জেস organ=অর্গান other=আদার others=আদার্স
padma=পদ্মা parents=পেরেন্টস parts=পার্টস pass=পাস patient=পেশেন্ট patients=পেশেন্টস perfect=পারফেক্ট physics=ফিজিক্স pills=পিলস plant=প্ল্যান্ট plants=প্ল্যান্টস playing=প্লেইং pots=পটস precious=প্রেশাস principal=প্রিন্সিপাল problem=প্রবলেম protects=প্রটেক্টস protein=প্রোটিন pumps=পাম্পস
questions=কোয়েশ্চেনস
rabbit=র‍্যাবিট rains=রেইনস rainy=রেইনি raj=রাজ raj's=রাজের rani=রানী rarely=রেয়ারলি real=রিয়াল recovering=রিকভারিং regular=রেগুলার respect=রিস্পেক্ট roots=রুটস
school=স্কুল science=সায়েন্স season=সীজন secrets=সিক্রেটস seed=সীড share=শেয়ার shelf=শেলফ shout=শাউট shouting=শাউটিং show=শো shows=শোজ sister's=সিস্টারস skeleton=স্কেলিটন skin=স্কিন skip=স্কিপ slower=স্লোয়ার smile=স্মাইল smiles=স্মাইলস smiling=স্মাইলিং sneeze=স্নিজ sneezing=স্নিজিং society=সোসাইটি someone=সামওয়ান something=সামথিং sometimes=সামটাইমস sound=সাউন্ড spreads=স্প্রেডস ssc=এসএসসি stays=স্টেইজ step=স্টেপ stone=স্টোন stops=স্টপস subjects=সাবজেক্টস such=সাচ sunlight=সানলাইট surprising=সারপ্রাইজিং sweets=সুইটস symptom=সিম্পটম symptoms=সিম্পটমস system=সিস্টেম
teachers=টিচার্স tell=টেল thankful=থ্যাংকফুল them=দেম thing=থিং thinking=থিংকিং through=থ্রু tidy=টাইডি tightly=টাইটলি times=টাইমস tiny=টাইনি tongue=টাং tonight=টুনাইট treatment=ট্রিটমেন্ট trillions=ট্রিলিয়ন্স trust=ট্রাস্ট turtle=টার্টল tv=টিভি
us=আস use=ইউজ useful=ইউজফুল uses=ইউজেস
valuable=ভ্যালুয়েবল vitamins=ভিটামিনস
waiting=ওয়েটিং wall=ওয়াল warm=ওয়ার্ম watching=ওয়াচিং weak=উইক wealth=ওয়েলথ whale=হোয়েল wood=উড word=ওয়ার্ড
yard=ইয়ার্ড years=ইয়ার্স
zumur=ঝুমুর
"""
PRON = dict(p.split("=", 1) for p in _RAW.split())
_TOK = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?(?:-[A-Za-z]+)*")


def build_line(text):
    """'Hello! My name is Sanjoy.' -> 'হ্যালো! মাই নেইম ইজ সঞ্জয়।' (punctuation kept; ।  for a full stop)."""
    def one(m):
        w = m.group(0).lower()
        return "-".join(PRON[x] for x in w.split("-"))
    out = _TOK.sub(one, text)
    out = re.sub(r"\.(?=[\s\"”]|$)", "।", out)
    return out.replace("’", "'")


def missing(texts):
    return sorted({x for t in texts for w in _TOK.findall(t) for x in w.lower().split("-") if x not in PRON})
