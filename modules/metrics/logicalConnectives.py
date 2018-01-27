#!/usr/bin/env python
# -*- coding: utf-8 -*-

connectives = [
    "but", "because", "although", "though", "despite", "necessarily",
    "therefore", "thus", "nevertheless", "consequently", "alternatively",
    "resulting", "unless"
    # omitted "if"/"then" because they're ubiquitous outside conditionals
    # omitted "since" because NLTK (annoyingly) lumps prepositions and
    # subordinating conjunctions together, so can't differentiate logical vs temporal
]

connectiveNonAdv = ["so", "yet"]
connectiveWithComma = ["first", "second", "third", "however", "finally"]
# ordering words aren't really logical connectives, but do give logical structure
# however also works followed by

def logicalConnectivesPct(taggedText, wordList): #needs punctuation included
    connectiveCount = 0
    for i in range(0, len(taggedText)):
        word = taggedText[i][0]
        if (
        word in connectives
        or (word in connectiveNonAdv and taggedText[i][1] != "RB")
        or (word in connectiveWithComma and taggedText[i+1][0] == ",")
        or (word == "however" and taggedText[i+1][0] == ".")
        ):
            connectiveCount += 1
    return 100*float(connectiveCount)/len(wordList)


"""
NOTES:
ntlk:
successfully parses "so" as RB (adv) or IN
successfully parses "yet" CC sentence-initial, but not other clause-initial
    (consider adding after-comma excpetion to catch clause-initial)
fails altogether to recognize "for" as a CC; I've excluded
exclude "since" because can't distinguish temporal from causal
"""
