# this syllable-counting algorithm uses general English phonetic principles,
# so it is only an approximation.  However, it's accurate within about 2%
# and is several orders of magnitude faster than dictionary-based methods
# (such as using cmudict from nltk.corpus

def syllableCount(word):
    word = word.lower()
    syllables = 0
    vowels = ["a","e","i","o","u"]
    bisyllabicClusters = ["ia", "eo", "iu"]
    for i in range(len(word)):
        letter = word[i]
        if letter in vowels:
            if i == len(word)-1: # word-final vowels:
                # any word-final vowel other than "e" is a syllable
                # and "e" counts if preceded by a vowel (since vowels preceding
                # other vowels don't get counted as syllables)
                if letter != "e" or word[i-1] in vowels or \
                (letter=="e" and len(word) < 4): # for "she/he/the/we"
                    syllables += 1
            elif (letter == "e" and i == len(word)-2 and i != 0)\
             and \
            ((word[-1] == "d" and len(word) > 4 and word[i-1] not in ["t","d"]) or \
            (word[-1] == "s" and word[i-1] not in (vowels + ["c","g","h","s","z"]))):
                # past-tense word-final "ed" is only a syllable after alveolar stops
                # word-final -es is only a syllable if it follows the consonants above
                # included vowels because vowels followed by vowels are skipped below
                pass
            elif word[i+1] not in vowels:
                # counts one syllable for every vowel cluster (imperfect metric)
                syllables += 1
            elif (letter + word[i+1]) in bisyllabicClusters:
                # a few vowel combinations are usually two syllables, not one
                syllables += 1
        elif letter == "y" and i != 0:
            # word-initial "y" is never a syllable
            if i != len(word)-1 and word[i-1] not in vowels and word[i+1] not in vowels:
                # any interconsonantal "y" is a syllable
                syllables += 1
            elif i == len(word)-1 and word[i-1] not in vowels:
                # any word-final "y" not preceded by vowel is a syllable
                syllables += 1
    return syllables

def syllableAverage(wordList):
    syllCount = sum([syllableCount(word) for word in wordList])
    return syllCount/len(wordList)

def syllableTotal(wordList):
    return sum([syllableCount(word) for word in wordList])
