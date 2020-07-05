import urllib.request
from bs4 import BeautifulSoup

url = urllib.request.urlopen("https://google.com")
x = url.read()

soup = BeautifulSoup(str(x), "html.parser")
get = soup.find_all("a")

for x in get:
    print(x.get('href'))
