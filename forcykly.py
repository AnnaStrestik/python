# cisla = list (map(int,input("Napis cela cisla : ").split()))

# # seznam = ["12", "34", "89"]
# # cisla = list(map(int, seznam))
# # cisla = [int(cislo) for cislo in cisla]

# from pprint import pprint
# pprint(f"Seznam cisel je: {cisla}")

# from pprint import pprint
# pprint(f"Seznam cisel je:  - {cisla}")


# and a or 
jmena = ['petr','karel','pavel','jelena','hana']
for jmeno in jmena:
  if 'a' in jmeno and len(jmeno) > 4:
    print (jmeno)

for jmeno in jmena:
  if 'p' in jmeno or len(jmeno) > 5:
    print (jmeno)

# range
jmena = ['petr','karel','pavel']
for jmeno in jmena:
  print (jmeno)

for cislo in range (0,5):
  print (f"cislo: {cislo} jmeno: {jmena[cislo]}")