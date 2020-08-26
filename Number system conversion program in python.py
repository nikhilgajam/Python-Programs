print("Number System Conversion Program\n")


def string_to_other():
    convert = input("Enter a String: ")
    num = int(input("1. String To Binary\n2. String To Octal\n3. String To Decimal\nString To Hexadecimal\nEnter: "))

    lis = []

    if num == 1:
        for i in convert:
            lis.append(str('0') + bin(ord(i))[2:])
    elif num == 2:
        for i in convert:
            lis.append(oct(ord(i))[2:])
    elif num == 3:
        for i in convert:
            lis.append(ord(i))
    elif num == 4:
        for i in convert:
            lis.append(hex(ord(i))[2:])

    print()

    string = ""

    for i in lis:
        string += i + str(" ")

    string = string.rstrip()

    print(string)


def other_to_string():
    convert = input("Enter a String: ")
    num = int(input("1. Binary To String\n2. Octal To String\n3. Decimal To String\nHexadecimal To String\nEnter: "))

    lis = convert.split()

    string = ""

    try:

        if num == 1:
            for i in lis:
                string += chr(int(i, 2))   # Base 2 is binary
        elif num == 2:
            for i in lis:
                string += chr(int(i, 8))   # Base 8 is octal
        elif num == 3:
            for i in lis:
                string += chr(int(i, 10))  # Base 10 is decimal
        elif num == 4:
            for i in lis:
                string += chr(int(i, 16))  # Base 16 is hexadecimal

        print(string)

    except ValueError:
        print("Select Correct Type Of Number System")


string_to_other()
