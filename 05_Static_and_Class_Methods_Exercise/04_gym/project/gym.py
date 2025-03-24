from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan
from typing import List

class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        s = next((s for s in self.subscriptions if s.id == subscription_id), None)
        c = next((c for c in self.customers if s.customer_id == c.id), None)
        t = next((t for t in self.trainers if s.trainer_id == t.id), None)
        ex = next((ex for ex in self.plans if s.exercise_id == ex.id), None)
        eq = next((eq for eq in self.equipment if ex.equipment_id == eq.id), None)
        return f"{s}\n{c}\n{t}\n{eq}\n{ex}"
