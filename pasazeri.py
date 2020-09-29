soubor = open (r"C:\Users\anna\Documents\python\pasazeri.txt", encoding = "utf8")
radky = [radek.strip() for radek in soubor]
soubor.close()

print(radky)

# a) vezmu si jen ten prvni radek co me zajima 
# radek = radky [0] - reseni a

radek = " ".join(radky)
# nejdriv si to splitnu podle mezer abych dostala 4 dvojce a vadi mi volnej radek, tak si to jeste splitnu
cesty = [cesta.strip() for cesta in radek.split(" ")] #reseni b

# vytvorim si vnitrni seznamy prvku
tam_i_zpet = [cesta.split (",") for cesta in cesty]
print (tam_i_zpet)

tam = [int(cesta[0]) for cesta in tam_i_zpet]
zpet = [int(cesta [1]) for cesta in tam_i_zpet]
print (tam)
print (zpet)

celkem_tam = sum(tam)
celkem_zpet = sum(zpet)
print (f"Celkem jelo {celkem_tam} pasazeru tam a {celkem_zpet} pasazeru zpet.")

# b)