"""
    For this session, no Jupiter Notebook.
    There'll be .ipynb files

    Apparently PyTorch is used in ChatGPT

    Jupyter is better for data science and visualizations

    For those of us who have some knowledge, we need some patience so that the
    beginners can catch up

    Sessions will be on Wednesdays and Thursdays
    2 Sessions a week
    8 Sessions in total

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
# name = input("Enter your name: ")
# sandwich = input(f"Hi {name}! Nice to meet you! Would you like a sandwich? ")

# if sandwich == "Yes" or "yes" or "Y" or "y":
#     print(f"Here's your sandwich {name} 🥪")
# else:
#     print("Sorry. No sandwich for you.")


# Test 11
"""
    Comments
    You can use:
    # => For single line comments
    """ """ => For multi-line comments

    You can check out how they're used throughout this file
"""

# Exercise 1
"""
    Write a program to prompt the user for hours and rate per hour to compute
    gross pay.

    Eg:
    Enter Hours: 35
    Enter Rate: 2.75
    Pay: 96.25

    Where Pay = Hours * Rate
"""
# # * Initial Submission
# hours = input("Enter Hours: ")
# rate = input("Enter Rate: ")
# hours = float(hours)
# rate = float(rate)
# pay = hours * rate
# print(f"Pay: {pay}")


# # * Shortened code
# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))
# print(f"Pay: {hours * rate}")

"""
    NOTE:
    I've seen that with regard to the way the lecturer works, he prioritizes
    concise code over verbose code.

    He also prefers efficient yet readable code.

    Have to keep watch for this.
"""


# Exercise 2
"""
    Write a program which prompts the user for a Celsius temperature, convert
    the temperature to Fahrenheit, and print out the converted temperature.

    fahrenheit = celsius * 1.8 + 32
"""
# * Initial Submission
# celsius = float(input("Input a temperature in Celsius: "))
# print(f"Your temperature in Fahrenheit is {celsius * 1.8 + 32}ºF")

# * Custom Implementation
# celsius = float(input("Input a temperature in Celsius: "))
# fahrenheit = format(celsius * 1.8 + 32, ".2f")  # Formats to 2 decimal places
# print(f"Your temperature in Fahrenheit is {fahrenheit}ºF")


# Test 12
"""
    Boolean Algebra
    To check if a value is an instance of a certain data type we use:
    isinstance(variable, data_type)

    Eg:
    x = 5
    print(isinstance(x, list)) => This will print false
"""
# # If Statements
# x = 5
# if x > 0:
#     print("x is positive")

# # If with Else Statement
# x = 0
# if x > 0:
#     print("x is positive")
# else:
#     print("x is either zero or negative")


# # One Liner
# x = -5
# print("x is positive") if x > 0 else print("x is either zero or negative")

# # Chained Conditionals
# x = 5
# y = 10

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x and y are equal")

# choice = "b"
# if choice == "a":
#     print("Bad guess")
# elif choice == "b":
#     print("Good guess")
# else:
#     print("Close, but not correct")


# Nested conditionals
# x = 5
# y = 10

# if x == y:
#     print("x and y are equal")
# else:
#     if x < y:
#         print("x is less than y")
#     elif x > y:
#         print("x is greater than y")


# Test 13
"""
    Error Handling
    Usually try and except, and raising exceptions
"""
# # try and except
# try:
#     print(x)
# except Exception as exception:
#     print(f"An exception occurred. Exception message: {exception}")

# try:
#     print(x)
# except Exception:
#     pass

# try:
#     print(x)
# except NameError as error:
#     print(f"An exception occurred. Exception message: {error}")
# except Exception as exception:
#     print(f"Something went wrong. Exception message: {exception}")
# else:
#     print("Something went wrong.")

# try:
#     print(x)
# except NameError as error:
#     print(f"An exception occurred. Exception message: {error}")
# except Exception as exception:
#     print(f"Something went wrong. Exception message: {exception}")
# else:
#     print("Something went wrong.")
# finally:
#     print("Exit Code 0")

# Try Catch Implementation for choice
# try:
#     choice = input("Input a letter: ")
#     response = {"a": "Bad guess", "b": "Good guess"}
#     print(response[choice])
# except Exception:
#     print("Close, but not correct")


# # Raise an Exception
# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# x = -1

# if x < 0:
#     raise NameError("Sorry, no numbers below zero")

# x = "hello"

# if not type(x) is int:
#     raise TypeError("Only integers allowed")


# Exercise 3
"""
    1.Rewrite your pay computation to give the employee 1.5 times the hourly
    rate for hours worked above 40 hours.

    Eg:
    Enter Hours: 45
    Enter Rate: 10
    Pay: 475.0
"""
# # * Initial Submission
# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))
# pay = 0.0

# if hours <= 40:
#     pay = hours * rate
# elif hours > 40:
#     overtime_hours = hours - 40
#     pay = (40 * rate) + (overtime_hours * (rate * 1.5))

# print(f"Pay: {pay}")

# # * Custom Implementation
# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))
# overtime_mark = 40.0
# pay = 0.0

# if hours <= overtime_mark:
#     pay = hours * rate
# elif hours > overtime_mark:
#     overtime_hours = hours - overtime_mark
#     pay = (overtime_mark * rate) + (overtime_hours * (rate * 1.5))

# print(f"Pay: {pay}")

# # * Other Custom Implementation
# pay = 0.0
# overtime_mark = 40.0

# try:
#     hours = float(input("Enter Hours: "))
#     rate = float(input("Enter Rate: "))

#     if hours <= overtime_mark:
#         pay = hours * rate
#     elif hours > overtime_mark:
#         overtime_hours = hours - overtime_mark
#         pay = (overtime_mark * rate) + (overtime_hours * (rate * 1.5))
#     print(f"Pay: {pay}")
# except Exception:
#     print("Please input a numeric value")
