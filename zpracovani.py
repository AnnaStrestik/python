# import sys
# nazev_souboru = sys.argv[1]

nazev_souboru = input ("napiste jmeno souboru")

if nazev_souboru.endswith(".csv") != True:
  print ("Priloha ma spanou priponu")
  exit ()
else:
  print (f"nazev souboru je:{nazev_souboru}")