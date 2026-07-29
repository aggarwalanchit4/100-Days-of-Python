# -----------------------------------------
# Day 17 Mini Project — Vehicle Management System
# -----------------------------------------

class Vehicle:
    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model 
        self.price = price 
    def display(self):
        print(f"BRAND : {self.brand}")
        print(f"MODEL : {self.model}")
        print(f"PRICE : {self.price}")

class Car(Vehicle):
    def __init__(self, brand, model, price , fuel_type , doors):
        super().__init__(brand, model, price)
        self.fuel_type = fuel_type
        self.doors = doors
    def display(self):
        super().display()
        print(f"FUEL TYPE : {self.fuel_type}")
        print(f"NUMBER OF DOORS : {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, model, price , Bike_type , Engine_cc):
        super().__init__(brand, model, price)
        self.Bike_type = Bike_type
        self.Engine_cc = Engine_cc
    def display(self):
        super().display()
        print(f"ENGINE CC : {self.Engine_cc}")
        print(f"BIKE TYPE : {self.Bike_type}")

brand_car = input("Enter brand name of car : ")
model_car = input("Enter model name of car : ")
price_car = int(input("enter price of car : "))
engine_car = input("enter car type : ") 
doors = int(input("enter number of doors in  car : "))

brand_bike = input("Enter brand name of bike : ")
model_bike = input("Enter model name of bike : ")
price_bike = int(input("enter price of bike : "))
engine_bike = int(input("enter engine CC of bike : "))
type_bike = (input("enter type of bike : "))

car1 = Car(brand_car , model_car , price_car , engine_car , doors)
bike1 = Bike(brand_bike , model_bike , price_bike , type_bike , engine_bike)
car1.display()
bike1.display()



