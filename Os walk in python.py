import os

a = os.walk("D:\\")

p = open("Path.txt", "w", encoding="utf-8")

for path, dirs, cont in a:
    p.write("Path: " + str(path) + "\nDirs: " + str(dirs) + "\nContent: " + str(cont)+'\n\n\n')

p.close()

print("Succesfully Written")
