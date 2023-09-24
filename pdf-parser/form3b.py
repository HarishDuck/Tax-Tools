import pdfquery
import pandas as pd

def extract(file):
    pdf = pdfquery.PDFQuery(file)
    pdf.load()
    #pdf.tree.write('text.txt', pretty_print=True)
    result = pdf.extract([
        ('with_parent','LTPage[pageid=\'1\']'),
        ('with_formatter','text'),

        ('gstin','LTTextLineHorizontal:overlaps_bbox("338.0, 690.913, 438.276, 701.913")'),
        ('name','LTTextLineHorizontal:overlaps_bbox("338.0, 660.913, 452.301, 671.913")'),
        ('year','LTTextLineHorizontal:overlaps_bbox("1058.0, 765.913, 1082.464, 776.913")'),
        ('month','LTTextLineHorizontal:overlaps_bbox("1058.0, 745.913, 1120.337, 756.913")'),
        ('filed_date','LTTextLineHorizontal:overlaps_bbox("1058.0, 725.913, 1114.254, 736.913")')
    ])
    print(result)