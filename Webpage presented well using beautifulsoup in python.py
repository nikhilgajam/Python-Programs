from bs4 import BeautifulSoup
import requests

page_source = requests.get("http://www.cartoonnetworkindia.com/")
url_get = BeautifulSoup(page_source.text, "html.parser")
page = url_get.prettify()

with open("page.html", "w", encoding="utf-8") as p:
    p.write(str(page))
