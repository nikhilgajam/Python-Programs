class Counts:

    count = 0

    def __init__(self):

        Counts.count += 1
        # We are adding to class variable


a = Counts()
print(a.count)

b = Counts()
print(a.count)

c = Counts()
print(c.count)
