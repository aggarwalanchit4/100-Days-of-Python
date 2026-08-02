
# -----------------------------------------
# Challenge 1 — Duck Typing
# -----------------------------------------

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def animal_sound(animal):
    animal.speak()

dog1 = Dog()
cat1 = Cat()

animal_sound(dog1)
animal_sound(cat1)