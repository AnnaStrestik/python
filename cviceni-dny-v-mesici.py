pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

soubor = open (r"C:\Users\anna\OneDrive\Desktop\kalendar.txt", encoding = "utf8", mode = "w")

[soubor.write(str(pocet_dnu) + "\n") for pocet_dnu in pocty_dni]
soubor.close()

mesice = ['leden','unor','brezen','duben','kveten','cerven',       'cervenec','srpen','zari','rijen','listopad','prosinec']

soubor = open (r"C:\Users\anna\OneDrive\Desktop\kalendar4.txt", encoding = "utf8", mode = "w")
soubor.write("mesic\tpocet dnu\n")
soubor.write("-----------------\n")
[soubor.write (f"{mesice[i]}\t{pocty_dni[i]}\n")for i in range(12)]
soubor.close()