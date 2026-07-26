 # -----------------------------------------
# Challenge 1 — Student Class
# -----------------------------------------

class student :
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def display(self) :
        print(f"Name of student is {self.name}")
        print(f"Marks of {self.name} are : {self.marks}")

        
name1 = input("enter name of student : ")
marks1 = int(input("enter marks of student: "))

name2 = input("enter name of student : ")
marks2 = int(input("enter marks of student: "))

student1 = student(name1 , marks1)
student2 = student(name2 , marks2)
student1.display()
student2.display()

# -----------------------------------------
# Challenge 2 — Product Class
# -----------------------------------------

class product :
    def __init__(self  , name , price , quantity):
        self.name = name
        self.price = price 
        self.quantity = quantity
    def total_price(self):
        return self.price*self.quantity


name = input("enter name of product : ")
price = int(input(f"enter price of one {name} : "))
quantity = int(input(f"enter quantity of {name}: "))
product1 = product(name , price , quantity)
print(f"Total price of {quantity} {name} is {product1.total_price()}")

# -----------------------------------------
# Challenge 3 — Modify Object Data
# -----------------------------------------

class player :
    def __init__(self , name , score):
        self.name = name
        self.score = score

    def display(self):
        print(f"Name of player is {self.name}")
        print(f"Score of {self.name} is {self.score}")
    
    def points_scored(self , points ):
        self.score = self.score + points

name = input("enter name of player : ")
score = int(input(f"enter score of {name} : "))
points = int(input(f"enter points earned by {name} :"))
player1 = player(name , score)
player1.points_scored(points)
player1.display()