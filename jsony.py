# import json
# soubor = open('absolventi.json', encoding='utf-8')
# text = soubor.read()
# # metoda read umi nacist cely soubor a prevedeme ho z jsonu na soubor
# soubor.close()
# # funkce load v jsonu prevede soubor na slovnik
# absolventi = json.loads(text)
# print(absolventi)

# import json
# soubor = open('absolventi.json', encoding='utf-8')
# absolventi = json.load(soubor)
# soubor.close()
# print(absolventi)

# import json
# hodiny = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
# soubor = open('hodiny.json', 'w', encoding='utf-8')
# json.dump(hodiny, soubor)
# soubor.close()

# import json
# soubor = open('hodiny.json', encoding='utf-8')
# soubor.close()
# print (hodiny)

import requests
import json
response = requests.get('http://api.kodim.cz/python-data/people')
data = json.loads(response.text)
print (data["gender"][1])

