from project.animal import Animal
from project.worker import Worker
from typing import List

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > 0:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                self.__animal_capacity -= 1
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return f"Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        d = next((worker for worker in self.workers if worker.name == worker_name), None)
        if d is not None:
            self.workers.remove(d)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = 0
        for a in self.workers:
            sum_salaries += a.salary
        if sum_salaries < self.__budget:
            self.__budget -= sum_salaries
            left_budget = self.__budget
            return f"You payed your workers. They are happy. Budget left: {left_budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_care = 0
        for a in self.animals:
            sum_care += a.money_for_care
        if sum_care < self.__budget:
            self.__budget -= sum_care
            left_budget = self.__budget
            return f"You tended all the animals. They are happy. Budget left: {left_budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal))
            else:
                cheetahs.append(repr(animal))
        result = [f'You have {len(self.animals)} animals', f'----- {len(lions)} Lions:']
        result.extend(lions)
        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(tigers)
        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(cheetahs)
        return "\n".join(result)

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(repr(worker))
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(repr(worker))
            else:
                vets.append(repr(worker))
        result = [f'You have {len(self.workers)} workers', f'----- {len(keepers)} Keepers:']
        result.extend(keepers)
        result.append(f'----- {len(caretakers)} Caretakers:')
        result.extend(caretakers)
        result.append(f'----- {len(vets)} Vets:')
        result.extend(vets)
        return "\n".join(result)

