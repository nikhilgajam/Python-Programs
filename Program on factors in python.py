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


factors(100)