pohyby = [
  56000,
  -10000,
  5000,
  -2000,
  -2000,
  47000,
  30000
]

datumy = [
  '12.03.2018',
  '13.03.2018',
  '15.03.2018',
  '20.03.2018',
  '21.03.2018',
  '22.03.2018',
  '23.03.2018'
]

castka = 0
for i in range(len(pohyby)):
  if pohyby[i] <0:
    if abs(pohyby[i]) > castka:
      print(datumy[i])
      exit()
  castka += pohyby[i]
  print(castka)
print ('ok')