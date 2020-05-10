def print_without_vowels():
    x = input("Enter a string: ")
    z = []

    for i in x:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            continue
        else:
            z.append(i)

    z.sort()
    print(z)


def print_without_vowels_using_sets():
    input_string = set(input("Enter a string: "))
    vowels = frozenset("aeiou")
    string = input_string.difference(vowels)   # input_string - vowels
    print(sorted(string))

























print_without_vowels_using_sets()
