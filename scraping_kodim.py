from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get ('http://kodim.cz/kurzy/python-data/prvni-programy/')


# for ukoly in stranka.html.find('.exercises-section h3'):
#   print(ukoly.text)

# for obtiznost in stranka.html.find(".exercise-body strong"):
#   print(obtiznost.text)

for ukol in stranka.html.find(".exercise-title h3, .exercise-body > p > strong"):
  print(ukol.text)
