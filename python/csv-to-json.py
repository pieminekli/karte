#!/usr/bin/python

import json
import csv

file_in = 'pieminekli.csv'
file_out = 'data.json'

arr = []
with open(file_in, encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    for row in csv_reader:
        arr.append(row)

arr2 = []
for idx, row in enumerate(arr):
    # set key, val
    obj1={}
    obj1['id'] = int(row[0])
    obj1['region'] = row[1]
    obj1['parish'] = row[2]
    obj1['location'] = row[3]
    obj1['name'] = row[4]
    obj1['date1'] = row[5]
    obj1['description'] = row[6]
    obj1['type'] = row[7]
    obj1['date2'] = row[8]
    obj1['position'] = {'lat': float(row[9]), 'lng': float(row[10])}
    obj1['status'] = int(row[11])
    obj1['url'] = row[12]
    obj1['locked'] = int(row[13])
    obj1['datetime'] = row[14]
    arr2.append(obj1)

with open(file_out, 'w', encoding='utf8') as outf:
    json.dump(arr2, outf, ensure_ascii=False)
