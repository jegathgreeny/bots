import requests
from bs4 import BeautifulSoup

res = requests.get('')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

ImageElem = soup.select('')


print(len(ImageElem))
