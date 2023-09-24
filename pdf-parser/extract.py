import fitz
from determineForm import *
from gst3b import *

def extract(file):
    pdf = fitz.open(file) # This is an array
    pagesString = extractPages(pdf)
    pages = []

    for page in pagesString:
        pages.extend(page.split('\n'))
        
    #print(*pages,sep="\n")

    form = determineForm(pages[0])
    result = None
    if form=="gst-3b":
        result = extract3b(pages)
    
    return result

def extractPages(file):
    pages = []
    for page in file:
        pages.append(page.get_text("text"))
        #print(pages)
        #print(page.get_text("pages"))
    return pages

