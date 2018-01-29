'''
Contains the following functions for adding and normalizing data:

genTable: creates a new csv data table of text metrics from an index of text file names

addAuthor: add a new author's text to a specified data table

standardize: z-score standardizes a list of numbers

standardizeTable: z-score standardizes columns of a csv data table

'''
from modules.textObject import TextObject
import csv
import random
import numpy
import os

def genTable(indexFileName, newFileName=None):
    '''
    indexFileName: a text file containing a list of file names in the format
    "filename, Author Name".  These files must be text files containing prose
    to be analyzed.

    newFileName: the name of the csv file to be created (if does not end in .csv,
    the .csv extension will be added automatically).  File name will default to
    textData[randomdigits].csv

    postcondition: create csv file which contains all relevant data for the text
    files listed in indexFileName
    '''
    indexFile = open(indexFileName, "r")
    lines = indexFile.readlines()
    columnTitles = ["Author", "adverbs", "to Be verbs", "contractions",
    "coordination", "fkLevel", "latinate roots", "lexicalDiversity",
    "nominalizations", "passivity", "punctuation density", "sentence length",
    "sent length variance", "subordination", "syllable avg"]
    vectors = [columnTitles]
    for line in lines:
        items = line.split(",")
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        textFileName = os.path.join(THIS_FOLDER, "comparison/texts/"+items[0])
        textFile = open(textFileName, "r")
        text = textFile.read()
        authorName = items[1][:-1]
        textObj = TextObject(text, authorName)
        vectors.append(textObj.getVector())
        textFile.close()
    if newFileName:
        filename = newFileName
        if newFileName[-4:] != ".csv":
            filename += ".csv"
    else:
        filename = "textData" + str(int(random.random()*10**5)) + ".csv"
    filename = os.path.join(THIS_FOLDER, "comparison/data/"+filename)
    with open(filename, "w") as indexFile:
        csvWriter = csv.writer(indexFile)
        for vector in vectors:
            csvWriter.writerow(vector)

def addAuthor(authorName, fileName, dataFileName, dataFileName2=None):
    '''
    authorName: name of author to be added to the data file

    fileName: name of the txt file containing the author's prose

    dataFileName: name of the csv data file the author will be added to

    dataFileName2: optional - another csv data file the author will be added to

    postcondition: add one row to bottom of dataFileName containing stats for
    a new author's prose
    '''
    # get text from file & create text object
    textFile = open(fileName, "r")
    text = textFile.read()
    textObj = TextObject(text, authorName)
    textFile.close()
    # add text vector to dataFile
    with open(dataFileName, "a") as dataFile:
        writer = csv.writer(dataFile)
        writer.writerow(textObj.getVector())

def standardize(numlist):
    '''
    numlist: a list of numbers

    return: the z-score standardization of the number relative to the numlist
    '''
    mean = sum(numlist)/len(numlist)
    sd = numpy.std(numlist)
    if sd == 0: # avoid divide-by-zero error (won't typically be relevant)
        sd = .0000000001
    return [ (num-mean) / sd for num in numlist]

def standardizeTable(tableFileName):
    '''
    tableFileName: name of .csv file to be standardized

    postcondition: create csv file "[tableFileName]STDD" in same directory.
    This file is identical to the original except that all rows are standardized.

    EXCLUDES the first row and column, assuming labels.
    '''
    # read file
    tableFile = open(tableFileName, "r")
    lines = [line[:-1] for line in tableFile.readlines()] # removes \n from line end
    rows = [line.split(",") for line in lines]
    for columnNum in range(1, len(rows[0])):  # skips column 1 = author names
        columnTitle = rows[0][columnNum]
        columnVals = [float(rows[i][columnNum]) for i in range(1, len(rows))]
        # standardize columns
        columnVals = [columnTitle] + standardize(columnVals)
        # reassign values in rows accordingly
        for i in range(1, len(rows)):
            rows[i][columnNum] = round(columnVals[i], 2)
    # create new csv file and write in the modified rows
    newFilename = tableFileName[:-4] + "STDD.csv"
    with open(newFilename, "w") as newFile:
        csvWriter = csv.writer(newFile)
        for row in rows:
            csvWriter.writerow(row)
