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


def armstrong_range():
    print("Armstrong Range Program\n")

    num = int(input("Enter a max range: "))
    power = int(input("Enter the power\nEx: n^3 is Armstrong\n: "))

    r = 0
    temp = num

    print("Numbers in range 1 to", num, ": \n")

    for i in range(1, temp+1):
        num = i

        while num > 0:
            n = num % 10
            r = r+(n**power)   # n**3 == n*n*n is Armstrong
            num //= 10

        if r == i:
            print(i)

        r = 0


print(armst(153))
