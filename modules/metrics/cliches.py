import string
import os

def clichePct(text, num_sentences):
    clicheCount = 0
    text = text.lower()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    clicheFileName = os.path.join(THIS_FOLDER, "cliches.txt")
    clicheFile = open(clicheFileName, "r")
    lines = clicheFile.readlines()
    cliches = [line[:-1] for line in lines] # removing \n from end of lines
    for cliche in cliches:
        if cliche in text:
            clicheCount += 1
    return clicheCount / num_sentences * 100
