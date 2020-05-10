def fibo(num):
    a = 0
    b = 1
    c = 0

    for i in range(num):
        print(a)
        a = a+b
        b = c
        c = a

    return i


def fibonacci_rec(num, a=0, b=1, c=0):

    if num > 0:
        print(a)
        c = a+b
        a = b
        b = c
        return fibonacci_rec(num-1, a, b, c)
    else:
        print("\nThese are the numbers in the range \nThe Highest Number: ", end="")
        return a  # Highest Value


print(fibonacci_rec(100))
