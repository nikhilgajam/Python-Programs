# Program to find even prime factors


def even_prime_factors(num):

    for i in range(1, num+1):
        if num % i == 0:
            count = 0

            for j in range(1, i+1):
                if i % j == 0:
                    count += 1

            if count == 2:
                print(i)


def odd_prime_factors(num):

    for i in range(1, num+1):
        if num % i != 0:
            count = 0

            for j in range(1, i+1):
                if i % j == 0:
                    count += 1

            if count == 2:
                print(i)


even_prime_factors(100)









