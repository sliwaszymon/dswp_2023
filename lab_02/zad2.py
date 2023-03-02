import requests
from bs4 import BeautifulSoup

URL = 'https://pl.lipsum.com/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

res = soup.find(id='Panes')
ress = res.find("div")
resss = ress.find("p")

zmienna = resss.get_text()
print(zmienna)