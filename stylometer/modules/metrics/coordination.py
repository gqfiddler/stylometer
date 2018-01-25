# the idea here is to measure how often the author uses subordinating structures
# vs. coordinating ones (subordination generally means more complex sentences,
# even for structures of the same length)
# THE CHALLENGE here is that nltk tagging doesn't distinguish between subordinating
# conjunctions (SCs) and prepositions.  This module uses the syntax of the
# subsequent phrase to make the distinction.

def coordination(taggedText):
    ccCount = 0
    for i in range(len(taggedText)):
        word = taggedText[i][0]
        tag = taggedText[i][1]
        if tag == "CC" or (tag == "IN" and word in ["so", "for"]):
            # for some reason nltk doesn't recognize "so" and "for" as CCs
            ccCount += 1
    return ccCount / len(taggedText) * 100
