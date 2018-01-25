import numpy

def sentenceData(sentenceList):
    lengths = [sentence.count(" ") for sentence in sentenceList]
    # number of words almost always equals number of spaces
    mean = numpy.mean(lengths)
    cv = numpy.std(lengths)/mean # coefficient of variation
    return mean, cv
