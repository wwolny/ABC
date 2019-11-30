import csv
import pandas as pd
import re

columnsN = []
rows = []
idx = -1
idPar = -1
bParam = False
with open("./res.dat", "r") as f:
    for line in f:
        param = re.search(r'param (\w+)', line)
        longParam = re.search(r'\[:,\*,\*,\*\]', line)
        setV = re.search(r'set (\w+\[?\d?\]?)+', line)
        paramVal = re.search(r'\t(?P<param>[0-9\. \t]+)', line)
        values = re.search(':= ([0-9\. \t]+?);', line)
        if param:
            columnsN.append(param.group(1))
            val = re.search(r':= (?P<val>[\d\.e-]+?);', line)
            if val:
                rows.append(val.group("val"))
            else:
                rows.append([])
            if longParam:
                bParam =True
            else:
                bParam=False
            idx+=1
        elif setV:
            columnsN.append(setV.group(1))
            if values:
                rows.append(values.group(1).split())
            else:
                rows.append([])
            idx+=1
        elif paramVal:
            if not bParam:
                rows[idx].append(paramVal.group('param').split())
            else:
                if paramVal.group('param').split()[0] is "1":
                    idPar+=1
                    rows[idx].append([])
                rows[idx][idPar].append(paramVal.group('param').split())

df_dict = {}
for idr, row in enumerate(rows):
    if not type(row) is list:
        df_dict[columnsN[idr]] = row
    else:
        df_dict[columnsN[idr]] = pd.DataFrame(list(row))

for key in df_dict.keys():
    print("\n" + "=" * 40)
    print(key)
    print("-" * 40)
    print(df_dict[key])
