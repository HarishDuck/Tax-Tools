import pdfquery
import pandas as pd

def extractText(file):
    pdf = pdfquery.PDFQuery(file)
    pdf.load()
    pdf.tree.write('text.txt', pretty_print=True)
    year = pdf.pq('LTTextLineHorizontal:overlaps_bbox("1058, 765, 1082, 776")').text()
    print(year)