# Day 19 — Polymorphism in Python

## 📚 Topics Covered

- Basic Polymorphism
- Method Overriding
- Duck Typing
- Built-in Polymorphism
- Polymorphism using Inheritance

---

## 📖 Concepts Learned

### 1. Basic Polymorphism

Same method name behaves differently for different objects.

Example:

```python
dog.speak()
cat.speak()
cow.speak()
```

---

### 2. Method Overriding

Child classes override parent class methods to provide their own implementation.

Example:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bark")
```

---

### 3. Duck Typing

Python focuses on an object's behavior rather than its type.

"If it behaves like a duck, treat it like a duck."

Example:

```python
def animal_sound(animal):
    animal.speak()
```

---

### 4. Built-in Polymorphism

Python's built-in functions and operators work with multiple data types.

Examples:

```python
len("Python")
len([1,2,3])
len((1,2))
```

```python
10 + 20
"Hello" + "World"
[1,2] + [3,4]
```

---

### 5. Polymorphism with Inheritance

Different child classes override the same parent method.

Example:

```python
Animal
│
├── Dog
├── Cat
├── Cow
└── Lion
```

Each class implements:

```python
speak()
```

differently.

---

## 📂 Files

- basic_polymorphism.py
- method_overriding_polymorphism.py
- duck_typing.py
- builtin_polymorphism.py
- polymorphism_with_inheritance.py
- challenge.py
- mini_project.py

---

## 🎯 Learning Outcome

After completing Day 19, I can:

- Understand the concept of polymorphism.
- Implement method overriding.
- Apply duck typing in Python.
- Recognize built-in polymorphism.
- Build polymorphic applications using inheritance.

---

## 🚀 Next Topic

➡️ Day 20 — Abstraction