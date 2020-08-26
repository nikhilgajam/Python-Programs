import matplotlib.pyplot as plt

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


plt.bar(list(count.keys()), list(count.values()), label="Word Count")
plt.title("Character Count Graph")
plt.xlabel("Characters")
plt.ylabel("Count")
plt.yticks(range(1, max(count.values())+1))
plt.legend()
# plt.show()
plt.savefig("Graph.png")













