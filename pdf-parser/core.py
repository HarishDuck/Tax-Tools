from fileUpload import *
from extract import *
import pandas as pd

# supporting multiple files
filenames = fileUpload()
result = []
for file in filenames:
    result.append(extract(file))

summatedData = {
    "itca0":[0,0,0,0],
    "itca1":[0,0,0,0],
    "itca2":[0,0,0,0],
    "itca3":[0,0,0,0],
    "itca4":[0,0,0,0],
    "itca5":[0,0,0,0],
    "itcr0":[0,0,0,0],
    "itcr1":[0,0,0,0],
    "itcr2":[0,0,0,0],
    "itcrc":[0,0,0,0],
    "itcd0":[0,0,0,0],
    "itcd1":[0,0,0,0],
    "itcd2":[0,0,0,0],
    }

for r in result:
    for k in summatedData:
        for row in range(len(summatedData[k])):
            summatedData[k][row] += int(r[k][row].replace(",",""))

data = {
    "(A)  ITC Available (whether in full or part)": summatedData["itca0"],
    "(1) Import of goods":summatedData["itca1"],
    "(2) Import of services":summatedData["itca2"],
    "(3) Inward supplies liable to reverse charge":summatedData["itca3"],
    "(4) Inward supplies from ISD":summatedData["itca4"],
    "(5) All other ITC":summatedData["itca5"],
    "(B)  ITC Reversed":summatedData["itcr0"],
    "(1) As per rules 42 and 43 of CGST Rules":summatedData["itcr1"],
    "(2) Others":summatedData["itcr2"],
    "(C) Net ITC Available (A) – (B)":summatedData["itcrc"],
    "(D)  Ineligible ITC":summatedData["itcd0"],
    "(1) As per section 17(5)":summatedData["itcd1"],
    "(2) Others":summatedData["itcd2"]
}

df= pd.DataFrame(data)

df.T.to_excel("output.xlsx")
# for r in result:
#     print(r["name"])
#     print(r["gstin"])
#     print(r["year"])
#     print(r["month"])
#     print(r["filed-date"])
#     print(r["itca0"])
#     print(r["itca1"])
#     print(r["itca2"])
#     print(r["itca3"])
#     print(r["itca4"])
#     print(r["itca5"])
#     print(r["itcr0"])
#     print(r["itcr1"])
#     print(r["itcr2"])
#     print(r["itcrc"])
#     print(r["itcd0"])
#     print(r["itcd1"])
#     print(r["itcd2"])