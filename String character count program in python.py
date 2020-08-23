print("String Character Count Program")

s = input("Enter a string: ")
count = dict()

for i in s:

    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i, j in count.items():

    print("'"+i+"'", ": ", j)


























