import requests

a = requests.get("https://www.cartoonnetworkindia.com/")
k = a.text
with open("a.html", "w", encoding="utf-8") as p:
    p.write(str(k))
