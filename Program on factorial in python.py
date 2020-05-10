def fact(num):
    ans = 1
    while num > 0:
        ans *= num
        num -= 1

    return ans


def factorial_rec(num):
    if num == 0:
        return 1
    else:
        return num*factorial_rec(num-1)


print(factorial_rec(3))