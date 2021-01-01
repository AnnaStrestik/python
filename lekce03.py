mereni = [
  ['po', 17.3],
  ['út', 16.8],
  ['st', 15.1],
  ['čt', 13.2],
  ['pá', 14.0],
  ['so', 13.9],
  ['ne', 15.8]
]
#1.najit prumernou teplotu
teploty = [den [1] for den in mereni]
print (teploty)

prumer = sum(teploty) / len(teploty)
print (f"Prumerna teplota je {prumer}.")

#2.spocitat vzdalenosti teplot od prumeru
vzdalenosti = [abs (teplota - prumer) for teplota in teploty]
print (vzdalenosti)

#3.najit den s teplotou nejbliz prumeru
nejmensi_vdalenost = min(vzdalenosti)
idx_nejmensi_vzdalenost = vzdalenosti.index (nejmensi_vdalenost)
print (f"Nejmensi vdalenost je {nejmensi_vdalenost} na indexu {idx_nejmensi_vzdalenost}.")

#4.vypsat jeho teplotu
print (mereni [idx_nejmensi_vzdalenost])

import math

print (math.log(15))

import statistics
seznam = [1,2,3,4,5,6,7,7,8,6]
prumer1 = sum (seznam)/ len(seznam)
prumer2 = statistics.mean (seznam)
print (f"muj prumer: {prumer1}")
print (f"statistics: {prumer2}")

import random
print (random.randint(1,6))
print (random.uniform (-100.0, 10.0))

falesna_kostka = random.choices ([1,2,3,4,5,6],[0.1,0.1,0.1,0.1,0.1,0.5])
print (falesna_kostka)

