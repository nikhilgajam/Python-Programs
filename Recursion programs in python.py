print("Recursion Programs In Python\n")


def rev_rec(num, r=0):
    if num > 0:
        n = num % 10
        r = r*10+n
        return rev_rec(num//10, r)
    else:
        return r


def sum_rec(num, r=0):
    if num > 0:
        n = num % 10
        r = r+n
        return sum_rec(num//10, r)
    else:
        return r


def arm_rec(num, r=0):
    if num > 0:
        n = num % 10
        r = r+(n*n*n)
        return arm_rec(num//10, r)
    else:
        return r


def factorial_rec(num):
    if num == 0:
        return 1
    else:
        return num*factorial_rec(num-1)


def fibonacci_rec(num, a=0, b=1, c=0):

    if num > 0:
        print(a)
        c = a+b
        a = b
        b = c
        return fibonacci_rec(num-1, a, b, c)
    else:
        print("\nThese are the numbers in the range")
        return a  # Highest Value

        
def print_n_times(num):
    if num > 0:
        print(num)
        return print_n_times(num-1)
    else:
        return None


def even_odd_count_rec(num, ec=0, oc=0, tsum=0):
    if num > 0:
        tsum += num
        if num % 2 == 0:
            ec += 1
        else:
            oc += 1
            
        return even_odd_count_rec(num-1, ec, oc, tsum)
    else:
        print("Even Sum =", ec)
        print("Odd Sum =", oc)
        print("Total Sum =", tsum)
        
        return ec, oc, tsum


def gcd_rec(num1, num2):
    if num2 != 0:
        return gcd_rec(num2, num1 % num2)
    else:
        return num1


def lcm_rec(num1, num2):

    gcd = gcd_rec(num1, num2)

    return int((num1 * num2)/gcd)


def power_rec(base, power):
    if power != 0:
        return base * power_rec(base, power-1)
    else:
        return 1


k = even_odd_count_rec(1000)
print(k)
