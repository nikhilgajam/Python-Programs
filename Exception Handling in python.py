try:

    print("Exception Handling\n")

    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(a/b)

except ZeroDivisionError:

    print("You Cannot Divide By Zero Because That Value Goes To Infinity")

except (ValueError, TypeError):

    print("Enter integer(int) values only")

except Exception as ex:     # ex contains the error and we can print it

    print("Error:", ex)

except:

    print("Other Error Man like syntax(typing) error in the code")

finally:

    print("This finally code will be executed before executing other lines irrespective of any error")

# Creating own exception class


class OwnErrorClass(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


# raise OwnErrorClass("Own error class")   # To call own error class


# To raise error with own message

def error_with_own_message(num):
    if not isinstance(num, int):
        raise RuntimeError("Own error message")


# Try and else clause (else is executed when no error occurred)

x = None


try:
    if x is True:
        raise OwnErrorClass("X is True")
    print("OK")
except ZeroDivisionError:
    print("You shouldn't divide a number by zero")
else:
    print("Program executed well")
    
