# Highest repeated word (histogram program)
name = input("Enter file: ")
p = open(name, "r")

# Counts word frequency
counts = dict()
for line in p:
    words = line.split()
    for word in words:
        word = word.lower()  # Makes all words in lowercase to count correctly
        counts[word] = counts.get(word, 0) + 1  # When we have same key then the number increments

# Checks the most common word and stores it
big_count = None
big_word = None

print("\nHistogram:\n", counts)

for word, num in counts.items():
    if big_count is None or num > big_count:   # when big_count is None (initial) and greater one num>big_count
        big_word = word
        big_count = num

# Prints
print("\nData ===>", '"' + big_word + '"', 'repeated', '"' + str(big_count) + '"', 'time(s)')
















