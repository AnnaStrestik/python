jmena = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

soubor = open (r"C:\Users\anna\OneDrive\Desktop\jmena.txt", encoding = "utf8", mode="w")
[soubor.write(jmeno + "\n")for jmeno in jmena]
soubor.close()

soubor = open (r"C:\Users\anna\OneDrive\Desktop\jmena2.txt", encoding = "utf8", mode="w")
soubor.write (",".join(jmena))
soubor.close()