from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Dog barks")


dog1 = Dog()
dog1.speak()