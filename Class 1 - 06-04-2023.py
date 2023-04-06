"""
    For this session, no Jupiter Notebook.
    There'll be .ipynb files

    Apparently PyTorch is used in ChatGPT

    Jupyter is better for data science and visualizations

    For those of us who have some knowledge, we need some patience so that the
    beginners can catch up

    Tasks
    TODO How to work with Jupiter Notebook Files
"""

# Test 1
# print(type("Sup Dude"))
# print(type(4))
# print(type(4.0))
# print(type(print))

# Test 2
# c = True
# d = [1, 2, 3, 4, 5]
# print(c)
# print(d)

# Test 3
# x = 5
# print(id(x))  # Prints the memory location of the variable, usually in hex

# y = 5
# print(x == y)

# x = "string"
# print(id(x))
# print(x)
# print(x == y)


# Test 4
# name = "John"
# age = 30
# print("Hi, my name is " + name + ", I'm " + str(age) + " years old.")
# print("Hi, my name is", name, ", I'm", str(age), "years old.")
# print(f"Hi, my name is {name}, I'm {age} years old.")


# Test 5
# fruits = ["apple", "banana", "orange", "mango"]
# print(f"My third favourite fruit is {fruits[2]}")

# person = {"name": "Jane", "age": 25, "city": "New York"}
# print(f"{person['name']} is {str(person['age'])} years old.")


# Test 6
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# print(type(matrix))


# Test 7
"""
    Invalid variable names:
        1. Not start the variable name with a number
        2. Don't separate words with a space in the variable name
        3. Can't use the keywords as the variable name
            Eg. for, if, and, del etc
        4. Use snake_case for the variable names
            No camelCase, lowercaseformultiplenames
"""

# Test 8
"""
    He won't go over mathematical operations; eg: Addition, Subtraction etc
    It works the way it does on a calculator

    NOTE: // is used for Floor Division
    Floor division is used to divide a number and get just the quotient
    Eg: 7 // 3 = 2
    This is because the quotient is 2, and the remainder is 1
    And since it's floor division, it only returns the quotient
"""
# quotient = 7 // 3
# print(quotient)

# quotient = 7 / 3
# print(quotient)

# quotient = 6 // 3
# print(quotient)

# Test 9
"""
    Modulo => %
    NOTE: This is used to get the remainder after a number is divided
    Eg: 7 % 3 = 1
    This is because the quotient is 2, and the remainder is 1
    And since it's modulo, it only returns the remainder
"""
# remainder = 7 % 3
# print(remainder)

# # It is good to use when checking whether a number is even or odd
# even = (7 % 2) == 0  # A number divided by 2 is even when its remainder is 0
# print(even)

# even = (6 % 2) == 0
# print(even)

# Test 10
name = input("Enter your name: ")
sandwich = input(f"Hi {name}! Nice to meet you! Would you like a sandwich? ")

if sandwich == "Yes" or "yes" or "Y" or "y":
    print(f"Here's your sandwich {name} 🥪")
else:
    print("Sorry. No sandwich for you.")


# Test 11
"""
    Comments
    You can use:
    # => For single line comments
    """ """ => For multi-line comments

    You can check out how they're used throughout this file
"""
