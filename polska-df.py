import pandas as pd
import xml.etree.ElementTree as ET
import re

tree = ET.parse('./polska--D-B-M-N-C-A-N-N-xml/polska--D-B-M-N-C-A-N-N/polska.xml')

root = tree.getroot()

# all nodes
rowsN =[]
print('\nAll nodes data:')
for idx, elem in enumerate(root[0][0]):
#     print("\n"+str(elem.tag) + ": "+ str(elem.attrib.get("id")))
    rowsN.append([elem.attrib.get("id")])
    for subelem in elem:
        for subs in subelem:
#             print(str(subs.tag) + ": "+ str(subs.text))
            rowsN[idx].append(subs.text)

nodes = pd.DataFrame(rowsN,columns=["id", "x", "y"])
nodes.head()

# all links
rowsL =[]

print('\nAll links data:')
for idx, elem in enumerate(root[0][1]):
#     print("\n"+str(elem.tag) + ": "+ str(elem.attrib))
    rowsL.append([elem.attrib.get("id")])
    for subelem in elem:
#         print(str(subelem.tag) + ": "+str(subelem.text) + str(len(subelem.text)))
        if not "Modules" in subelem.tag: rowsL[idx].append(subelem.text)
        for subs in subelem:
            for s in subs:
#                 print(str(s.tag) + ": "+ str(s.text))
                rowsL[idx].append(s.text)

links = pd.DataFrame(rowsL,columns=["id", "source", "target", "setup cost", "capacity1", "cost1", "capacity2", "cost2"])
links.head()


# all demands
rowsD = []
print('\nAll demands data:')
for idx, elem in enumerate(root[1]):
#     print("\n"+str(elem.tag) + ": "+ str(elem.attrib))
    rowsD.append([elem.attrib.get("id")])
    for subelem in elem:
#         print(str(subelem.tag) + ": "+str(subelem.text))
        if not "Paths" in subelem.tag: rowsD[idx].append(subelem.text)
        for idPath, subs in enumerate(subelem):
#             print(str(subs.tag) + ": "+ str(subs.attrib))
            rowsD[idx].append([])
            for s in subs:
#                 print(str(s.tag) + ": "+ str(s.text))
                rowsD[idx][idPath+4].append(s.text)
demands = pd.DataFrame(rowsD, columns=["id","source","target","value","P_0","P_1","P_2","P_3","P_4","P_5","P_6"])
demands.head()
