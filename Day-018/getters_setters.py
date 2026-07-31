# -----------------------------------------
# Challenge 1 — getter Product
# -----------------------------------------

class Product:
    def __init__(self , name , price):
        self.name = name
        self.__price = price
    def display(self):
        print(f"PRODUCT : {self.name} ")
    def get_price(self):
        return self.__price

product = input("Enter name of product: ")
price = int(input(f"Enter price of {product}: "))

product1 = Product(product, price)

product1.display()
print(product1.get_price())

# -----------------------------------------
# Challenge 2 — setter Product
# -----------------------------------------

class Product:
    def __init__(self , name , price):
        self.name = name
        self.__price = price
    def display(self):
        print(f"PRODUCT : {self.name} ")
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price

product = input("Enter name of product: ")
price = int(input(f"Enter price of {product}: "))

product1 = Product(product, price)

product1.display()
print(product1.get_price())
new_price = int(input("enter new price : "))
product1.set_price(new_price)
print(product1.get_price())