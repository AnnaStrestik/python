# klasicka metoda (Martinova)
soubor = open (r"C:\Users\anna\OneDrive\Desktop\mereni.txt", encoding = "utf8")
radky = [radek for radek in soubor]
soubor.close()
print(radky)

# husta metoda (Tomasova)
with open (r"C:\Users\anna\OneDrive\Desktop\mereni.txt", encoding = "utf8") as soubor:
  radky = [radek for radek in soubor]
print (radky)
