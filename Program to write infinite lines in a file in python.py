print("Program to write infinite no.of lines in python")

type = str(input("Enter ~ to stop:\n"))

with open("a.txt", "w") as p:
        
    while type != '~':
        p.write(type)
        p.write("\n")
        type = str(input())





































