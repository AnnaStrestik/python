kurz = {
  'nazev': 'Úvod do programování',
  'lektor': 'Martin Podloucký',
  'konani': [
    {
      'misto': 'T-Mobile', 
      'koucove': [
        'Dan Vrátil', 
        'Filip Kopecký', 
        'Martina Nemčoková'
      ], 
      'ucastnic': 30
    },
    {
      'misto': 'MSD IT', 
      'koucove': [
        'Dan Vrátil', 
        'Zuzana Tučková', 
        'Martina Nemčoková'
      ], 
      'ucastnic': 25
    },
    {
      'misto': 'Škoda DigiLab', 
      'koucove': [
        'Dan Vrátil', 
        'Filip Kopecký', 
        'Kateřina Kalášková'
      ], 
      'ucastnic': 41
    }
  ]
}
# 1)
print (kurz ["konani"][-1]["ucastnic"])

# 2)
print (kurz ['konani'][0]['koucove'][-1])

# 3)
pocet_konani = len(kurz['konani'])
print (pocet_konani)

# 4)vyberu si misto ze slovniku misto ze slovniku konani v tabulce konani
mista = [misto["misto"]for misto in kurz ["konani"]]
print (mista)

for k in kurz['konani']:
  print(k['misto'])



