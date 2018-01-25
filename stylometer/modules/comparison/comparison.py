'''
Contains the following functions for comparing data:

readVectors: reads a list of vectors from a csv file

standardizeVector: z-score standardizes a vector of text metrics to the data
table of exemplary writing in the specified genre

findClosest: finds the three most similar authors to a submission

makeSuggestions: analyzes a submission and generates a paragraph of suggestions
for improvement

dendroPlot: generates a dendrogram from a list of vectors & 64-byte encodes it

displayDendro: plots and shows a dendogram from a list of vectors
'''

import numpy
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import minkowski
from io import BytesIO
import base64

def readVectors(filename):
    '''
    Args:
        filename: csv file with equal-length rows of data, where first row
            consists of labels
    Returns:
        a list of vectors (lists), each representing one row of data, excluding
            the first row (labels)
    '''
    vectors = []
    dataFile = open(filename, "r")
    lines = dataFile.readlines()
    for line in lines[1:]: # [1:] omits top row, which consists of metric labels
        stringVector = line[:-1].split(",") # [:-1] omits \n and end of line
        vector = [stringVector[0]] + [float(num) for num in stringVector[1:]]
        vectors.append(vector)
    return vectors

def standardizeVector(textVector, genre):
    '''
    Args:
        textVector: a vector of data analyzed from a text

        genre: the genre of the text ("fiction" or "nonfiction")

    Returns:
        a version of textVector with all values z-score standardized to the
            dataset of exemplary writing in its genre
    '''
    # get comparison set
    if genre == "fiction":
        comparisonSet = readVectors("modules/comparison/data/exemplaryFictionData.csv")
        standardizedCompSet = readVectors("modules/comparison/data/exemplaryFictionDataSTDD.csv")
    if genre == "nonfiction":
        comparisonSet = readVectors("modules/comparison/data/exemplaryNonfictionData.csv")
        standardizedCompSet = readVectors("modules/comparison/data/exemplaryNonfictionDataSTDD.csv")
    # standardize textVector
    stdTextVector = [textVector[0]]
    for i in range(1, len(textVector)):
        num = textVector[i]
        compColumn = [compVector[i] for compVector in comparisonSet]
        standardizedNum = (num - numpy.mean(compColumn)) / numpy.std(compColumn)
        stdTextVector.append(standardizedNum)
    return stdTextVector

def findClosest(textVector, genre):
    '''
    Args:
        vector: vector of data analyzed from a text

        genre: genre of text ("fiction" or "nonfiction")

    Returns:
        a list of three tuples (minkowskiDistance, author) of the three writers
        at the least minkowski distances from the submitted vector, ordered from
        least distance to greatest
    '''
    distanceTuples = []
    if genre == "fiction":
        standardizedCompSet = readVectors("modules/comparison/data/exemplaryFictionDataSTDD.csv")
    if genre == "nonfiction":
        standardizedCompSet = readVectors("modules/comparison/data/exemplaryNonfictionDataSTDD.csv")
    stdTextVector = standardizeVector(textVector, genre)
    # generate minkowski distance for each comparison text
    for vector in standardizedCompSet:
        distance = minkowski(stdTextVector[1:], vector[1:])
        distanceTuples.append((round(distance, 2), vector[0]))
    # return three closest (distance, author) tuples
    distanceTuples.sort()
    return distanceTuples[:3]

def makeSuggestions(textVector, genre):
    '''
    Args:
        textVector: a vector of data analyzed from a text

        genre: the genre of text ("fiction" or "nonfiction")

    Returns:
        a paragraph of suggestions for improving the submitted text
    '''
    suggestions = []
    stdTextVector = standardizeVector(textVector, genre)
    if genre == "nonfiction":
        relevantFeatures = [
        (" how often you use forms of \"to be\"", 2, "reduce"),
        (" how often you use nominalizations", 8, "reduce"),
        (" how often you use passive verbs", 9, "reduce"),
        (" the average sentence length", 11, "increase"),
        (" the average sentence length", 11, "reduce"),
        (" the variety of sentence lengths", 12, "increase"),
        (" the average clause length", 10, "reduce") # TODO: this is the OPPOSITE of punct density
        ]
    if genre == "fiction":
        relevantFeatures = [
        (" the number of adverbs", 1, "reduce"),
        (" how often you use forms of \"to be\"", 2, "reduce"),
        (" the proportion of Latinate to Germanic words", 6, "reduce"),
        (" how often you use passive verbs", 9, "reduce"),
        (" the average sentence length", 11, "increase"),
        (" the average sentence length", 11, "reduce"),
        (" the variety of sentence lengths", 12, "increase"),
        # ("uses of clichés", 1)
        ]

    for tup in relevantFeatures:
        featureName = tup[0]
        index = tup[1]
        changeType = tup[2]
        if (stdTextVector[index] > .5 and changeType == "reduce") \
        or (stdTextVector[index] < -.5 and changeType == "increase"):
            suggestions.append((abs(stdTextVector[index]), featureName, changeType))

    suggestions.sort()

    suggestionString = ""
    if len(suggestions) > 0:
        deviations = suggestions[0][0]
        featureName = suggestions[0][1]
        changeType = suggestions[0][2]
        if deviations > 1.2:
            adverb = ""
        else:
            adverb = "probably"
        suggestionString += "Judging by our metrics, you should " + adverb + " " \
        + changeType + featureName + " in your piece.  "
    if len(suggestions) > 1:
        deviations = suggestions[1][0]
        featureName = suggestions[1][1]
        changeType = suggestions[1][2]
        if deviations > 1.2:
            adverb = "likely"
        else:
            adverb = "may" # yeah yeah, it's not an adverb, I know
        suggestionString += "You  " + adverb + " ought to " + changeType \
         + featureName + " as well.  "
    if len(suggestions) > 2:
        deviations = suggestions[2][0]
        featureName = suggestions[2][1]
        changeType = suggestions[2][2]
        suggestionString += "Finally, consider trying to " + changeType \
         + featureName + "."

    return suggestionString

def dendroPlot(vectorList):
    '''
    Args:
        vectorList: a list of vectors of text data

    Returns:
        a 64-byte-encoded dendrogram matplotlib plot
    '''
    authors = [vector[0] for vector in vectorList]
    statlineMatrix = [vector[1:] for vector in vectorList]
    linkMat = linkage(statlineMatrix, method="average")
    # make plot
    plt.figure(1)
    plt.title("author comparisons")
    plt.subplots_adjust(bottom=0.25)
    dendrogram(linkMat, labels=authors, leaf_rotation=90, leaf_font_size=8)
    # encode plot for passing to html
    img = BytesIO()
    plt.savefig(img, format="png")
    return img

def displayDendro(vectorList):
    '''
    Args:
        vectorList: a list of vectors of text data

    Postcondition:
        display a dendogram of vectors (not for use in app)
    '''
    authors = [vector[0] for vector in vectorList]
    statlineMatrix = [vector[1:] for vector in vectorList]
    linkMat = linkage(statlineMatrix, method="average")
    # make plot
    plt.figure(1)
    plt.title("author comparisons")
    plt.subplots_adjust(bottom=0.25)
    dendrogram(linkMat, labels=authors, leaf_rotation=90, leaf_font_size=8)
    plt.show()


# authorDendro(readVectors("modules/comparison/data/exemplaryNonfictionDataSTDD.csv"))