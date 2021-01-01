soubor = open(r"C:\Users\anna\Downloads\pasazeri.txt", encoding = "utf8")
radky = [radek for radek in soubor]
print (radky)

pocty_pasazeru = [radek.strip().replace(","," ") for radek in radky]
print (pocty_pasazeru)

for i in range (0, len (pocty_pasazeru)):
  pocty_pasazeru [i] = int (pocty_pasazeru[i])
print (pocty_pasazeru)