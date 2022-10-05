print("###########################")
print("PROGRAMA COVID 19")
print("##########################\n")

import requests
import json

req = requests.get("https://api.covid19api.com/country/brazil")
info = json.loads(req.text)

data_fim = []

for i in info:
    data_fim.append([i['Confirmed'], i['Deaths'], i['Recovered'], i['Active'], i['Date']])

for x in (range(1, len(data_fim))):
    if data_fim[x][0] == 1:
        print("Data do Primeiro Caso: ", data_fim[x][4])
        break
    else:
        pass