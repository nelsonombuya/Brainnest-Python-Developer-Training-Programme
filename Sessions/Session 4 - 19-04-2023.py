"""
Using re
"""

# import re

txt = "The rain in Spain in 1946 caused temperatures of -3 degrees. I'm Sane"
# print(re.search("ai", txt))
# print(re.search("xyz", txt))

# match = re.search("rain", txt)
# print(f"Starting Index: {match.start()}")  # type:ignore
# print(f"Starting Index: {match.end()}")  # type:ignore

# # In regex '.' stands for any character
# print(re.search(".", txt))
# print(re.search(r"\.", txt))  # Use r when escaping a regex special character

"""
What's the difference between re.search and re.compile in python

In Python's re module, re.search() and re.compile() are both used for searching
for patterns in strings, but they differ in their functionality.

re.search() is a function that searches a string for a specified pattern and
returns a match object if there is a match. It takes two arguments: the regular
expression pattern to search for, and the string to search in. For example, the
following code searches for the word "hello" in a string:

import re

string = "Hello, world!"
pattern = "hello"

match = re.search(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")
The output of this code will be "Match found: Hello", since the re.search()
function is case-sensitive and the pattern "hello" doesn't match "Hello".

re.compile() is a function that compiles a regular expression pattern into a
regular expression object. This object can then be used to search for the
pattern in strings using the search(), findall(), and other functions. By
compiling the regular expression pattern, you can improve the efficiency of
your code if you need to search for the same pattern multiple times.

For example, the following code compiles a regular expression pattern to search
for email addresses and then uses it to search for email addresses in two
different strings:

import re

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex = re.compile(pattern)

string1 = "Contact us at info@example.com"
string2 = "Send an email to support@example.org"

match1 = regex.search(string1)
match2 = regex.search(string2)

if match1:
    print("Email address found in string 1:", match1.group())
else:
    print("No email address found in string 1")

if match2:
    print("Email address found in string 2:", match2.group())
else:
    print("No email address found in string 2")
The output of this code will be:

typescript
Email address found in string 1: info@example.com
Email address found in string 2: support@example.org
In summary, re.search() is used to search for a pattern in a string and returns
a match object, while re.compile() is used to compile a regular expression
pattern into a regular expression object that can be used to search for the
pattern in multiple strings.
"""
# # \d is equivalent to the whole numbers [0-9]
# p = re.compile(r"\d+")  # Checks for digits (outputs the absolute digit)
# print(p.findall(txt))

# p = re.compile(r"-*\d+")  # Checks for negative digits as well
# print(p.findall(txt))

# # \w is equivalent to [a-zA-Z0-9_]
# p = re.compile(r"\w")
# print(p.findall(txt))

# # \W returns all of the special characters
# p = re.compile(r"\W")
# print(p.findall(txt))

# # Test
# p = re.compile(r"ab*")
# print(p.findall("abababbababaababbb"))

"""
Split function in regex
It splits the string into an array using the regex as the separator
It returns the array of the string after removing the characters that match the
regex
"""
# \s is used to search for spaces
# print(re.split(r"\s", txt))
# print(re.split(r"\s", txt, 1))  # Splits it only on the first instance
# print(re.split("[a-f]", "Aey, Boy oh boy, come here!", flags=re.IGNORECASE))
# print(re.split("[a-f]+", "Aey, Boy oh boy, come here!", flags=re.IGNORECASE))

"""
Substitute
Used to substitute the strings that match the regex
"""
# print(re.sub(r"\sAND\s", " & ", "Baked Beans And Spam", flags=re.IGNORECASE))

"""
Subn
Similar to substitute, but also returns the frequency of the substitutions in a
tuple
"""
# print(
#   re.subn(r"\sAND\s", " & ", "Baked Beans And Spam", flags=re.IGNORECASE)
# )

"""
Escape Function
Puts a backslash before special characters.
This includes whitespaces
"""
# print(re.escape("This is awesome even 1 AM!"))

# Checks for the substring that starts with "S" and continues with alphanumeric
# Characters, then prints the word that matches this
# print(re.search(r"\bS\w+", txt).group())  # type:ignore

# Gets the placing of the substring
# print(re.search(r"\bS\w+", txt).span())  # type:ignore

# Checks if the whole string starts with "S" and continues with alphanumeric
# Characters, then prints the word that matches this
# print(re.search(r"^S\w+", f"S{txt}").group())  # type:ignore

# Checking for email addresses
# pattern = r"^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2-4}$"
# pattern = re.compile(pattern)
# print(pattern.search("info-wow@example.com"))
# print(pattern.search("info@@example.com"))
# print(pattern.search("info@example..com"))
# print(pattern.search("info@example.comm"))


"""
Exercise 1
1. Given a text string that contains phone numbers in the format of
(XXX) XXX-XXXX, write a regular expression to extract all the phone numbers
from the string.
"""


# def get_phone_nums(string: str):
#     pattern = re.compile(r"\(\d{3}\) \d{3}-\d{4}")
#     return pattern.findall(string)


# test = (
#     "Here are some phone numbers: "
#     "(123) 456-7890, "
#     "(555) 555-1212, "
#     "and (999) 123-4567."
# )
# print(get_phone_nums(test))


"""
Exercise 2
1. Given a text string that contains urls in the format
"https://www.google.com"
"""


# def get_urls(string: str):
#     pattern = re.compile(r"https?://\S+\.\S+")
#     urls = pattern.findall(string)
#     urls = [url.rstrip(".,!?:") for url in urls]
#     return urls


# test = (
#     "Here are some URLs: "
#     "https://www.google.com, "
#     "http://www.example.com, "
#     "http://www.yahoo.com, "
#     "https://www.example.co.uk, "
#     "and https://www.python.org."
# )
# print(get_urls(test))


"""
Exercise 3
"""


# def get_num_words(string: str):
#     pattern = re.compile(r"\w+")
#     words = pattern.findall(string)
#     return len(words)


# test = "Here are some words"
# print(get_num_words(test))


# """
# Tuples
# Are immutable
# They behave like mathematical variables
# """
# fruits = ("apples", "oranges")
# # This will create a new tuple in memory
# # /= and -= are not supported
# fruits += fruits
# fruits *= 2


"""
Exercise 4
"""


# def flatten_list(nested_list: list):
#     return [
#       nested_element
#       for element in nested_list
#       for nested_element in element
#     ]


# print(flatten_list([[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]]))


def generate_prime(n: int = 100):
    return [
        num
        for num in range(2, n + 1)
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    ]

    # for number in range(2, n + 1):
    #     is_prime = True
    #     for i in range(2, int(number**0.5) + 1):
    #         if number % i == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         prime_number_list.append(number)
    # return prime_number_list


# def generate_prime(n: int):
#     return [
#         number
#         for number in range(2, n + 1)
#         if all(number % i != 0 for i in range(2, int(number**0.5) + 1))
#     ]

print(generate_prime())
