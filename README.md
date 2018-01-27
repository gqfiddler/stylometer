THE APP
Stylometer is an Flask app with python3.  It launches web pages that process any text the user submits and display key metrics, author comparisons, and stylistic recommendations.

HOW IT WORKS
The metrics used for analysis and comparison are all fairly straightforward. (Brief descriptions can be found in __init__.py file of the modules/metrics package.)  The actual method of comparison is simply minimum 2nd-order Minkowski distance between data vectors; results are displayed as a list of the three most similar authors, and as a dendrogram that includes the submitter ("You") among the sample authors.  Recommendations are generated based on deviations from exemplary texts in comprehensible and practical stylistic characteristics such as adverb (over)use or sentence length variation.

INSTALLATION
To install and run the app:
- download package & subdirectories
- in Terminal, navigate to subdirectory "stylometer"
- run "pip install -r requirements.txt"
- run "python3 app.py"

MODIFICATION
To add other authors/texts to the comparison dataset:
- first add the desired txt file to the modules/comparison/texts directory. 
- then either call the appropriate functions from modules/dataGenerator.py, or just use the commented-out function calls in newData.py.

IMPORTANT NOTE ABOUT TEXTS: 
Unfortunately, for copyright reasons, only a few of the works used to generate the comparison text data have been included in the modules/comparison/texts directory.  The Bibliography.txt file under modules/comparison/texts lists which works were used for which authors.
    If you want to add data, using the "addAuthor" function in modules/dataGenerator.py will process metrics for a new text and add it to the specified .csv file(s).  If you want to use "genTable" to process multiple texts at once, be sure you pass in a new filename; if the name matches an existing .csv file, it will replace that file.

LICENSE
This app and all its contents are licensed under the MIT License, as specified in LICENSE.txt.