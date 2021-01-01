from requests_html import HTML

with open('ukazka.html', encoding="utf-8") as f:
  obsah = f.read()

kod = HTML(html=obsah)

for odstavec in kod.find ("p"):
  print (odstavec.text)

for div in kod.find(".sekce1"):
  print(div)

for odkaz in kod.find("a"):
  print(odkaz.text)
  print(odkaz.attrs["href"])

for nadpis in kod.find("h1,h2,h3,h4,h5,h6"):
  print(nadpis.text)

for seznam in kod.find("ol[type=a]"):
  print(seznam)

for odstavec in kod.find(".sekce1 p"):
  print (odstavec.text)

for prvek_seznamu in kod.find("ol[type=a] li"):
  print(prvek_seznamu.text)