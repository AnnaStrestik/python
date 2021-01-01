absolvent_pole = ['Petr', 'Roman', 2017, 0.95, True]

absolvent = {
  'jmeno': 'Petr',
  'prijmeni': 'Roman',
  'rok': 2017,
  'dochazka': 0.95,
  'vyznamenani': True
}

print (absolvent['rok'])

absolventi = [
  {'jmeno': 'Petr', 'prijmeni': 'Roman', 'rok': 2017, 'dochazka': 0.95, 'vyznamenani': True},
  {'jmeno': 'Jana', 'prijmeni': 'Kočanská', 'rok': 2015, 'dochazka': 0.92, 'vyznamenani': True},
  {'jmeno': 'Eva', 'prijmeni': 'Horká', 'rok': 2014, 'dochazka': 0.85, 'vyznamenani': False},
  {'jmeno': 'Ivo', 'prijmeni': 'Roubeník', 'rok': 2017, 'dochazka': 0.75, 'vyznamenani': False}
]

print (absolventi[-1]["dochazka"])

from statistics import mean

dochazka = [absolvent ["dochazka"] for absolvent in absolventi]
print (dochazka)

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


print (kurz ["konani"])