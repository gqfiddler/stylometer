def contractionPercent(text):
    wordCount = 1
    contractionCount = 0
    for i in range(1, len(text)-1):
        character = text[i]
        if (character in ["'", "’"]
        and text[i-1] != " " # deselects start-quotes within quotes and dialect
        and text[i+1] != " " # deselects end-quotes within quotes and dialect
        and text[i+1] != "s"): # deselects possessives
            contractionCount += 1
        elif character == " ":
            wordCount += 1
    return 100 * contractionCount / wordCount
