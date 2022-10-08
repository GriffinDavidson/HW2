import csv
from typing import OrderedDict
import pandas as pd
import json
import sys;
import os;
 
if (sys.argv[2] == "-c"):
    csv_table=pd.read_table(sys.argv[1],sep='\t', encoding="windows-1252")
    
    csv_table.to_csv(sys.argv[1].replace(".tsv", ".csv"),index=False)
    
    print("Successfully made csv file")

elif (sys.argv[2] == '-j'):
    def tsv2Json(inputFile, outputFile):
        arr = []
        file = open(inputFile, 'r')
        a = file.readline()

        titles = [t.strip() for t in a.split('\t')]
        for line in file:
            d = {}
            for t, f in zip(titles, line.split('\t')):
                d[t] = f.strip()
            arr.append(d)
        with open(outputFile, 'w', encoding='utf-16') as outputFile:
            outputFile.write(json.dumps(arr, indent=4))

    tsv2Json(sys.argv[1], sys.argv[1].replace(".tsv", ".json"))

    print("Sucessfully made json file")

elif (sys.argv[2] == "-x"):
    def convert_row(headers, row):
        s = f'<row id="{row[0]}">\n'
        for header, item in zip(headers, row):
            s += f'    <{header}>' + f'{item}' + f'</{header}>\n'
        return s + '</row>'
    with open(sys.argv[1], 'r') as f:
        r = csv.reader(f)
        headers = next(r)
        xml = '<data>\n'
        for row in r:
            xml += convert_row(headers, row) + '\n'
        xml += '</data>'
    with open("Data.xml", "w") as f:
        f.write(xml)
        print("Successfully made xml file")

else:
    print("Invalid arguments!")
