'''
contains the following functions for processing raw text:

wordify: splits a text string into a list of words
(necessary for some functions because the nltk word tokenizers split the ends of
contractions & possessives into separate "words")

wordCount: counts words in a text

stripDialogue: removes all sentences that consist partly or wholly of dialogue
(requires that dialogue is marked by quotation marks)
'''
import nltk

def wordify(text):
    '''
    Args:
        text: a single string of raw text
    Returns:
        list of words in text
    '''
    # would be shorter with regex, but I haven't really learned that yet
    removablePunct = [",",";",":","—","–","\"","(",")","..."]
    spacePunct = [".","!","?","-","\n"]
    for punct in removablePunct:
        text = text.replace(punct, "")
    for punct in spacePunct:
        text = text.replace(punct, " ")
    return [word.lower() for word in text.split(" ") if word not in [" ", ""]]

def wordCount(text):
    '''
    Args:
        text: a single string of raw text

    Returns:
        number of words in text (int)
    '''
    return sum(
    [
    1 for i in range(len(text)-1)
    if text[i] in [" ", "\n"]
    and text[i+1] not in [" ", "–", "\n"]
    ])

# NOTE: this next function, which removes all sentences that are partly or wholly
# dialogue, works imperfectly on the txt files, most likely because of their
# formatting inconsistencies.  Use with caution.
def stripDialogue(text):
    '''
    Args:
        text: a single string of raw text

    Returns:
        a string of raw text without any sentences consisting partly or wholly
        of dialogue
    '''
    sentenceList = nltk.sent_tokenize(text)
    dialogueIndices = []
    # first simple quotes, where open and close are identical
    quote_is_open = False
    for i in range(len(sentenceList)):
        sentence = sentenceList[i]
        if "\"" in sentence:
            dialogueIndices.append(i)
            if sentence.count("\"") % 2 != 0:
                quote_is_open = not quote_is_open
        elif quote_is_open == True:
            dialogueIndices.append(i)
    # then formatted quotes, where open and close are different
    quote_is_open = False
    for i in range(len(sentenceList)):
        sentence = sentenceList[i]
        quote_is_open = False
        if "“" in sentence:
            dialogueIndices.append(i)
            if sentence.count("“") != sentence.count("”"):
                quote_is_open = not quote_is_open
        elif quote_is_open == True:
            dialogueIndices.append(i)
    narrationList = [sentenceList[i] for i in range(len(sentenceList)) \
    if i not in dialogueIndices]
    return " ".join(narrationList)
