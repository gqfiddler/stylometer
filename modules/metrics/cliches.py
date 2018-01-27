import string

def clichePct(text, num_sentences):
    clicheCount = 0
    text = text.lower()
    clicheFile = open("modules/metrics/cliches.txt", "r")
    lines = clicheFile.readlines()
    cliches = [line[:-1] for line in lines] # removing \n from end of lines
    for cliche in cliches:
        if cliche in text:
            clicheCount += 1
    return clicheCount / num_sentences * 100
