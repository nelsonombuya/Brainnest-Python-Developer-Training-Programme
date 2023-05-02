class MyClass:  # type:ignore
    x = 5


print(MyClass)


class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:  # type:ignore
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:  # type:ignore
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


class Person:  # type:ignore
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


class Person:  # type:ignore
    def __init__(mysillyobject, name, age):  # type:ignore
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):  # type:ignore
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
# p1.name = "Mike"
# del p1.name
p1.myfunc()


# inheritance (parent = based, child = derived)
class Person:  # type:ignore
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):  # type:ignore
    pass


x = Student("Mike", "Olsen")
x.printname()


class Person:  # type:ignore
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):  # type:ignore
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)  # type:ignore


x = Student("Mike", "Olsen")
x.printname()


class Person:  # type:ignore
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear,
        )


x = Student("Mike", "Olsen", 2019)
x.welcome()
