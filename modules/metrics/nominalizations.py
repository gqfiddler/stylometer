def nominalizations(wordList):
    noms = 0
    for word in wordList:
        if word.endswith("tion") and len(word) > 9 and word not in [
        "population", "information", "organization," "organisation", "collection",
        "institution", "proportion," "legislation", "exhibition", "conversation,"
        "generation", "concentration", "revolution", "connection"
        ]:
            noms += 1
        elif word.endswith("sion") and len(word) > 9 and word not in [
        "television", "profession", "permission", "depression", "compassion",
         "transfusion", "hypertension", "percussion", "disillusion", "concussion"
         ]:
            noms += 1
        elif word.endswith("ity") and len(word) > 6 and word not in [
        "opportunity", "electricity", "personality", "probability", "inequality"
        ]:
            noms += 1
        elif word.endswith("ment") and len(word) > 7 and word not in [
        "government", "environment", "department", "management", "argument",
        "statement", "investment", "treatment", "parliament", "document", "instrument",
        "fragment", "regiment", "basement", "sediment", "sentiment", "compartment",
        "ornament"
        ]:
            noms += 1
        elif word.endswith("ance") and len(word) > 9 and word not in [
        "performance", "renaissance", "appearance", "inheritance"
        ]:
            noms += 1
        elif word.endswith("ence") and len(word) > 9 and word not in [
        "experience", "difference", "conference", "confidence", "consequence",
        "intelligence", "conscience", "excellence", "adolescence", "inconvenience",
        "turbulence"
        ]:
            noms += 1

    return 100*float(noms)/len(wordList)


#consider doubling points if the ending precedes "of" or "that"? (the insinuation of / insinuation that)
