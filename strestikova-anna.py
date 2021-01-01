# Země, nakažených, mrtvých, uzdravených
coronavirus = [ [ "China", 80967, 3248, 71150 ], 
[ "Italy", 47021, 4032, 5129 ], 
[ "Spain", 20412, 1032, 1588 ], 
[ "Iran", 19644, 1433, 6745 ], 
[ "Germany", 18794, 53, 180 ], 
[ "USA", 16489, 223, 125 ], 
[ "France", 10995, 372, 1295 ], 
[ "South Korea", 8652, 94, 2233 ], 
[ "UK", 3269, 184, 65 ], 
[ "Netherlands", 2994, 106, 2 ], 
[ "Austria", 2491, 6, 9 ], 
[ "Belgium", 2257, 37, 204 ], 
[ "Norway", 1912, 7, 1 ], 
[ "Sweden", 1639, 16, 16 ], 
[ "Denmark", 1255, 9, 1 ], 
[ "Malaysia", 1030, 3, 87 ], 
[ "Portugal", 1020, 6, 5 ], 
[ "Japan", 963, 33, 215 ], 
[ "Canada", 924, 12, 11 ], 
[ "Australia", 876, 7, 46 ], 
[ "Czechia", 833, 0, 4 ], 
[ "Israel", 705, 0, 15 ], 
[ "Brazil", 654, 7, 2 ], 
[ "Ireland", 557, 3, 5 ], 
[ "Pakistan", 500, 3, 13 ], 
[ "Greece", 495, 9, 19 ], 
[ "Luxembourg", 484, 5, 6 ], 
[ "Qatar", 460, 0, 10 ], 
[ "Finland", 450, 0, 10], 
[ "Chile", 434, 0, 6 ], 
[ "Poland", 411, 5, 13 ], 
[ "Iceland", 409, 0, 5 ], 
[ "Singapore", 385, 0, 131 ], 
[ "Indonesia", 369, 32, 17 ]
 ]

# print (coronavirus)
# Kolik zemí je celkem v tabulce?
pocet_zemi = len(coronavirus)
print (f"V tabulce je {pocet_zemi} zemi.")

# Kolik je celkem nakažených ve všech uvedených zemích dohromady?
nakazenych_celkem = sum([pocet [1] for pocet in coronavirus])
print (f"Celkem nakazenych ve vsech zemich dohromady je {nakazenych_celkem}.")

# Kolik je největší počet mrtvých v jedné zemi?
nejvice_mrtvych = max([pocet[2] for pocet in coronavirus])
print (f"Nejvice mrtvych v jedne zemi je {nejvice_mrtvych}.")

# Vytáhněte si ze vstupní tabulky seznam všech zemí (ne, že to ručně opíšete, vymyslete na to kód !).
seznam_zemi = [zeme [0] for zeme in coronavirus]
print (seznam_zemi)

# Seznam z předchozího úkolu převeďte na jeden velký řetězec, jednotlivé země v něm budou oddělené pomlčkou.
zeme_s_pomlckou = "-".join (seznam_zemi)
print (zeme_s_pomlckou)

# Z dat ve vstupní tabulce vytvořte novou tabulku, 
# kde v prvním sloupci bude název země a 
# ve druhém sloupci bude počet aktuálně nakažených 
# (tedy rozdíl mezi celkovým počtem nakažených a počtem zemřelých a uzdravených).

# nakazenych = ([pocet [1] for pocet in coronavirus])
# # print (nakazenych)
# mrtvych = ([pocet[2] for pocet in coronavirus])
# # print (mrtvych)
# uzdravenych = ([pocet[3] for pocet in coronavirus])
# # print (uzdravenych)
# aktualne_nakazenych = [nakazenych[x] -mrtvych[x] - uzdravenych[x] for x in range(len(coronavirus))]

aktualne_nakazenych = [[pocet[0],pocet[1]-pocet[2]-pocet[3]] for pocet in coronavirus]
import pprint
pprint.pprint (aktualne_nakazenych)

