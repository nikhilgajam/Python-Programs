r = int(input("Transpose of matrix program\n\nRows: "))
c = int(input("Columns: "))

arr = [[int(input("==> ")) for i in range(c)] for j in range(r)]

print("\nTransposed Matix: ")

for i in range(r):
    for j in range(c):
        print(arr[j][i], end="\t")
    print()