<img src='https://github.com/gqfiddler/stylometer/blob/master/app%20screenshot.png?raw=true' width="460" align="left"/>

# the app
Stylometer is an Flask app with python3.  It launches web pages that process user-submitted text and displays key metrics, author comparisons, and stylistic recommendations.  You can view and use the app online at http://gqfiddler.pythonanywhere.com/

# how it works
### Metrics
The metrics used for stylistic analysis and comparison are fairly straightforward: lexical diversity, reading level, adverb density, clause types, etc. A brief description of each can be found in the __init__.py file of the modules/metrics package.
### Comparison
The method of comparison is simply minimum 2nd-order Minkowski distance between data vectors.  Results are displayed as a list of the three most similar authors by distance, and as a dendrogram of all authors, including the submitter ("You") among the sample authors.  
### Recommendations
Recommendations are generated based on deviations from stylistically exemplary texts (not all stylistic comparisons are exemplary), and are communicated in terms of writing charactersitcs (e.g. sentence length) that are easy to comprehend and modify.

# installation (macOS)
To install and run the app on your localhost:
- download package & subdirectories
- in Terminal, navigate to subdirectory "stylometer"
- run "pip install -r requirements.txt"
- run "python3 app.py"

# modification
To add other authors/texts to the comparison dataset:
- first add the desired txt file to the modules/comparison/texts directory.
- then either call the appropriate functions from modules/dataGenerator.py, or just use the commented-out function calls in newData.py.

# the texts
The texts used to generate the comparison data are drawn from a broad range of well-known authors (Neil Gaiman, Zadie Smith, Joan Didion, etc.).  Unfortunately, for copyright reasons, only a few of these works are included in this repository (they're in the modules/comparison/texts directory).  The Bibliography.txt file under modules/comparison/texts lists which works were used for which authors.
    If you want to add data, using the "addAuthor" function in modules/dataGenerator.py will process metrics for a new text and add them as a new row in the specified .csv file(s).  If you want to use "genTable" to process multiple texts at once, be sure you pass in a new filename; if the name matches an existing .csv file, it will replace that file.

# license
This app and all its contents are licensed under the MIT License, as specified in LICENSE.txt.
