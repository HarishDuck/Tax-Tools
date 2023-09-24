from fileUpload import *
from extractText import *

# for now this will only support single file will change it for multiple files
filename = fileUpload()

resultArray = extractText(filename)
