# -----------------------------------------
# Day 18 — Property Decorator
# -----------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price")


product = input("Enter product name: ")
price = int(input(f"Enter price of {product}: "))

product1 = Product(product, price)

print(f"Product: {product1.name}")
print(f"Current price: {product1.price}")

new_price = int(input("Enter new price: "))

product1.price = new_price

print(f"Updated price: {product1.price}")