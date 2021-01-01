from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get ('http://scrape.kodim.cz/sample/index')

for odstavec in stranka.html.find('p'):
  print(odstavec.text)