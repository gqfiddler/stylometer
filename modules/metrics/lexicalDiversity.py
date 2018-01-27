# i.e., type-token ratio
from nltk import SnowballStemmer

# TODO: find a method to regularize lexical diversity for text length instead of
# arbitrarily choosing to measure by increments of 500 words.  Start by plotting
# lexical diversity against length from short essays to novels, and observe the
# trend.  My guess is that lexDiv might be linear against log of textLength
def computeLexDiv(wordList):
    '''
    wordList: a tokenized string with symbols removed
    returns: average type-token ration per 500 word segment
    '''
    if len(wordList) < 500:
        return lexDiv(wordList)
    else:
        totalLexDiv = 0
        segmentCount = 0
        while len(wordList) > 500:
            totalLexDiv += lexDiv(wordList[:500])
            wordList = wordList[500:]
            segmentCount += 1
        averageDiv = totalLexDiv / segmentCount
        return averageDiv

def lexDiv(wordList):
    stemmer = SnowballStemmer("english")
    stems = [stemmer.stem(word) for word in wordList]
    return len(set(stems))/len(stems)

#print computeLexDiv(word_tokenize("Here is a sentence that I am trying to determine the lexical diversity of, but it has nearly no repeated words repeated words."))
