# Day 17 — Inheritance and Method Overriding in Python

## 📚 Topics Covered

- Inheritance
- Single Inheritance
- Method Overriding
- super() Function
- Constructor Inheritance
- Parent and Child Classes

---

## 📖 Concepts Learned

### 1. Inheritance

Inheritance allows a child class to acquire the properties and methods of a parent class, promoting code reusability.

Example:

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

---

### 2. Single Inheritance

A child class inherits from one parent class.

Example:

```python
class Vehicle:
    pass

class Car(Vehicle):
    pass
```

---

### 3. Method Overriding

A child class provides its own implementation of a method already defined in the parent class.

Example:

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
```

---

### 4. super() Function

The `super()` function is used to call methods or constructors of the parent class.

Example:

```python
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
```

---

### 5. Constructor Inheritance

A child class can reuse the parent's constructor using `super()` and add its own attributes.

Example:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
```

---

## 📂 Files

- inheritance_basics.py
- method_overriding.py
- super_function.py
- constructor_inheritance.py
- challenge.py
- mini_project.py

---

## 💻 Mini Project

### Vehicle Management System

Implemented:

- Parent class: `Vehicle`
- Child classes:
  - `Car`
  - `Bike`

Concepts used:

- Inheritance
- Method Overriding
- Constructors
- `super()`
- User Input
- Object Creation

---

## 🎯 Learning Outcome

After completing Day 17, I can:

- Create parent and child classes.
- Reuse code using inheritance.
- Override parent class methods.
- Use `super()` to access parent constructors and methods.
- Build simple OOP applications using inheritance.

---

## 🚀 Next Topic

➡️ Day 18 — Encapsulation`