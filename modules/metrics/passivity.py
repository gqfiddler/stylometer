
def computePassivity(taggedText):
    passiveCount = 0
    for i in range(0, len(taggedText)):
        if taggedText[i][1] == "VBN": #VBN == past participle of a verb
            if checkForToBe(taggedText, i) \
            and not checkForNounAfter(taggedText, i) \
            and not checkForExceptions(taggedText, i):
                passiveCount += 1
    return 100*float(passiveCount)/len(taggedText)
    #might be slightly better to calculate compared to punctuation-less RegexpTokenizer

def checkForToBe(taggedText, index):
    result = False
    scope = 3 #only want to check a few words back; if the verb form is further than 3, it's probably unrelated to the passive participle
    if index < 3:
        scope = index
    while scope > 0 and taggedText[index][0] not in [".", "!", "?", ",", ";", ":", "- "]:
        #Note: this only picks up dashes followed by a space (because of .txt files using ASCII and making no distinction between dash and hyphen)
        if taggedText[index][0] in ["be", "been", "am", "are", "is", "was", "were",
         "get", "gets", "got", "gotten"]:
            result = True
            break
        index -= 1
        scope -= 1

    return result

def checkForNounAfter(taggedText, index):
    #if a noun follows the participle, it's probably an adj and not a passive construction, e.g. "we got painted earrings"
    if taggedText[index+1][1] in ["NN", "NNS", "NNP", "NNPS", "PRP"]:
        return True
    else:
        return False

def checkForExceptions(taggedText, index):
    #function to check for common exceptions
    word = taggedText[index][0]
    postWord = taggedText[index + 1][0] if index < len(taggedText) else '.'
    exceptions = [
        "tired", "excited", "bored", "interested", "scared", "frightened",
        "amused", "confused", "embarrassed", "exhausted", "fascinated",
        "frustrated", "overwhelmed", "pleased", "relaxed", "satisfied",
        "surprised", "shocked", "terrified", "thrilled"
    ]
    if postWord != "by" and word in exceptions:
        return True
    else:
        return False
