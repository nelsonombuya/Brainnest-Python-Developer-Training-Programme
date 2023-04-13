# # Functions
# """
#     Used to minimise repeated code
# """


# def my_function():
#     print("Hello from a function")


# def my_name(fname):  # The argument
#     print(f"{fname} Johnson")


# my_function()
# my_name("Nelson")  # The parameter
# my_name("Tobias")
# my_name("Linus")
# my_name("Emil")
# """
#     Parameter and argument can be used interchangeably
# """


# def my_full_name(fname, lname):
#     print(f"{fname} {lname}")


# my_full_name("Nelson", "Ombuya")


# def math_function(x):
#     return 5 * x


# print(math_function(3))
# print(math_function(5))
# print(math_function(9))


"""
    Intermediate Functions

    Non-Key-Word arguments
    This allows for more flexible arguments in a function
    Ha

    There are Key word arguments
"""


# def my_function(*args):
#     for arg in args:
#         print(arg)


# my_function("Hello", "My", "Name", "Is", "Cow")


# def my_second_function(arg1, *argv):
#     print("First argument: ", arg1)

#     for arg in argv:
#         print("Next argument through *argv: ", arg)


# def function(arg1, arg2, arg3):
#     print("arg1: ", arg1)
#     print("arg2: ", arg2)
#     print("arg3: ", arg3)


# args = (1, 2, 3)
# function(*args)


# Key-word arguments
# Arguments from a dictionary
# def function_2(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)


# # Default arguments
# def function_4(country="Kenya"):
#     print("I am from", country)


# function_4()
# function_4("Sweden")

"""
    Exercise 1
    Rewrite your pay computation with time-and-a-half for overtime and create
    a function called computepay which takes two parameter (hours and rate).

    Enter Hours: 45
    Enter Rate: 10
    Pay: 475.0
"""


# def computepay(
#     rate: float,
#     hours: float,
#     overtime_mark: float = 40.0,
#     overtime_multiplier: float = 1.5,
# ):
#     pay = 0.0

#     if hours <= overtime_mark:
#         pay = hours * rate
#     elif hours > overtime_mark:
#         overtime_hours = hours - overtime_mark
#         overtime_rate = rate * overtime_multiplier
#         pay = (overtime_mark * rate) + (overtime_hours * overtime_rate)

#     return pay


# while True:
#     try:
#         hours = float(input("Enter Hours: "))
#         rate = float(input("Enter Rate: "))
#         pay = computepay(rate=rate, hours=hours)
#         print(f"Pay: {pay}")
#         break
#     except ValueError:
#         print("Kindly input a number")
#         continue

"""
    Exercise 2
    Write a program to prompt for a score between 0.0 and 1.0.
    If the score is out of range, print an error message. If the score is
    between 0.0 and 1.0, print a grade using the following table:

    Score Grade
    >= 0.9 A
    >= 0.8 B
    >= 0.7 C
    >= 0.6 D
    < 0.6 F
"""


# def grade(score: float):
#     if score < 0.0 or score > 1.0:
#         raise ValueError
#     if score < 0.6:
#         return "F"
#     if score < 0.7:
#         return "D"
#     if score < 0.8:
#         return "C"
#     if score < 0.9:
#         return "B"
#     if score <= 1.0:
#         return "A"


# while True:
#     try:
#         score = float(input("Kindly input your score: "))
#         print(f"Your grade is: '{grade(score)}'")
#         break
#     except ValueError:
#         print("Kindly input a score between 0.0 and 1.0")
#         continue

# def calculate_grade(score_input: float) -> str:
#     """
#     Calculate the grade for a given score.
#     """
#     # Define the grade boundaries
#     grade_boundaries = {
#         0.0: "F",
#         0.6: "D",
#         0.7: "C",
#         0.8: "B",
#         0.9: "A"
#     }

#     # Check if the score is valid
#     if score_input < 0.0 or score_input > 1.0:
#         raise ValueError("Score must be between 0.0 and 1.0.")

#     # Determine the grade based on the score
#     for boundary, grade in grade_boundaries.items():
#         if score_input < boundary:
#             return grade

#     # If the score is greater than or equal to 1.0, return "A"
#     return "A"


# while True:
#     try:
#         score_input = float(input("Please enter your score: "))
#         score = round(score_input, 1)
#         grade = calculate_grade(score)
#         print(f"Your grade is: '{grade}'")
#         break
#     except ValueError as e:
#         print(e)
#         continue


# def get_feelings(greeting: str) -> None:
#     print(greeting)
#     user_feeling = input("How are you feeling? ")
#     print(f"I'm happy to hear that you are feeling {user_feeling}.")


# all_greetings = ["Good morning!", "Good afternoon!", "Good evening!"]
# for greeting in all_greetings:
#     get_feelings(greeting)


# for greeting in ["Good morning!", "Good afternoon!", "Good evening!"]:
#     print(greeting)
#     feeling = input("How are you feeling? ")
#     print(f"I'm happy to hear that you are feeling {feeling}.")


"""
    Loops!
"""
# from statistics import mean

# numbers = []
# while True:
#     try:
#         number = input("Enter a number: ")
#         if number == "done":
#             print(f"The total is: {sum(numbers)}")
#             print(f"The count is: {len(numbers)}")
#             print(f"The average is: {mean(numbers)}")
#             break
#         else:
#             numbers.append(int(number))
#     except ValueError:
#         print("Invalid Input")
