import requests
import json
import sys

# a)
adress = 'http://svatky.adresa.info/json'

response = requests.get(adress)

response_json = json.loads(response.text)

name = response_json [0]["name"]
print (f"Dnes ma svatek {name}.")

# b)
date = sys.argv[1]

full_adress = f"{adress}?date={date}"

response = requests.get(full_adress)

response_json = json.loads(response.text)

name = response_json[0]["name"]

day = date[:2]
month = date [2:]

if day [0] =="0":
  day = day[1]

if month [0] == "0":
  month = month[1]

print (f"Dne {day}.{month}. ma svatek {name}.")

import pandas
print(pandas.__version__)