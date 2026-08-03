
# -----------------------------------------
# Challenge 1 — Basic Polymorphism
# -----------------------------------------

class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


class Cow:
    def speak(self):
        print("Moo")

dog1 = Dog()
cat1 = Cat()
cow1 = Cow()
dog1.speak()
cat1.speak()
cow1.speak()
