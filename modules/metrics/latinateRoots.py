# the idea here is to produce a rough measure of how many Latinate vs Germanic
# words a writer uses.  Actually looking up the root of each word in an etymological
# dictionary would be enormously time-consuming, so instead this metric uses
# suffixes to distinguish the majority of Latinate words.  It also detects
# specifically germanic suffixes and subtracts accordingly from the Latinate score
def latinateRoots(taggedText):
    latinateCount = 0
    germanicCount = 0
    for pair in taggedText:
        word = pair[0]
        tag = pair[1]
        if len(word) > 5:
            for key in latinateSuffixes.keys():
                if word[len(word)-len(key):] == key and tag == latinateSuffixes[key]:
                    latinateCount += 1
                    break
            for key in germanicSuffixes.keys():
                if word[len(word)-len(key):] == key and tag == germanicSuffixes[key]:
                    germanicCount += 1
                    break


    return (latinateCount - germanicCount) / len(taggedText) * 100

germanicSuffixes = {
"hood": "NN",
"dom": "NN",
"doms": "NNS", # plural noun,
"ship": "NN",
"ships": "NNS", # plural noun,
"ling": "NN",
"lings": "NNS", # plural noun,
"kin": "NN",
"kins": "NNS", # plural noun,
"age": "NN",
"ward": "RB",
"wards": "RB",
"ly": "RB",
"like": "JJ",
"ish": "JJ",
"ishly": "RB",
"en": "JJ",
"enly:": "RB",
}

latinateSuffixes = {
# adjectives & adverbs
"ble": "JJ",
"bly": "RB",
"al": "JJ",
"ally": "RB",
"an": "JJ",
"anly": "RB",
"ate": "JJ",
"ent": "JJ",
"ently": "RB",
"ic": "JJ",
"ically": "RB",
"id": "JJ",
"idly": "RB",
"ine": "JJ",
"inely": "RB",
"ive": "JJ",
"ively": "RB",
"ous": "JJ",
"ously": "RB",
# nouns
"ade": "NN",
"ades": "NNS",
"algia": "NN",
"nce": "NN",
"cy": "NN",
"cian": "NN",
"cians": "NNS",
"ule": "NN",
"ules": "NNS",
"ee": "NN",
"sis": "NN",
"et": "NN",
"ets": "NNS",
"ette": "NN",
"ettes": "NNS",
"ice": "NN",
"ide": "NN",
"ine": "JJ",
"ion": "NN",
"ions": "NNS",
"ism": "NN",
"isms": "NNS",
"ist": "NN",
"ists": "NNS",
"ite": "NN",
"ty": "NN",
"ties": "NNS",
"nomy": "NN",
"tude": "NN",
"tudes": "NNS",
"ure": "NN",
"ures": "NNS"
}
