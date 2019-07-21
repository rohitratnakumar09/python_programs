import csv
import requests
import json

with open('data.json','r') as json_file:
    json_data=json.load(json_file)
length_dict=len(json_data['organizations'])
headers=list(json_data['organizations'][0].keys())
with open('json_csv.csv','w') as csv_file:
    csvwriter=csv.writer(csv_file)
    csvwriter.writerow(headers)
    for i in range(0,length_dict):
        
        data=list(json_data['organizations'][i].values())
        csvwriter.writerow(data)
