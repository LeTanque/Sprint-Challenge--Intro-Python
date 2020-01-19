# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# y = [incoming_input for incoming_input in x if int(incoming_input) % 2 == 0]
# a = ["foo", "bar", "baz"]
# y = [x.upper() for x in a]
# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [name.name for name in humans if "Human: D" in str(name)]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [name.name for name in humans if "e," in str(name)]
print(b)


# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
# def char_range(c1, c2):
#     for c in range(ord(c1), ord(c2)+1):
#         print(chr(c))
print("Starts between C and G, inclusive:")
# c = [name.name for name in humans if char_range("c", "g") in str(name)]
# c = [name.name for name in humans if "Human: C" in str(name) or "Human: D" in str(name) or "Human: E" in str(name) or "Human: F" in str(name) or "Human: G" in str(name)]
# c = [human.name for human in humans if ord(human.name[0]) in range(ord("c"), ord("h"))]
c = [human.name for human in humans if ord(human.name[0]) in range(ord("C"), ord("H"))]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [human.age + 10 for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{human.name}-{human.age}" for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if 27 <= human.age <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(human.name.upper(), human.age + 5) for human in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")

h = [math.sqrt(human.age) for human in humans]
print(h)
