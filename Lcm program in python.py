def lcmp(num1, num2):
    i = gcd = 1

    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
        i += 1

    lcm = num1*num2//gcd
    return lcm


def gcd_rec(num1, num2):
    if num2 != 0:
        return gcd_rec(num2, num1 % num2)
    else:
        return num1


def lcm_rec(num1, num2):

    lcm = gcd_rec(num1, num2)
    lcm = (num1 * num2) // lcm
    return lcm


print(lcm_rec(12, 14))
