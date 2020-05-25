import requests
from bs4 import BeautifulSoup

# We can use urllib.request but this is much easier

print("Getting Data Please Wait...")

url = requests.get("http://www.gamesfreak.net/")
soup = BeautifulSoup(url.text, "html.parser")
get = soup.find_all("a")

# Writing to hard disk
p = open("links.txt", "w")

# enumerate is used print numbers 1 says enumerate to start at index 1

for e, link in enumerate(get, 1):
    # Getting only specific tag

    data = str(link.get('href', None))
    # every website starts with https://
    if data.startswith("h"):
        # writing to a file with spacings
        p.write(str(e) + "   " + str(data) + "\n\n")


p.close()

print("Done")












