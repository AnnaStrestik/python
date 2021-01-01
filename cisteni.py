with open ("spinavy_vstup.txt", encoding = "utf8") as f:
  radky = [radek for radek in f]

print (radky)

# chci: ["Muj oblibeny film je Star Wars","Je moc hezky","Taky je fajn Lord of The Rings","HODNE DOBREJ JE PULP FICTION"]

# smazu volne misto na zacatku a na konci
radky = [radek.strip() for radek in radky]
print (radky)

# zahodim prazdne radky
radky = [radek for radek in radky if radek!= ""]
print (radky)

# vsechny otazniky nahradim teckami
radky = [radek.replace("?",".") for radek in radky]
print (radky)

# Rozdelim vety do samostatnych textovych retezcu.
radky = [radek.split (".") for radek in radky]
print (radky)

# Vycistim vnitrni seznamy.
radky = [[veta.strip()for veta in radek if veta != ""] for radek in radky]
print (radky)

vysledek = []
print ("for cyklus")
for radek in radky:
  print (radek)
  for veta in radek:
    print(f"\t {veta}")
    mala_veta = veta.lower()
    print (f"\t {mala_veta}")
    vysledek.append (mala_veta)

print ("Vysledek programu")
print (vysledek)