def armst(num):
    n = r = 0

    while num > 0:
        n = num % 10
        r = r+n*n*n
        num //= 10

    return r


def arm_rec(num, r=0):
    if num > 0:
        n = num % 10
        r = r+(n*n*n)
        return arm_rec(num//10, r)
    else:
        return r


print(armst(153))