"""
Pydantic Classes
"""
from dataclasses import dataclass
from typing import List, Dict
import json


@dataclass
class Person:
    name: str = "Joe"
    age: int = 30
    height: float = 1.8
    # gender: bool = "Non-Binary"  # This will actually work fine

    def __repr__(self) -> str:
        return f"Cheeky Fella! Class {self.__class__.__name__}"


@dataclass
class People:
    people: List[Person]


# nelson = Person("Nelson Ombuya", 26, 1.75)
# john = Person("John Ombuya", 21, 1.80)
# print(nelson)
# print(john)
# print(Person.gender)
# print(People([nelson, john]))


@dataclass
class Student:
    name: str
    id: int
    grades: List[float]

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


# alice = Student("Alice", 12345, [3.5, 4.0, 3.7])
# print(f"{alice.name}'s average grade is {round(alice.average_grade(), 2)}")


@dataclass
class Book:
    title: str
    author: str
    year: int
    pages: int
    rating: float
    publisher: str
    genres: List[str]

    def has_genre(self, genre: str) -> bool:
        return genre in self.genres

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "pages": self.pages,
            "rating": self.rating,
            "publisher": self.publisher,
            "genres": self.genres,
        }


lord_of_the_rings = Book(
    "Lord of the Rings",
    "That Author Guy",
    2020,
    3000,
    4.75,
    "That Publisher Guy",
    ["Fantasy", "Action", "Drama"],
)

one_piece = Book(
    "One Piece",
    "Oda Something",
    1999,
    1050,
    4.85,
    "Shounen Jump",
    ["Shounen", "Fantasy"],
)
# print(lord_of_the_rings.has_genre("Fantasy"))
# print(lord_of_the_rings.to_dict())
# print(one_piece.has_genre("Seinen"))
# print(one_piece.to_dict())

"""
JSON
"""
a = {"name": "Nelson", "age": 26, "salary": 1000000000}
b = json.dumps(a)  # Converts a Dictionary input to a JSON String output
c = json.loads(b)  # Converts a JSON String Object to a Dictionary

with open("output.json", "w") as json_file:
    json.dump(a, json_file)

with open("output.json", "r") as json_file:
    d = json.load(json_file)


class JSONParser:
    def __init__(self, json_file: str) -> None:
        self.json_file = json_file
        self.json = self.parse_json_file()
        self.students = self.json["students"]
        self.update_students_avg_grade()
        self.class_average = self.get_class_average()
        self.update_students_above_avg_grade()
        self.update_json_file()
        print(self.students)

    def parse_json_file(self):
        with open(self.json_file, "r") as file:
            return json.load(file)

    def average_grade(self, student: Dict):
        avg_grade = sum(student["grades"]) / len(student["grades"])
        return {"avg_grade": avg_grade}

    def update_students_avg_grade(self):
        return [
            student.update(self.average_grade(student))
            for student in self.students  # ignore
        ]

    def get_class_average(self):
        return sum(student["avg_grade"] for student in self.students) / len(
            self.students
        )

    def above_average_grade(self, student: Dict):
        return {"above_avg": student["avg_grade"] > self.class_average}

    def update_students_above_avg_grade(self):
        return [
            student.update(self.above_average_grade(student))
            for student in self.students
        ]

    def update_json_file(self):
        with open(self.json_file, "w") as file:
            json_dict = {"students": self.students}
            json.dump(json_dict, file)


JSONParser("students.json")
