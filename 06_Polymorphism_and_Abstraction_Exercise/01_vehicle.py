from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    additional_fuel = 0.9
    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + self.additional_fuel) * distance:
            self.fuel_quantity -= (self.fuel_consumption + self.additional_fuel) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    additional_fuel = 1.6
    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + self.additional_fuel) * distance:
            self.fuel_quantity -= (self.fuel_consumption + self.additional_fuel) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95