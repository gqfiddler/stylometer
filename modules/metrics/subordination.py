# the idea here is to measure how often the author uses subordinating structures
# vs. coordinating ones (subordination generally means more complex sentences,
# even for structures of the same length)
# THE CHALLENGE here is that nltk tagging doesn't distinguish between subordinating
# conjunctions (SCs) and prepositions.  This module uses the syntax of the
# subsequent phrase to make the distinction.
def subordination(taggedText):
    scCount = 0
    nounTags = ["NN","NNS","NNP","NNPS","PRP"]
    for i in range(len(taggedText)):
        word = taggedText[i][0]
        tag = taggedText[i][1]
        if tag == "IN" and word not in ["so", "for"]:
            # from the IN tag we know the word is either a preposition or an SC
            # ("so" and "for" are coordinating conjunctions, but nltk tags them as IN)
            nextNounIndex = None
            checkIndex = i + 1
            # find the next noun, if there is one before the end of the sentence
            while checkIndex < len(taggedText)-1:
                nextTag = taggedText[checkIndex][1]
                if nextTag in nounTags and taggedText[checkIndex+1][1] != "POS":
                    # don't count POS-followed nouns - possessives are syntactically adjs
                    nextNounIndex = checkIndex
                    break
                if nextTag == ".":
                    break
                checkIndex += 1
            # if function found a noun before the end of the sentence, check next word
            if nextNounIndex != None:
                # if the word after the next noun is a verb or adv, it was a SC
                if taggedText[nextNounIndex+1][1][:2] in ["VB", "RB"]:
                    scCount += 1
    return scCount / len(taggedText) * 100

'''
## TEST STATEMENTS:
s = "Although we never knew it, we didn't sue, and it rained blood."
print(subordination(nltk.pos_tag(nltk.word_tokenize(s))))
print(nltk.pos_tag(nltk.word_tokenize(s)))
'''
