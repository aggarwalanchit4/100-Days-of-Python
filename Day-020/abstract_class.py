# -----------------------------------------
# Day 19 Mini Project — Animal Sound Simulator
# -----------------------------------------

class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("DOG BARK's")
class Cat(Animal):
    def speak(self):
        print("CAT MEOW's")
class Lion(Animal):
    def speak(self):
        print("LION ROAR's")

def animal_sound(animal):
    animal.speak()

animal1 = Animal()
dog1 = Dog()
cat1 = Cat()
lion1 = Lion()


animal_sound(animal1)
animal_sound(dog1)
animal_sound(cat1)
animal_sound(lion1)

