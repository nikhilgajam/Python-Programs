def revs(num):
    n = r = 0

    while num > 0:
        n = num % 10
        r = r*10+n
        num //= 10

    return r


def rev_rec(num, r=0):
    if num > 0:
        n = num % 10
        r = r*10+n
        return rev_rec(num//10, r)
    else:
        return r


print(revs(789))