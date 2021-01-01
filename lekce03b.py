import sys

print (sys.argv)

bez_nazvu = sys.argv[1:]
print (bez_nazvu)

cisla = [float(cislo) for cislo in bez_nazvu]
print (cisla)

import statistics

prumer = statistics.mean(cisla)
print (prumer)