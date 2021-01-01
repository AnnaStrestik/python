import sys

cislo = int(sys.argv[1])


if cislo < 0 or cislo > 36:
  print ("Neplatne cislo.")
elif cislo == 0:
  print ("Cislo je nula.")

elif 1 <= cislo <=10 or 19 <= cislo <= 28:
  if cislo %2 == 0:
    print ("Cislo je sude a cerne.")
  else:
    print ("Cislo je liche a cervene.")
else:
  if cislo %2 ==0:
    print ("Cislo je sude a cervene.")
  else:
    print ("Cislo je liche a cerne.")