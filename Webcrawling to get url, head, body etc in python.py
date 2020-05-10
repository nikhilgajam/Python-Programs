from bs4 import BeautifulSoup
import requests

# Main code

page_source = requests.get("https://developerinsider.co/c-programming-language-example-by-topics/")

data = BeautifulSoup(page_source.text, "html.parser")


# Explanation


print(data.title)  # url_get.head  (or)  url_get.body
print("==========================================================\n")
print(data.title.string)
print()


# Parent name
print("Title Parent:", data.title.parent.name)


print()
# attributes (links) <a>    print(data.a)

all_links = data.find_all("a")  # All links

# print(str(num) + ".)", link)   All tags and other data (in the below loop you can use this)


# Link

for num, link in enumerate(all_links):
    print(num, link.get("href"))

# You Can Also Use (link.get(id="something"))


# To get text data
print(data.get_text())
