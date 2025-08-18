## Create list example

# 1. The dummiest way
square_list = []
for i in range(10):
    square_list.append(i * i)

# print(square_list)

# 2. List comprehension
square_list = [i * i for i in range(10)]
# or longer version
square_list_2 = list(map(lambda x: x * x, range(10)))
print(square_list)
print(square_list_2)


# another example how shorter comprehension is
# (x, y) is a tuple
another_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# is equivalent to:
another_list_2 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            another_list_2.append((x, y))

print(another_list_2)
print(another_list)

# List comprehensions can also be used to flatten a list of lists:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

matrix_change = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix_change)
# it's equivalent to:
transposed = []
for i in range(len(matrix[0])):
    transposed.append([row[i] for row in matrix])
print(transposed)

# There is a built-in function `zip` that can be used to combine multiple lists into a list of tuples
print(list(zip(*matrix)))


# Tuples
empty = ()
singleton = (1,)  # Note the comma, otherwise it's just an int in parentheses
pair = (1, 2)
print(singleton)


# sets
empty_set = set()
basket = {"apple", "banana", "orange"}
print(basket)

letters_1 = set("abracadabra")
letters_2 = set("alacazam")
# letters in 1 but not in 2
print(letters_1 - letters_2)
# letters in 1 or 2
print(letters_1 | letters_2)
# letters in both
print(letters_1 & letters_2)
# letters in either 1 or 2 but not both
print(letters_1 ^ letters_2)

# set comprehension
set_comprehension = {x for x in "abracadabra" if x not in "abc"}
print(set_comprehension)
