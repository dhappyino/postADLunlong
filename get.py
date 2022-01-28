import pandas as pd
import json
import requests
import numpy as np
from bs4 import BeautifulSoup
from requests.packages import urllib3
from openpyxl.workbook import Workbook

#102

urllib3.disable_warnings()
url = "https://59.126.145.136:53443/fhir/QuestionnaireResponse?authored=gt2021-11-01&_filter=subject%20ne%20356"
response = requests.get(url, verify=False)
total = json.loads(response.text)['total']
print(total)

header=["Id", "Name", "Position", "lastUpdated", "identifier", "status", "reference", "authored"]
for j in range(0,103):
    item=json.loads(response.text)['entry'][0]['resource']['item'][j]['text']
    header.append(item)
df = pd.DataFrame(columns=header)

url2="https://59.126.145.136:53443/fhir/Patient"
response2 = requests.get(url2, verify=False)
total2 = json.loads(response2.text)['total']
her=["id","name","pos"]
df2 = pd.DataFrame(columns=her)
print(total2)

while(1):
    
    try:
        relation2 = json.loads(response2.text)['link'][1]['relation']
        if(relation2=="next"):
            temp2=20
            total2=total2-20
        else:
            temp2=total2
    except:
        continue

    for i in range(0, temp2):
        resource2=json.loads(response2.text)['entry'][i]['resource']
        id2 = "Patient/"+resource2['id']
        try:
            name2 = resource2['name'][0]['text']
            where = resource2['name'][1]['text']
            F_payload2 = [
            id2,
            name2,
            where
        ]
        except:
            name2 = resource2['name'][0]['text']
            F_payload2 = [
            id2,
            name2,
            0
        ]

        s2 = pd.Series(F_payload2, index=her)
        df2 = df2.append(s2, ignore_index=True)

    print(df2)
    try:
        relation = json.loads(response2.text)['link'][1]['relation']
        if(relation=="next"):
            url = json.loads(response2.text)['link'][1]['url']
            response2 = requests.get(url, verify=False)
        else:
            break
    except:
        break




while(1):
    
    try:
        relation = json.loads(response.text)['link'][1]['relation']
        if(relation=="next"):
            temp = 20
            total = total - 20
        else:
            temp = total
    except:
        continue

    for i in range(0, temp):
        resource=json.loads(response.text)['entry'][i]['resource']
        id = resource['subject']["reference"]
        name = ""
        where = ""
        for j in range(0, total2):
            if(id == df2.at[j, "id"]):
                name = df2.at[j, "name"]
                where = df2.at[j, "pos"]

        print(name)
        lastUpdated=resource['meta']['lastUpdated']
        identifier=resource['identifier']['value']
        status=resource['status']
        reference=resource['subject']['reference']
        authored=resource['authored']

        F_payload = [
            id,
            name,
            where,
            lastUpdated,
            identifier,
            status,
            reference,
            authored
        ]

    
        items=resource['item']

        for k in range(0,95):
            try:
                varlue=items[k]['answer'][0]['valueInteger']
            except:
                varlue=items[k]['answer'][0]['valueString']
        
            F_payload.append(varlue)
    
        for k in range(95,103):
            try:
                varlue=items[k]['answer'][0]['valueString']
            except:
                varlue=' '
        
            F_payload.append(varlue)
        s = pd.Series(F_payload, index=header)
        df = df.append(s, ignore_index=True)
    
    try:
        relation = json.loads(response.text)['link'][1]['relation']
        if(relation=="next"):
            url = json.loads(response.text)['link'][1]['url']
            response = requests.get(url, verify=False)
        else:
            break;
    except:
        break
name="名單"
#df2.to_excel('out2.xlsx',sheet_name = name)
print(df)
