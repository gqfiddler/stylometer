def toBeVerbCount(wordList):
    instances = 0
    for word in wordList:
        if word in ["is", "are", "was", "were", "be"]:
            instances += 1
    return instances/len(wordList) * 100
