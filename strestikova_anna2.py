radky = []
with open('strestikova_anna_vynosy.csv', 'r', encoding = 'utf-8') as v:
    for radek in v.readlines():
        name = radek.strip('\n').split(';')
        radky.append((name))

with open('psenice.txt', encoding="utf8", mode = "w") as psenice, open('jecmen.txt', mode="w", encoding="utf8") as jecmen:
  psenice.write("Rok-Výnos\n")
  jecmen.write("Rok-Výnos\n")
  for radek in radky:
    if "Pšenice".startswith(tuple(radek)):
      [psenice.write(radek[1] + "-" + radek[2] + "\n")]
    if "Ječmen".startswith(tuple(radek)):
      [jecmen.write(radek[1] + "-" + radek[2] + "\n")]