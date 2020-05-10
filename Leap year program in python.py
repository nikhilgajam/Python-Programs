def leap_year(num):

    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        print(num, "is a Leap Year")
    else:
        print(num, "is a Normal Year")


x = int(input("Enter a year: "))
leap_year(x)
