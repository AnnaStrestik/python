import statistics

soubor = open (r"C:\Users\anna\Documents\python\hody.txt", encoding = "utf8")
hody = [int(hod) for hod in soubor]
soubor.close()

if len (hody) > 1000:
  print ('Nespolehlivy vysledek kvuli nedostatku dat.')
  exit()
else:
  print ("jsme v else, achjo")

print (statistics.mean(hody))