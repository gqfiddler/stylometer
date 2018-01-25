from modules.metrics.syllables import syllableTotal

def flesch_kincaid_level(sentenceList, wordList):
    return (
    ( 0.39 * (len(wordList) / len(sentenceList)) ) +
    ( 11.8 * (syllableTotal(wordList) / len(wordList)))
    - 15.59
    )

def flesch_reading_ease(sentenceList, wordList):
    return (
    206.385 -
    1.015 * (len(wordList) / len(sentenceList)) -
    84.6 * (syllableTotal(wordList) / len(wordList))
    )

def coleman_liau_index(sentenceList, wordList):
    letterTotal = sum([len(word) for word in wordList])
    return (
    .0588 * 100*letterTotal/len(wordList) -
    .296 * 100*len(sentenceList)/len(wordList) -
    15.8
    )
