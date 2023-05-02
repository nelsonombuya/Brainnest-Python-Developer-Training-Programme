from functools import reduce

"""
Classes 😲
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    """
    The string method is useful for printing the properties of a class at a
    glance
    """

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."


# person = Person("Nelson Ombuya", 26)
# print(person)
# print(person.name)
# print(person.age)

# person.name = "Mike"
# print(person)

# try:
#     del person.name
#     print(person)  # Will raise an error
# except Exception:
#     print("The name hasn't been set")


"""
Inheritance 😳
"""


class Student(Person):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        height: float,
        gender: bool = True,
    ) -> None:
        Person.__init__(self, name=f"{first_name} {last_name}", age=age)
        self.height = height
        self.gender = "He" if gender else "She"

    def __str__(self) -> str:
        return f"{super().__str__()} {self.gender} is {self.height}cm tall."


# student = Student("Mike", "Olsen", 3000, 175.0)
# bestie = Student("Tracy", "Wanjiku", 19, 152.0, False)
# print(student)
# print(bestie)


"""
Exercise 1
1.Create a Dog class with the following attributes: name, breed, and age.
The class should also have the following methods: bark() and info().
"""


class Dog:
    def __init__(self, name: str, breed: str, age: int) -> None:
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("WOOF")

    def info(self):
        print(
            f"This dog's name is {self.name}."
            f" Their breed is {self.breed}"
            f" and they are {self.age} years old."
        )


# charlie = Dog("Charlie", "German Shepherd", 2)
# charlie.info()
# charlie.bark()

"""
Exercise 2
"""


class BankAccount:
    def __init__(self, balance: float, account_no: int) -> None:
        self.balance = balance
        self.account_no = account_no

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Your new balance is :{self.balance}")
        else:
            print("You can't deposit a negative amount")

    def withdraw(self, amount: float):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            print(f"Your new balance is :{self.balance}")
        elif amount > self.balance:
            print(f"You have insufficient funds: {self.balance}")
        else:
            print("You can't withdraw a negative amount")

    def info(self):
        print(f"Bank Account No: '{self.account_no}'. Balance: {self.balance}")


# my_account = BankAccount(0, 1234)
# my_account.deposit(10000)
# my_account.withdraw(2000)
# my_account.withdraw(10000)
# my_account.info()


class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.status = False  # The car is off by default

    def start(self) -> None:
        self.status = True
        self.info()

    def stop(self) -> None:
        self.status = False
        self.info()

    def info(self) -> None:
        status = "on" if self.status else "off"
        print(
            f"This vehicle is a {self.year} {self.make} {self.model} ."
            f"It is currently {status}"
        )


class Car(Vehicle):
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        num_doors: int,
    ) -> None:
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.doors_locked = False  # The car's doors are unlocked by default

    def info(self) -> None:
        status = "on" if self.status else "off"
        doors = "locked" if self.doors_locked else "unlocked"
        print(
            f"This vehicle is a {self.year} {self.make} {self.model}."
            f"It is currently {status} and it's {self.num_doors} doors are "
            f"{doors}"
        )

    def lock_doors(self) -> None:
        self.doors_locked = True
        self.info()


# mclaren = Car("McLaren", "Speedtail", 2020, 2)
# mclaren.info()
# mclaren.start()
# mclaren.stop()
# mclaren.lock_doors()


"""
Sets
Similar to tuples but are mutable
"""
fruits = {"Apples", "Oranges", "Bananas"}
print("Bananas" in fruits)
fruits.add("Grapes")
fruits.update(["Kiwi", "Strawberries"])
fruits.remove("Bananas")  # Raises exception if item is not in the set
fruits.discard("Bananas")  # No exception if the item is not in the set
fruits.pop()  # Removes a random element from the set
fruits.clear()  # Clears the set
del fruits

letters = {"a", "b", "c"}
numbers = {1, 2, 3}
alphanumeric = letters.union(numbers)
alphanumeric.update(numbers)

"""
Lambda Functions
lambda arguments: expression
"""


l_function = lambda a: a + 10
l_function2 = lambda a, b: a + b
# print(l_function(5))
# print(l_function2(5, 10))


def factor(n):
    return lambda a: a * n


factor_of_two = factor(2)
factor_of_three = factor(3)
# print(factor_of_two(13))
# print(factor_of_three(13))


def reverse_upper():
    return lambda string: string.upper()[::-1]


rev_up = reverse_upper()
# print(rev_up("Wack!"))

is_even_list = [(lambda arg=x: x if arg % 2 == 0 else None)() for x in range(1, 10)]
# print(is_even_list)

ages = [12, 13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
# print(adults)
adults = list(map(lambda age: age > 18, ages))
# print(adults)


summed_ages = reduce((lambda x, y: x + y), ages)
# print(summed_ages)

string_list = ["a", "b", "c", "d", "e"]
uppercase_list = [(lambda arg=string: arg.upper())() for string in string_list]
print(uppercase_list)

to_upper = lambda string_list: [string.upper() for string in string_list]
# print(to_upper(["a", "b", "c", "d", "e"]))


get_max = lambda nl1, nl2: [max(nl1[i], nl2[i]) for i in range(len(nl2))]

print(get_max([1, 3, 5], [2, 4, 6]))
