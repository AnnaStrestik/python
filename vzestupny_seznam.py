seznam = [1, 3, 4, 5, 6, 7, 10]


# varianta a)
# serazeny_seznam = sorted(seznam)

# if seznam == serazeny_seznam:
#   print ("Seznam je serazeny")
# else:
#   print ("Seznam neni serazeny")

# varianta b)
serazeno = False
for i in range (len(seznam)-1):
  if seznam [i] > seznam [i + 1]:
    serazeno = True

if serazeno:
  print ("Seznam neni serazeny")
else:
  print ("Seznam je serazeny")

