
def adverbCount(taggedText):
    advCount = 0
    for wordTuple in taggedText:
        if wordTuple[1] == "RB":
            advCount += 1
    return advCount / len(taggedText) * 100
