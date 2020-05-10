def powr(num, exp):
    i = exp
    ans = 1
    
    while i > 0:
        ans *= num
        i -= 1
    
    return ans


def revs(num):
    n = r = 0

    while num > 0:
        n = num % 10
        r = r*10+n
        num //= 10
    
    return r


def armst(num):
    n = r = 0
    
    while num > 0:
        n = num % 10
        r = r+n*n*n
        num //= 10
    
    return r


def summ(num):
    n = r = 0
    
    while num > 0:
        n = num % 10
        r = r+n
        num //= 10
    
    return r


def fact(num):
    ans = 1
    while num > 0:
        ans *= num
        num -= 1
        
    return ans


def factors(num):
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end="")
            
            if num > i:
                print(", ", end="")
            if num == i:
                print(".")
            
        i += 1

        
def prime(num):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
            
        i += 1
        
    if count == 2:
        print(num, "is a PRIME Number")
    else:
        print(num, "is a ORDINARY Number")
        
        
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


def primes(num):
    count = 0
    
    i = 1
    while i <= num:
        count = 0
        
        j = 1
        while j <= num:
            if i % j == 0:
                count += 1
            j += 1
        
        if count == 2:
            print(i)
        i += 1


def leap_year(num):
    
    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        print(num, "is a Leap Year")
    else:
        print(num, "is a Normal Year")


def gcdp(num1, num2):
    i = gcd = 1

    while i >= num1 and i >= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
        i += 1
            
    return gcd


def gcd_rec(num1, num2):
    if num2 != 0:
        return gcd_rec(num2, num1 % num2)
    else:
        return num1
    
    
def lcmp(num1, num2):
    i = gcd = 1

    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
        i += 1
            
    lcm = num1*num2//gcd
    return lcm


# Main


k = powr(100, 1)
print(k)
