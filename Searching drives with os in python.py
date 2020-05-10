import os

a = os.walk("D:/")

search = input("Enter something search: ")
search = search.lower()

for path, dirs, cont in a:

    cont = str(cont).split(".")

    if (search in path.lower()) or (search in str(dirs).lower()) or (search in str(cont).lower()):

        print("\nGot What You've Searched: \n")
        print("Path: ", path)
        print("Dirs: ", dirs)
        print("Content: ", cont)

        print()

