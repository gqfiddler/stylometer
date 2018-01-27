'''
contains class Submission for submitted texts and analysis-derived text data
'''
import modules.metrics as metrics
import modules.comparison.comparison as comparison
import modules.dataGenerator as dataGenerator
from modules.textObject import TextObject
import nltk

class Submission(object):
    '''
    Contains all submitted information for a text submission (title, text, genre)
    and all data about the text as analyzed by the metrics modules
    '''

    def __init__(self, title, text, genre):
        self.title = title
        self.text = text
        self.genre = genre
        self.textObj = TextObject(text)
        self.vector = self.textObj.getVector()
        self.stdVector = comparison.standardizeVector(self.vector, self.genre)

    def genReport(self):
        title = self.title
        genre = self.genre
        sentenceAverage = self.vector[11]
        sentenceCV = self.vector[12]
        nominalizations = self.vector[8]
        lexicalDiversity = self.vector[7]
        passivity = self.vector[9]
        fkLevel = self.vector[5]
        toBeVerbCount = self.vector[2]
        similarityReport = comparison.findClosest(self.vector, self.genre)
        recommendations = comparison.makeRecommendations(self.vector, self.genre)
        if self.genre == "nonfiction":
            vectorList = comparison.readVectors("modules/comparison/data/allNonfictionDataSTDD.csv")
        if self.genre == "fiction":
            vectorList = comparison.readVectors("modules/comparison/data/allFictionDataSTDD.csv")
        vectorList.append(self.stdVector)

        report = {
          "title" : title,
          "similarity report" : similarityReport,
          "recommendations" : recommendations,
          "average senLeng" : round(sentenceAverage, 2),
          "senLeng CV" : round(sentenceCV, 2),
          "lexical diversity" : round(lexicalDiversity, 2),
          "nominalizations" : round(nominalizations, 2),
          "passivity" : round(passivity, 2),
          "toBeCount" : round(toBeVerbCount, 2),
          "fkLevel" : round(fkLevel, 2)
        }

        # self.storeReport(report)

        return vectorList, report
