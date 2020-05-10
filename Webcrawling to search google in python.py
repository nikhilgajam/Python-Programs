from bs4 import BeautifulSoup
import requests

user = input("Enter any keyword: ")
print("googling.......")

google_search = requests.get('https://www.google.com/search?q=' + user)

soup = BeautifulSoup(google_search.text, 'html.parser')

search = soup.select(".r a")
print(search)
for link in search[:5]:
    print(link.get('href'))
# OK
