# -----------------------------------------
# Challenge 1 — Polymorphism with Inheritance
# -----------------------------------------

class Animal :
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("DOG BARK'S")
class Cow(Animal):
    def speak(self):
        print("COW MOO'S")
class Cat(Animal):
    def speak(self):
        print("CAT MEOW's")

animal1 = Animal()
dog1 = Dog()
cat1 = Cat()
cow1 = Cow()
animal1.speak()
dog1.speak()
cat1.speak()
cow1.speak()