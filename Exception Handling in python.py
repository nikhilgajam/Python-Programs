try:

    print("Exception Handling\n")

    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    print(a/b)
    
except ZeroDivisionError:
    
    print("You Cannot Divide By Zero Because That Value Goes To Infinity")

except (ValueError, TypeError):

    print("Enter integer(int) values only")

except Exception as ex:     # ex contains what error it is and prints it

    print("Error:", ex)

except:

    print("Other Error Man like syntax(typing) error in the code")
    
finally:
    
    print("This finally code will be executed before execucting other lines irrespective of any error")
















