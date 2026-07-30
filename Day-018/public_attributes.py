# -----------------------------------------
# Challenge 1 — Public Product
# -----------------------------------------

class Product:
    def __init__(self , name , price):
        self.name = name
        self.price = price
    def display(self):
        print(f"PRODUCT : {self.name} ")
        print(f"PRICE : {self.price}")

product = input("Enter name of product: ")
price = int(input(f"Enter price of {product}: "))

product1 = Product(product, price)

product1.display()

new_price = int(input(f"Enter new price of {product}: "))

product1.price = new_price

product1.display()