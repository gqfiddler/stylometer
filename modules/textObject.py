'''
contains class TextObject for storing and analyzing texts
'''

import nltk
from modules.processing import wordify
from modules.metrics import adverbs, beVerbs, cliches, contractions, coordination, \
latinateRoots, lexicalDiversity, logicalConnectives, nominalizations, passivity, \
punctuation, qualification, readability, sentences, subordination, syllables


class TextObject(object):
    def __init__(self, text, authorName="You"):
        self.authorName = authorName
        self.text = text
        self.wordList = wordify(self.text)
        self.sentenceList = nltk.sent_tokenize(text)
        self.taggedText = nltk.pos_tag(nltk.word_tokenize(text))
        # specific metrics:
        self.adverbs = adverbs.adverbCount(self.taggedText)
        self.beVerbs = beVerbs.toBeVerbCount(self.wordList)
        self.clichePct = cliches.clichePct(self.text, len(self.sentenceList))
        self.contractions = contractions.contractionPercent(self.text)
        self.coordination = coordination.coordination(self.taggedText)
        self.fkLevel = readability.flesch_kincaid_level(self.sentenceList, self.wordList)
        self.latinateRoots = latinateRoots.latinateRoots(self.taggedText)
        self.lexicalDiversity = lexicalDiversity.computeLexDiv(self.wordList)
        self.logicalConnectives = logicalConnectives.logicalConnectivesPct(self.taggedText, self.wordList)
        self.nominalizations = nominalizations.nominalizations(self.wordList)
        self.passivity = passivity.computePassivity(self.taggedText)
        self.punctuationDensity = punctuation.punctuationDensity(self.sentenceList, len(self.wordList))
        self.qualificationRate = qualification.qualificationRate(self.wordList)
        self.sentenceLength, self.sentenceCV = sentences.sentenceData(self.sentenceList)
        self.subordination = subordination.subordination(self.taggedText)
        self.syllableAverage = syllables.syllableAverage(self.wordList)

        # define vector for comparison to other authors & texts
        self.vector = [self.authorName] + [round(metric, 2) for metric in [
        self.adverbs,
        self.beVerbs,
        self.contractions,
        self.coordination,
        self.fkLevel,
        self.latinateRoots,
        self.lexicalDiversity,
        self.nominalizations,
        self.passivity,
        self.punctuationDensity,
        self.sentenceLength,
        self.sentenceCV,
        self.subordination,
        self.syllableAverage
        ]]

    def getVector(self):
        return self.vector

    def getAdverbs(self):
        return round(self.adverbs, 2)

    def getBeVerbs(self):
        return round(self.beVerbs, 2)

    def getClichePct(self):
        return round(self.clichePct, 2)

    def getCoordination(self):
        return round(self.coordination, 2)

    def getContractions(self):
        return round(self.contractions, 2)

    def getFkLevel(self):
        return round(self.fkLevel, 2)

    def getImpersonality(self):
        return round(self.impersonality, 2)

    def getLatinateRoots(self):
        return round(self.latinateRoots, 2)

    def getLexicalDiversity(self):
        return round(self.lexicalDiversity, 2)

    def getLogicalConnectives(self):
        return round(self.logicalConnectives, 2)

    def getNominalizations(self):
        return round(self.nominalizations, 2)

    def getPassivity(self):
        return round(self.passivity, 2)

    def getPunctuationDensity(self):
        return round(self.punctuationDensity, 2)

    def getQualificationRate(self):
        return round(self.qualificationRate, 2)

    def getSentenceLength(self):
        return round(self.sentenceLength, 2)

    def getSentenceCV(self):
        return round(self.sentenceCV, 2)

    def getSubordination(self):
        return round(self.subordination, 2)

    def getSyllableAverage(self):
        return round(self.syllableAverage, 2)
