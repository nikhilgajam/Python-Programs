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


def prime_number(num):
    # Using for loop

    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, "is a Prime number")
    else:
        print(num, "is a Ordinary number")


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


def primes_numbers(num):
    # Using for loop

    for i in range(2, num+1):
        count = 0
        for j in range(1, num+1):
            if i % j == 0:
                count += 1

        if count == 2:
            print(i)


prime(100)
