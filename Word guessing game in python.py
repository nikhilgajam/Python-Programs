import random

eatables = ["Orange", "Apple", "Banana", "Kiwi", "Mango", "Pineapple", "Watermelon", "Muskmelon", "Grapes", "Guava"]
eat = random.choice(eatables)

print("Random Fruit Game\n")
print("1st letter should be capital And Enter 1 to see answer")
print("Enter the name of a fruit")
print("The Hint is: The 3rd letter is {} ".format(eat[2]))

typ = None
while eat != typ:
    typ = str(input("Enter:"))
    if typ == "1":
        print("Answer is:", eat)
    elif typ == eat:
        print("Correct The Answer is:", eat)
    else:
        print("Keep typing new things")




















