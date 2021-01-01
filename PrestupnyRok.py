rok = 1989

if rok %4 ==0:
  if rok % 100 == 0:
    if rok % 400 == 0:
      prestupny = True
    else:
      prestupny = False
  else:
    prestupny = True
else:
  prestupny = False

if prestupny:
  print ("Rok {rok} je prestupny.")
else:
  print ("Rok neni prestupny.")