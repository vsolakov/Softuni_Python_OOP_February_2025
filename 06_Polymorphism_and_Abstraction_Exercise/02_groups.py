from typing import List

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        if isinstance(other, Person):
            return Person(self.name, other.surname)
        raise TypeError("Can only concatenate Person instances")


class Group:
    def __init__(self, name, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f'{self.name} {other.name}', self.people + other.people)


    def __str__(self):
        return f"Group {self.name} with members {', '.join(str(s) for s in self.people)}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"

