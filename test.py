import csv
import json
import pandas as pd
 
tsv_file='Data.tsv'
 

csv_table=pd.read_table(tsv_file,sep='\t', encoding="windows-1252")
 
csv_table.to_csv('Data.csv',index=False)
 
print("Successfully made csv file")

df = pd.read_csv (r'/Users/dangngo/Desktop/HW2/Data.csv')
df.to_json (r'/Users/dangngo/Desktop/HW2/Data.json')
filename = 'Data.csv'
print("Successfully made json file")

def convert_row(headers, row):
    s = f'<row id="{row[0]}">\n'
    for header, item in zip(headers, row):
        s += f'    <{header}>' + f'{item}' + f'</{header}>\n'
    return s + '</row>'
with open(filename, 'r') as f:
    r = csv.reader(f)
    headers = next(r)
    xml = '<data>\n'
    for row in r:
        xml += convert_row(headers, row) + '\n'
    xml += '</data>'
with open("Data.xml", "w") as f:
    f.write(xml)
    print("Successfully made xml file")
