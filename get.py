import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
from requests.packages import  urllib3
from openpyxl.workbook import Workbook

#102

urllib3.disable_warnings()
url = "https://59.126.145.136:53443/fhir/QuestionnaireResponse?authored=gt2021-11-01&_filter=subject%20ne%20356"
response = requests.get(url, verify=False)
total = json.loads(response.text)['total']
print(total)

header=["id", "lastUpdated", "identifier", "status", "reference", "authored"]
for j in range(0,103):
    item=json.loads(response.text)['entry'][0]['resource']['item'][j]['text']
    header.append(item)
df = pd.DataFrame(columns=header)

url2="https://59.126.145.136:53443/fhir/Patient"
response2 = requests.get(url2, verify=False)
total2 = json.loads(response2.text)['total']
print(total2)

while(1):
    
    try:
        relation = json.loads(response.text)['link'][1]['relation']
        if(relation=="next"):
            temp=20
            total=total-20
        else:
            temp=total
    except:
        continue

    for i in range(0, temp):
        resource=json.loads(response.text)['entry'][i]['resource']
        id = resource['id']
        lastUpdated=resource['meta']['lastUpdated']
        identifier=resource['identifier']['value']
        status=resource['status']
        reference=resource['subject']['reference']
        authored=resource['authored']

        F_payload = [
            id,
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
name="問卷"
df.to_excel('out.xlsx',sheet_name = name)
print(df)
