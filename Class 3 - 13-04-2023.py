"""
For Loops
"""
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

"""
When dealing with ranges, the first number is included, but the last number
isn't included. This means that it counts from zero to n-1
"""
# for x in range(10):
#     print(x)

# for x in range(1, 10, 2):
#     print(x)

# adjectives = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for adjective in adjectives:
#     for fruit in fruits:
#         print(adjective, fruit)

# count = 0
# count_v = 0
# for number in [3, 41, 12, 9, 74, 15]:
#     count += 1
#     count_v += number

# print(count)
# print(count_v)

"""
Exercise 1
Create a for loop that iterates through a list of numbers and prints the square
of each number
"""
# import random

# numbers = []
# for i in range(5):
#     numbers.append(random.randint(1, 20))

# for number in numbers:
#     print(f"{number}^2 = {number ** 2}")

# import random

# numbers = [random.randint(1, 20) for number in range(10)]
# print("\n".join([f"{number}^2 = {number ** 2}" for number in numbers]))


"""
Exercise 2
"""


# def generate_prime(n: int):
#     if n <= 1:
#         raise ValueError

#     prime_number_list = []
#     for number in range(2, n + 1):
#         is_prime = True
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_number_list.append(number)
#     return prime_number_list


# try:
#     number = int(input("Kindly input a whole number: "))
#     prime_numbers = generate_prime(number)
#     print(f"The list of prime numbers below '{number}' is {prime_numbers}")
# except ValueError:
#     print("Kindly input a whole number that's greater than 1")


"""
File Handling 😃
"""
# file = open("hangman.py")
# print(file)
# print(file.read(4))
# print(file.readline())  # Returns only the first line
# print(file.readline())  # Returns the next line
# print(file.readline())  # Returns the line after that
# print(file.readline())  # Returns the line after that
# print(file.readline())  # Returns the line after that
# # If we exceed the lines, it returns nothing
# print(file.readlines())  # Returns every line in the format of a list
# file.close()  # Close the file after reading

# # a appends the contents to the file
# # w writes/overwrites the file
# f = open("demo_file_2.txt", "a")  # Creates the file if it doesn't exist
# f.write("Writing to a file")
# f.close()

# # Deleting files will require the os library
# import os

# if os.path.exists("file.txt"):  # Check if the path exists
#     os.remove("file.txt")
# else:
#     print("File not found")

# os.mkdir("my_folder")  # Create a directory
# os.rmdir("my_folder")  # Remove a directory
# try:
#     senders = {}
#     with open("mbox-short.txt") as file:
#         for line in file.readlines():
#             try:
#                 line = line.split()
#                 if line[0] == "From":
#                     if line[1] in senders:
#                         senders[line[1]] += 1
#                     else:
#                         senders.update({line[1]: 1})
#             except IndexError:
#                 continue
#     print("\n".join([f"'{sender}' : {c}" for sender, c in senders.items()]))
#     most_emails = max(senders, key=lambda c: senders[c])
#     print(
#         f"The sender with the most emails is : '{most_emails}'"
#         + f" with {senders[most_emails]} emails"
#     )
# except FileNotFoundError:
#     print("File Not Found")

# try:
#     senders = {}
#     with open("mbox-short.txt") as file:
#         for line in file.readlines():
#             try:
#                 line = line.split()
#                 if line[0] == "From":
#                     domain = line[1].split("@")[1]
#                     if domain in senders:
#                         senders[domain] += 1
#                     else:
#                         senders.update({domain: 1})
#             except IndexError:
#                 continue
#     print(senders)
# except FileNotFoundError:
#     print("File Not Found")
