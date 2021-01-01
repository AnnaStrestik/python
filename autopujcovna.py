soubor = open(r"C:\Users\anna\Documents\python\auta.txt", encoding = "utf8")

kilometry = [radek.strip().replace(",",".") for radek in soubor]
print (kilometry)

rozsek = [radek.split(" ") for radek in kilometry]
print(rozsek)

najete_km = [float(radek[-1]) for radek in rozsek]