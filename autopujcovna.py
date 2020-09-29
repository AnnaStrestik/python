# cast2
import sys
# vytvorim si promenou cesta, jakoze cesta k souboru
cesta = sys.argv[1]




soubor = open(cesta, encoding = "utf8")

# ze souboru si chci nacist radky
radky = [radek for radek in soubor]
soubor.close ()

# potrebuju si vytahnout cisla, tj 1.prvek a zbavit se prazdnych radku na konci, proto podminka if
cisla = [radek.split (" ") [1].strip() for radek in radky if radek != "\n"]
print (cisla)

# potrebuju si u promene cisla vymenit carky za tecky a prevest to na float
cisla = [float(cislo.replace(",",".")) for cislo in cisla]
print (cisla)

# sectu si kilometry a vypisu si to
soucet = sum (cisla)
print (f"Celkovy pocet kilometru je {soucet}.")
