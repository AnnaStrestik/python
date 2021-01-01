from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get ('http://scrape.kodim.cz/dhmo/index')

for nadpisy in stranka.html.find('h2'):
  print (nadpisy.text)

for cesty_odkazu in stranka.html.find('ol li a'):
  print(cesty_odkazu.attrs["href"])

for obrazky in stranka.html.find('img'):
  atributy = obrazky.attrs
  print(atributy["src"])