def extract3b(pages):
    result = {}
    result["form"]="gst3b"


    # Gstin,name,year,month,fileddate
    result["gstin"] = pages[3]
    index = pages.index('Legal name of the registered person')
    result["name"] = pages[index+1]
    result["year"] = pages[index+2]
    result["month"] = pages[index+3]
    result["filed-date"] = pages[index+5]
    

    # Eligible ITC A 0
    dummy = []
    index = pages.index("(A)  ITC Available (whether in full or part)")
    dummy.insert(0,pages[index-1])
    dummy.insert(0,pages[index-2])
    dummy.insert(0,pages[index-3])
    dummy.insert(0,pages[index-4])
    result["itca0"] = dummy

    # Eligible ITC A 1
    dummy = []
    index = pages.index("(1) Import of goods")
    dummy.insert(0,pages[index-1])
    dummy.insert(0,pages[index-2])
    dummy.insert(0,pages[index-3])
    dummy.insert(0,pages[index-4])
    result["itca1"] = dummy

    # Eligible ITC A 2
    dummy = []
    index = pages.index("(2) Import of services")
    dummy.insert(0,pages[index-1])
    dummy.insert(0,pages[index-2])
    dummy.insert(0,pages[index-3])
    dummy.insert(0,pages[index-4])
    result["itca2"] = dummy
    
    # Eligible ITC A 3
    
    dummy = []
    index = pages.index("(3) Inward supplies liable to reverse charge")
    dummy.insert(0,pages[index-1])
    dummy.insert(0,pages[index-2])
    dummy.insert(0,pages[index-3])
    dummy.insert(0,pages[index-4])
    result["itca3"] = dummy

     # Eligible ITC A 4
    
    dummy = []
    index = pages.index("(4) Inward supplies from ISD")
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itca4"] = dummy

    # Eligible ITC A 5
    
    dummy = []
    index = pages.index("(5) All other ITC")
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itca5"] = dummy

    # Eligible ITC R 0
    
    dummy = []
    index = pages.index("(B)  ITC Reversed")
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itcr0"] = dummy

    # Eligible ITC R 1
    
    dummy = []
    index = pages.index("  (1) As per rules 42 and 43 of CGST Rules")
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itcr1"] = dummy

    # Eligible ITC R 2
    dummy = []
    index = pages.index("  (2) Others",index)
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itcr2"] = dummy

    # Eligible ITC R C
    dummy = []
    index = pages.index("(C) Net ITC Available (A) – (B)")
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itcrc"] = dummy

    
    # Eligible ITC D 0
    dummy = []
    index = pages.index("(D)  Ineligible ITC")
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itcd0"] = dummy

    # Eligible ITC D 1
    dummy = []
    index = pages.index(" (1) As per section 17(5)")
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itcd1"] = dummy

    # Eligible ITC D 2
    dummy = []
    index = pages.index(" (2) Others",index)
    dummy.append(pages[index+1])
    dummy.append(pages[index+2])
    dummy.append(pages[index+3])
    dummy.append(pages[index+4])
    result["itcd2"] = dummy

    return result
    