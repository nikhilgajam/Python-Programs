a = (lambda x: x*x) (100)
print(a)

b = (lambda x, y: x+y) (100, 1000)
print(b)

c = lambda x, y: (x+y)*x
print(c(100, 1000))