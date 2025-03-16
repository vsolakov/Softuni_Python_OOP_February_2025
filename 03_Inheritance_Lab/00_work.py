# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         return "eating"
#
#
# class Teacher(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
#
# t = Teacher("test", 40, 2000)
# print(t.eat())


class Person:
    def __init__(self, first_name, last_name):
        if len(first_name) < 2:
            raise ValueError("Person can not be instantiated with name less than 2 chars")
        self.first_name = first_name
        self.last_name = last_name


    def greet(self):
        return f'{self.first_name} {self.last_name}'

class Student(Person):
    def __init__(self, first_name, last_name, fac_number):
        super().__init__(first_name, last_name)
        self.fac_number = fac_number

    def greet(self):
        return super().greet() + f' {self.fac_number}'


s = Student("Test", "Testov", 123)
print(s.greet())


class Food:
    def __init__(self, food_type, exp_date):
        self.food_type = food_type
        self.exp_date = exp_date


class Fruit(Food):
    def __init__(self, exp_date):
        super().__init__("fruit", exp_date)

