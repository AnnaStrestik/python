hlasy = [ 
  [78774, 43179, 225111, 144799, 242854],
  [91062, 22451, 17475, 53391, 46450],
  [179186, 216499, 4493, 156305, 61222],
  [9619, 53476, 926, 64737, 34566],
  [66904, 85730, 27271, 12964, 38041],
  [118755, 1929, 30426, 25178, 31952],
  [64467, 40993, 81181, 39392, 4335],
  [11221, 97970, 26179, 98539, 112578],
  [171064, 7638, 8752, 96666, 39738],
  [74235, 101680, 18920, 45904, 1922],
  [39309, 1505, 10531, 30458, 40228],
  [131584, 1812, 241122, 22267, 99326],
  [194133, 39985, 200997, 28229, 20780],
  [66188, 51607, 15977, 177272, 17664]
]

igor = [kraj [0] for kraj in hlasy]
igor_celkem = sum (igor)
print (f"Igor dostal {igor_celkem} hlasu.")

augustyn = [kraj [1] for kraj in hlasy]
augustyn_celkem = sum (augustyn)
print (f"Augustyn dostal {augustyn_celkem} hlasu.")

vladan_celkem = sum ([kraj [2] for kraj in hlasy])
print (f"Vladan dostal {vladan_celkem} hlasu.")

print (f"Ondrej dostal {sum ([kraj[3] for kraj in hlasy])} hlasu.")

print (f"Radim dostal {sum ([kraj[4] for kraj in hlasy])} hlasu.")

ondrej_celkem = sum ([kraj[3] for kraj in hlasy])
radim_celkem = sum ([kraj[4] for kraj in hlasy])

kandidati_celkem = [igor_celkem, augustyn_celkem, vladan_celkem, radim_celkem]
maximum_hlasu = max (kandidati_celkem)
idx_maxima = kandidati_celkem.index (maximum_hlasu)
jmena = ["Igor Rezek", "Augustyn Dolezal", "Vladan Bednar","Ondrej Brotz","Radim Kaspar"]
print (f"Maximum hlasu dostal kandidat {jmena[idx_maxima]}, a to {maximum_hlasu}.")

kraje_celkem = [sum(kraj) for kraj in hlasy]
# print (kraje_celkem)
minimum_hlasu = min (kraje_celkem)
idx_minimun_hlasu = kraje_celkem.index (minimum_hlasu)
print (f"Minimum hlasu je {minimum_hlasu} v kraji cislo {idx_minimun_hlasu + 1}.")

max_hlasu = max (kraje_celkem)
idx_max_hlasu = kraje_celkem.index (max_hlasu)
print (f"Maximum hlasu je {max_hlasu} v kraji cislo {idx_max_hlasu + 1}.")

#d)
# maxima = [max(kraj) for kraj in hlasy]
# print (maxima)
idx_maxima = [kraj.index (max(kraj)) for kraj in hlasy]
print (idx_maxima)
jmena_maxima = [jmena [kraj.index (max(kraj))]for kraj in hlasy]
print (jmena_maxima)

# e)
procenta_praha = [round (100 * pocet_hlasu / sum (hlasy [0]), 2) for pocet_hlasu in hlasy [0]]
procenta_praha = [f"{procento}%" for procento in procenta_praha]
print (f"Praha : {procenta_praha}")

procenta_jck = [round (100 * pocet_hlasu / sum (hlasy [1]), 2) for pocet_hlasu in hlasy [1]]
procenta_jck = [f"{procento}%" for procento in procenta_jck]
print (f"JCK : {procenta_jck}")

procenta_jmk = [round (100 * pocet_hlasu / sum (hlasy [2]), 2) for pocet_hlasu in hlasy [2]]
procenta_jmk = [f"{procento}%" for procento in procenta_jmk]
print (f"JMK : {procenta_jmk}")

procenta = [[round (100 * pocet_hlasu /sum (hlasy[i]),2) for pocet_hlasu in hlasy [i]] for i in range (0,14)]
import pprint
pprint.pprint (procenta)

# f)
pocet_obyvatel = [1280508, 638782, 1178812,296749,508952,550804,440636,1209879,633925,517087,578629,1338982,821377,583698]
vysoka_ucast = [sum(hlasy[i]) > pocet_obyvatel [i] * 0.5 for i in range (14)]
print (vysoka_ucast)