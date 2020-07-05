import urllib.request

# loading pages using urllib
url = urllib.request.urlopen("https://google.com")
print(url.read())
