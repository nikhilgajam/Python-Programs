def powr(num, exp):
    i = exp
    ans = 1

    while i > 0:
        ans *= num
        i -= 1

    return ans


print(powr(3, 40))
