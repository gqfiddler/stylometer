'''
contains example calls for adding authors or generating new data tables
with authors / texts of your choice
'''
from scipy.spatial.distance import minkowski
import modules.dataGenerator as dataGenerator
import modules.metrics as metrics
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# ADD AUTHOR TO TABLES:
# authorName = "Susan Sontag"
# sourceFileName = os.path.join(THIS_FOLDER, "modules/comparison/texts/Sontag.txt")
# targetFileName = os.path.join(THIS_FOLDER, "modules/comparison/data/exemplaryNonfictionData.csv")
# dataGenerator.addAuthor(authorName, sourceFileName, targetFileName)

# GENERATE NEW TABLES:
# indexFileName = os.path.join(THIS_FOLDER, "modules/comparison/texts/exemplary_nonfiction_index.txt")
# newFileName = "exemplaryNonfictionData"
# dataGenerator.genTable(indexFileName, newFileName)
# dataGenerator.standardizeTable(newFileName)
