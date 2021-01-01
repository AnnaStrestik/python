import pprint
from unidecode import unidecode

studenti = []
with open('studenti.txt', 'r', encoding = 'utf-8') as s:
    for student in s.readlines():
        name = student.strip('\n').strip(' ').split('\t')
        studenti.append((name))

pprint.pprint (studenti)

studenti = studenti[1:]
# print (studenti)

rok_narozeni = []
for student in studenti:
  rok = student[2][:2]
  student.append((rok))
  print(student)

pohlavi = []
mesic = [student[2][2:4] for student in studenti]
# print (mesic)

for i in range(1,len(studenti)):
  if int(mesic[i]) > 20:
    pohlavi.append('F')
  else:
    pohlavi.append('M')
print(pohlavi)

for student in studenti:
  zena_muz = pohlavi
  print (student)




jmena = [student[:1] for student in studenti]
seznam_jmen = []
# print (seznam_jmen)
for jmeno in jmena:
  mail = [student + [unidecode(f'{student[1][:5]}{student[0][:3].lower() + '@hybrid.edu'
  seznam_jmen.append((mail))
print (seznam_jmen)


