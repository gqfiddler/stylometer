from modules.comparison import findClosest, makeSuggestions, authorDendro
from modules.textObject import textObject

def testFindClosest(filename):
    pass

def testMakeSuggestions(filename, authorName, genre):
    ''' takes a txt file, returns suggestions'''
    with open(filename, "r") as file1:
        text = file1.read()
    textObj = textObject(text, authorName)
    return makeSuggestions(textObject.getVector(), genre)

# print(testMakeSuggestions("modules/comparison/texts/StudentEssays_Poor.txt", "students", "nonfiction"))
