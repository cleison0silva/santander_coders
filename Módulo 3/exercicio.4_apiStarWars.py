print("###########################")
print("PROGRAMA API STAR WARS")
print("##########################\n")

import requests
import json

req = requests.get("https://swapi.dev/api/people/4/")
info = json.loads(req.text)

print("Nome: ",info["name"])
print("Altura: ",info["height"])
print("Massa: ",info["mass"])
print("Ano de Nascimento: ",info["birth_year"])

