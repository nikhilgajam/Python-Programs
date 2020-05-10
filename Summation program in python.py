def summ(num):
    n = r = 0

    while num > 0:
        n = num % 10
        r = r+n
        num //= 10

    return r


def sum_rec(num, r=0):
    if num > 0:
        n = num % 10
        r = r+n
        return sum_rec(num//10, r)
    else:
        return r






















print(summ(100))
