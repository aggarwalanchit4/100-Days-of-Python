# -----------------------------------------
# Challenge 1 – Implement Abstraction using ABC
# -----------------------------------------

from abc import ABC , abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    
class Car(Vehicle):
    def __init__(self , name):
           self.name = name
   
    def start(self):
        print("Car Started")
        print(f"Car Name : {self.name}")

name = input("enter car name : ")
Car1 = Car(name)
Car1.start()

# -----------------------------------------
# Challenge 2 – Multiple Vehicle Types using Abstraction
# -----------------------------------------

from abc import ABC , abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    
class Car(Vehicle):
    def __init__(self , name):
           self.name = name
   
    def start(self):
        print("Car Started")
        print(f"Car Name : {self.name}")

class Bike(Vehicle):
    def __init__(self , name):
                self.name = name
        
    def start(self):
        print("Bike Started")
        print(f"Bike Name : {self.name}")

car_name = input("enter car name : ")
bike_name = input("enter bike name :")
Car1 = Car(car_name)
Bike1 = Bike(bike_name)
Car1.start()
Bike1.start()