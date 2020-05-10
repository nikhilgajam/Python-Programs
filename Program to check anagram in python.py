print("Anagram Checking Program\nEx:earth & heart\n")

a = input("Enter a string: ")
b = input("Enter another string: ")

a = sorted(a.lower())
b = sorted(b.lower())

if len(a) == len(b):
    if a == b:
        print("\nIt is an Anagram")

else:
    print("\nIt s not an Anagram")
