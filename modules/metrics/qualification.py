
qualifyingWords = [
    "likely", "seems", "may", "might", "could", "probably", "pretty", "fairly",
    "somewhat", "relatively", "imply", "implies", "suggest", "suggests"
]

def qualificationRate(wordList):
    qualCount = 0
    for word in wordList:
        if word in qualifyingWords:
            qualCount += 1
    return 100 * float(qualCount)/len(wordList)
