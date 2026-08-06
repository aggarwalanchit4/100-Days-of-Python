# -----------------------------------------
# Challenge 1 – Vehicle Abstraction
# -----------------------------------------

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


class Bike(Vehicle):

    def start(self):
        print("Bike Started")


car = Car()
bike = Bike()

car.start()
bike.start()

# -----------------------------------------
# Challenge 2 – Animal Abstraction
# -----------------------------------------

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()