windows = "cesta\\do\\rise\\smazenych\\krevet"
print (windows)

unixl = windows.replace ("\\","/")
print (unixl)

rozsekano = windows.split ("\\")
print (rozsekano)
unix2 = "/".join (rozsekano)
print (unix2)  

hodiny = 3
minuty = 43
sekundy = 45
# vycpe to na dve cislice aby to melo podobu digitalnich hodin
print (f"{hodiny:02d}:{minuty}:{sekundy}")

pi = 3.141542342342342
# chci zaokrouhlit pi na 4 destinna cistla
print (f"pi = {pi:0.4f}")

import math
print (f"pi = {math.pi}")