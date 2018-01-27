def punctuationDensity(sentenceList, wordCount):
    punctuation = [",",";","—",":"]
    punctCount = 0
    for sentence in sentenceList:
        for character in sentence:
            if character in punctuation:
                punctCount += 1
    return 100 * punctCount / wordCount
