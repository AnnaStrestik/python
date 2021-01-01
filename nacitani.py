soubor = open(r"c:\Users\anna\OneDrive\Desktop\mereni.txt", encoding = "utf8")
# r string ´- zpetna lomitka ztrati vyznam
# utf8 universal text format - umi zapsat jakykoliv soubor - znak
radky = [radek for radek in soubor]
soubor.close ()
# \t je tabulator
# \n je novy radek 
print (radky)
# chci zahodit konce radku - chroustanim
ciste_radky = [udaj.strip () for udaj in radky]
print (ciste_radky)
# strip umaze radky na konci a mezery na zacatku

dny_v_tydnu = [udaj.split ("\t") [0] for udaj in ciste_radky]
teploty =  [float(udaj.split ("\t") [1]) for udaj in ciste_radky]
print (dny_v_tydnu)
print (teploty)
# prevedu si cisla v teplotach ze stringu na cisla float, takze jsem ho pridala k prikazu v teplotach

prumerna_teplota = sum (teploty)/ len (teploty)
print (prumerna_teplota)

