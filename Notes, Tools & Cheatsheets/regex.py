import re

"""findall 	Returns a list containing all matches
search 	Returns a Match object if there is a match anywhere in the string
split 	Returns a list where the string has been split at each match
sub 	Replaces one or many matches with a string """


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


s = "This is a demo."

match = re.search(r"demo", s)

print("Start Index:", match.start())  # type:ignore
print("End Index:", match.end())  # type:ignore


s = "Hi.Hi again"

# without using \
match = re.search(r".", s)
print(match)

# using \
match = re.search(r"\.", s)
print(match)


# \d is equivalent to [0-9].
p = re.compile(r"\d")
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# to find negative numbers
p = re.compile(r"-*\d+")

# \d+ will match a group on [0-9], group
# of one or greater size
p = re.compile(r"\d+")
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))


# \w is equivalent to [a-zA-Z0-9_].
p = re.compile(r"\w")
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile(r"\w+")
print(
    p.findall(
        "I went to him at 11 A.M., he \
said *** in some_language."
    )
)

# \W matches to non alphanumeric characters.
p = re.compile(r"\W")
print(p.findall("he said *** in some_language."))


# '*' replaces the no. of occurrence
# of a character.
p = re.compile(r"ab*")
print(p.findall("ababbaabbb"))


txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)


txt = "The rain in Spain"
x = re.split(r"\s", txt, 1)
print(x)


# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(re.split(r"\W+", "Words, words , Words"))
print(re.split(r"\W+", "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(re.split(r"\W+", "On 12th Jan 2016, at 11:02 AM"))

# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(re.split(r"\d+", "On 12th Jan 2016, at 11:02 AM"))


# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split(r"\d+", "On 12th Jan 2016, at 11:02 AM", 1))

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split(r"[a-f]+", "Aey, Boy oh boy, come here", flags=re.IGNORECASE))
print(re.split(r"[a-f]+", "Aey, Boy oh boy, come here"))


txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
print(x)


txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt, 2)
print(x)


# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
print(
    re.sub(
        r"ub",
        "~*",
        "Subject has Uber booked already",
        flags=re.IGNORECASE,
    )
)

# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be replaced.
print(re.sub(r"ub", "~*", "Subject has Uber booked already"))

# As count has been given value 1, the maximum
# times replacement occurs is 1
print(
    re.sub(
        r"ub",
        "~*",
        "Subject has Uber booked already",
        count=1,
        flags=re.IGNORECASE,
    )
)

# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r"\sAND\s", " & ", "Baked Beans And Spam", flags=re.IGNORECASE))


print(re.subn("ub", "~*", "Subject has Uber booked already"))

t = re.subn("ub", "~*", "Subject has Uber booked already", flags=re.IGNORECASE)
print(t)
print(len(t))

# This will give same output as sub() would have
print(t[0])


# escape() returns a string with BackSlash '\',
# before every Non-Alphanumeric Character
# In 1st case only ' ', is not alphanumeric
# In 2nd case, ' ', caret '^', '-', '[]', '\'
# are not alphanumeric
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))


txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())  # type:ignore


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)  # type:ignore


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())  # type:ignore


text = "The price of this item is $100."
print(re.findall(r"\$\d+", text))


# compile function


pattern = re.compile(r"\d+")

print(pattern.findall("This is a string with 123 numbers."))


pattern = r"\d+"

text = "This is a string with 123 numbers."

print(re.findall(pattern, text))


pattern = re.compile(r"^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern.search("smth@mail.com"))
