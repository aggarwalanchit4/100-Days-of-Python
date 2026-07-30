# -----------------------------------------
# Challenge 1 — Private Product
# -----------------------------------------

class Product:
    def __init__(self , name , price):
        self.name = name
        self.__price = price
    def display(self):
        print(f"PRODUCT : {self.name} ")
        print(f"PRICE : {self.__price}")

product = input("Enter name of product: ")
price = int(input(f"Enter price of {product}: "))

product1 = Product(product, price)

product1.display()
print(product1.__price)