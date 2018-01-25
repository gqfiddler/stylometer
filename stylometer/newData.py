'''
contains example calls for adding authors or generating new data tables
with authors / texts of your choice
'''
from scipy.spatial.distance import minkowski
import modules.dataGenerator as dataGenerator
import modules.metrics as metrics

# ADD AUTHOR:
# dataGenerator.addAuthor("Susan Sontag", "modules/comparison/texts/Sontag.txt",
# "modules/comparison/data/exemplaryNonfictionData.csv")


# GENERATE TABLES:
# dataGenerator.genTable("modules/comparison/texts/exemplary_nonfiction_index.txt", "exemplaryNonfictionData")
# dataGenerator.standardizeTable("modules/comparison/data/allNonfictionData.csv")
