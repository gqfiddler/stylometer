'''
Contains the following list of metric functions
(all metrics return float values):

adverbs: percent of adverbs in words

beVerbs: percent of "to be" verbs in words

cliches: percent of sentences containing a cliche (from list)

contractions: percent of contractions in words

coordination: percent of coordinating conjunctions in words

latinateRoots: percent of Latinate-suffixed words minus percent o
    Germanic-suffixed words

lexicalDiversity: measures lexical diversity per 500 words

logicalConnectives: percentage of logical-connective-words (from list) in words

nominalizations: percentage of nominalizations (verb- or adj- derived nouns)
    in words

passivity: percentage of passive verbs in words

punctuation: non-period punctuation marks per word (also serves as a rough
    inverse measure of clause length)

qualification: percentage of qualifying words from list (e.g., "relatively")
    in words

readibility: contains functions for several different readibility tests (e.g.,
    Flesch-Kincaid) which return approximate U.S. grade levels of education
    required for comprehension

sentences: measures mean and coefficient of variance for sentence length

subordination: percentage of subordinating conjunctions in words

syllables: returns average number of syllables per word (also contains
    syllable-counting function used in readability.py)

'''
