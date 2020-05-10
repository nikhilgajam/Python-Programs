import sys
# Variable Size And Type
x = 100
y = 100.1
z = "A"
z1 = "Aa"

print(type(x), sys.getsizeof(x), "Bytes")
print(type(z), sys.getsizeof(z), "Bytes")
print(type(y), sys.getsizeof(y), "Bytes")
print(type(z1), sys.getsizeof(z1), "Bytes")
