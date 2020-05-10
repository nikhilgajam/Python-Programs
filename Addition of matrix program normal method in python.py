print("Matrix Addition Program\n")

row = int(input("Enter rows: "))
col = int(input("Enter columns: "))

a = []
b = []
c = []

# To make entered dimensional matrix

for i in range(row):
    a.append(col*[0])
    
for i in range(col):
    b.append(col*[0])
    
for i in range(row):
    c.append(col*[0])
    
print(c)
    

print("\nEnter matrix 1 elements: ")
    
for i in range(row):
    for j in range(col):
        print("Enter row", i, "column", j, ": ", end="")
        a[i][j] = int(input())
        
        
print("\nEnter matrix 2 elements: ")
        
for i in range(row):
    for j in range(col):
        print("Enter row", i, "column", j, ": ", end="")
        b[i][j] = int(input())
        
        
for i in range(row):
    for j in range(col):
        c[i][j] = a[i][j] + b[i][j]
        
        
print("\nResultant Matrix: \n")
        
for i in range(row):
    for j in range(col):
        print(c[i][j], end="\t")
    print()