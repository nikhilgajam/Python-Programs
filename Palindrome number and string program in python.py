# Palindrome


def palindrome_number(num):

    print("Palindrome Number Program\n")

    temp = num
    r = 0

    while num > 0:

        n = num % 10
        r = r*10+n
        num //= 10

    if r == temp:

        print(r, "==", temp, ": Palindrome Number")

    else:

        print(r, "!=", temp, ": Ordinary Number")


def palindrome_string(string):

    print("Palindrome String Program\n")

    temp = string[::-1]

    if string.lower() == temp.lower():

        print(string + " == " + temp, "Palindrome String")

    else:

        print(string + " == " + temp, "Ordinary String")


palindrome_string("Dad")
