from fileUpload import *
from extractText import *

# for now this will only support single file will change it for multiple files
filename = fileUpload()

# for now this wont work cause i am now testing form3b parser
resultArray = extractText(filename)
