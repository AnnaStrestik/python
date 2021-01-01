print ("Anna\nPardubice")

# Spočítejte svůj měsíční příjem víte-li, že pracujete 7 hodin denně se mzdou 450 Kč na hodinu. Řekněme, že měsíc má 21 pracovních dní.
# Uložte si počet pracovních hodin za den do proměnné hodin, hodinovou mzdu do proměnné mzda a počet pracovních dní do proměnné dni. Spočítejte svou výplatu s použitím těchto proměnných.
# Pokud pracujete na živnostenský list, můžete si odečíst 60 % příjmů jako paušál a ze zbytku zaplatíte 15% daň. Uložte si tyto hodnoty do proměnných paušál a dan a spočítejte svůj příjem po zdanění.


mzda_za_hodinu = 450
pracovni_doma_hodin = 7
pracovni_mesic_dni = 21

vyplata = ((pracovni_mesic_dni * pracovni_doma_hodin) * mzda_za_hodinu)
print (f"Vyplata tento mesic cini {vyplata} Kc.")


# Vytvořte seznam průměrných teplot pro každý den.
# Vytvořte seznam ranních teplot.
# Vytvořte seznam nočních teplot.
# Vytvořte seznam dvouprvkových seznamů obsahujících pouze denní a noční teplotu.
# Spočítejte celkovou průměrnou teplotu za celý týden.

teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]
teploty_pondeli = teploty [0] 
teploty_utery = teploty [1] 
teploty_streda = teploty [2] 
teploty_ctvrtek = teploty [3] 
teploty_patek = teploty [4] 
teploty_sobota = teploty [5] 
teploty_nedele = teploty [6] 

seznam_prumernuch_teplot = [(sum(teploty_pondeli)/ len(teploty_pondeli)),(sum(teploty_utery)/ len(teploty_utery)),(sum(teploty_streda)/ len(teploty_streda)),(sum(teploty_ctvrtek)/ len(teploty_ctvrtek)),(sum(teploty_patek)/ len(teploty_patek)),(sum(teploty_sobota)/ len(teploty_sobota)),(sum(teploty_nedele)/ len(teploty_nedele))]
print (seznam_prumernuch_teplot)

dny_prumerne_teploty = [(sum(teploty)[i]/ len(teploty)[i])for i in range (0,4)]


 
dny_v_tydnu = ['pondeli','utery','streda','ctvrtek','patek','sobota','nedele']
print (dny_v_tydnu)

import pprint
tabulka_prumernych_teplot = [[dny_v_tydnu[0],seznam_prumernuch_teplot[0]],[dny_v_tydnu[1],seznam_prumernuch_teplot[1]],[dny_v_tydnu[2],seznam_prumernuch_teplot[2]],[dny_v_tydnu[3],seznam_prumernuch_teplot[3]],[dny_v_tydnu[4],seznam_prumernuch_teplot[4]],[dny_v_tydnu[5],seznam_prumernuch_teplot[5]],[dny_v_tydnu[6],seznam_prumernuch_teplot[6]]]

prumerne_teploty= [[dny_v_tydnu[i],seznam_prumernuch_teplot[i]]for i in range (0,6)]

pprint.pprint (prumerne_teploty)
