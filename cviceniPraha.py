soubor = open(r"C:\Users\anna\OneDrive\Desktop\praha.txt", encoding = "utf8")
radky = [radek for radek in soubor]
soubor.close ()
print (radky)
# kdyz do splitu nedam ceho chci zbavit tak me zbavi mezer a tabulatoru a prazdych radku
seznamy_slov = [radek.split() for radek in radky]
print (seznamy_slov)

delky_radku = [len (radek)for radek in seznamy_slov]
print (delky_radku)

delka_slohu = sum(delky_radku)
print (f"Delka slohove prace je {delka_slohu} slov. Gratulujeme propadl jste.")

