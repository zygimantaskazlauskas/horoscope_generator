import random
from datetime import datetime

SENTENCES_IN_HOROSKOPAS = 2

sentences = [
    "Šiandien stokosite ūpo aktyviai veiklai, tačiau galite {{kaVeikti}} ir puikiai pasinaudoti {{kuo}}.",
    "Kad ir kas benutiktų, galite pasikliauti savo {{kuo}}.",
    "Būsite nusiteikę {{kaVeikti}}, {{kaVeikti}}, {{kaVeikti}}.",
    "Venkite {{kaVeikti}}.",
    "Jeigu ketinate {{kaVeikti}}, pasitarkite su suinteresuotais asmenimis.",
    "Nepasiduokite {{kam}}, {{kam}}.",
    "Prasminga pasišnekėti su {{suKuo}} ar {{suKuo}} – gautais pažadais galite tikėti.",
]
used_sentences = []

kuo = ["tvirta valia", "gilia intuicija", "sveiku protu", "paprastumu", "ryžtu"]
kuo_used = []

ka_veikti = [
    "realizuoti meninį įkvėpimą",
    "važinėtis dviračiu",
    "apsidairyti",
    "nusispjauti į viską",
    "aiškintis meilės santykius",
    "ginti vaikų interesus",
    "užsiimti kūryba",
    "tvarkyti turtinius reikalus",
    "veltis į aferas",
    "domėtis aktualia informacija",
    "vykti į kelionę",
    "investuoti į verslą",
    "fiziškai ir protiškai pailsėti",
]
ka_veikti_used = []

kam = ["aplinkinių nerimui", "nepasitenkinimui", "pirmam impulsui"]
kam_used = []

su_kuo = [
    "viršininkais",
    "įtakingais žmonėmis",
    "antra puse",
    "vaikais",
    "šeima",
    "nepažįstamais",
]
su_kuo_used = []


def get_random_from_list(list, dirty):
    randomItem = random.choice(list)
    index = list.index(randomItem)

    if len(dirty) == len(list):
        raise Exception("Visos list" "o reikšmės panaudotos")
    elif index in dirty:
        return get_random_from_list(list, dirty)
    else:
        dirty.append(index)

    return randomItem


def replace_words(sentence, placeholder, wordList, dirtyWordList):
    if placeholder in sentence:
        sentence = sentence.replace(
            placeholder, get_random_from_list(wordList, dirtyWordList), 1
        )
        if placeholder in sentence:
            sentence = replace_words(sentence, placeholder, wordList, dirtyWordList)
    return sentence


def generate_one_sentence():
    sentence = get_random_from_list(sentences, used_sentences)

    sentence = replace_words(sentence, "{{kuo}}", kuo, kuo_used)
    sentence = replace_words(sentence, "{{kaVeikti}}", ka_veikti, ka_veikti_used)
    sentence = replace_words(sentence, "{{kam}}", kam, kam_used)
    sentence = replace_words(sentence, "{{suKuo}}", su_kuo, su_kuo_used)

    return sentence


def generate_horoskopas(sentenceCount):
    resultArray = []

    for i in range(0, sentenceCount):
        resultArray.append(generate_one_sentence())

    return "\n".join(resultArray)


# source: https://stackoverflow.com/a/3274654
def get_zodiac_of_date(date):
    zodiacs = [
        (120, "Ožiaragis"),
        (218, "Vandenis"),
        (320, "Žuvys"),
        (420, "Avinas"),
        (521, "Jautis"),
        (621, "Dvyniai"),
        (722, "Vėžys"),
        (823, "Liūtas"),
        (923, "Mergelė"),
        (1023, "Svarstyklės"),
        (1122, "Skorpionas"),
        (1222, "Šaulys"),
        (1231, "Ožiaragis"),
    ]

    date_number = int("".join((str(date.date().month), "%02d" % date.date().day)))
    for z in zodiacs:
        if date_number <= z[0]:
            return z[1]


def get_zodiakas():
    try:
        data_string = input("Įveskite savo gimimo datą (YYYY-MM-DD):")
        data_object = datetime.strptime(data_string, "%Y-%m-%d")
        return get_zodiac_of_date(data_object)
    except:
        print("Blogas datos formatas. Bandykite dar kartą...")
        get_zodiakas()


print(get_zodiakas())
print(generate_horoskopas(SENTENCES_IN_HOROSKOPAS))
