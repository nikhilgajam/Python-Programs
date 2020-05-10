import random

print("Rock Paper Scissor Game\n")

items = ["Rock", "Paper", "Scissor"]

print("Enter r: Rock")
print("Enter p: Paper")
print("Enter s: Scissor")
print("Enter q: Quit")

user_points = 0
comp_points = 0
count = 0

while True:
    count += 1

    user = input("\nIteration " + str(count) + " Enter: r (or) p (or) s: ").lower()

    entered = ""

    if 'r' in user:
        entered = "Rock"
    elif 'p' in user:
        entered = "Paper"
    elif 's' in user:
        entered = "Scissor"
    elif 'q' in user:
        break
    else:
        print("Enter Instructed Letters Only")

    comp = random.choice(items)
    print("Computer:", comp)

    if comp == entered:
        print("Tie")
    elif comp == "Rock" and entered == "Paper":
        print("You Got A Point: Paper Covered The Rock")
        user_points += 1
    elif comp == "Paper" and entered == "Rock":
        print("Computer Got A Point: Paper Covered The Rock")
        comp_points += 1
    elif comp == "Scissor" and entered == "Rock":
        print("You Got A Point: Rock Smashed The Scissor")
        user_points += 1
    elif comp == "Rock" and entered == "Scissor":
        print("Computer Got A Point: Rock Smashed The Scissor")
        comp_points += 1
    elif comp == "Paper" and entered == "Scissor":
        print("You Got A Point: Scissor Cuts The Paper")
        user_points += 1
    elif comp == "Scissor" and entered == "Paper":
        print("Computer Got A Point: Scissor Cuts The Paper ")
        comp_points += 1


if user_points > comp_points:
    print("\n\nYou Won", "\nYou Got:", user_points, "Point(s)", "\nComputer Got:", comp_points, "Point(s)",)
elif user_points == comp_points:
    print("\n\nTie", "\nComputer Got:", comp_points, "Point(s)", "\nYou Got:", user_points, "Point(s)")
else:
    print("\n\nComputer Won", "\nComputer Got:", comp_points, "Point(s)", "\nYou Got:", user_points, "Point(s)")
