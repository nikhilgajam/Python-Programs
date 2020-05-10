import random
print("Random Number Guessing Game\n")

rand = random.randrange(11)
typ = None
while rand != typ:
    typ = int(input("Enter: "))
    if rand < typ:
        print("It is little higher")
    elif rand > typ:
        print("It is little lower")
    else:
        print("Correct The Number is:", rand)
        break
