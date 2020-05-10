print("Swapping The Numbers\n")

a = int(input("Enter 1: "))
b = int(input("Enter 2: "))

c = a         # We can also write    | a, b = b, a  |
a = b
b = c


print("A =", a, "B =", b)
