# Day 18 — Encapsulation in Python

## 📚 Topics Covered

- Public Attributes
- Protected Attributes
- Private Attributes
- Getter Methods
- Setter Methods
- Property Decorator (@property)

---

## 📖 Concepts Learned

### 1. Public Attributes
- Accessible from anywhere.
- Can be modified directly.

Example:
```python
self.price = price
```

---

### 2. Protected Attributes
- Uses a single underscore (`_`).
- Indicates that the attribute is intended for internal use.
- Can still be accessed from outside.

Example:
```python
self._price = price
```

---

### 3. Private Attributes
- Uses double underscores (`__`).
- Cannot be accessed directly from outside the class.

Example:
```python
self.__price = price
```

---

### 4. Getter Methods
- Used to read private attributes.

Example:
```python
product.get_price()
```

---

### 5. Setter Methods
- Used to modify private attributes.
- Can include validation before updating data.

Example:
```python
product.set_price(2000)
```

---

### 6. Property Decorator
- Pythonic way of implementing getters and setters.
- Allows attribute-like access while keeping data protected.

Example:
```python
product.price
product.price = 2500
```

---

## 📂 Files

- public_attributes.py
- protected_attributes.py
- private_attributes.py
- getters_setters.py
- property_decorator.py
- challenge.py
- mini_project.py

---

## 🎯 Learning Outcome

After completing Day 18, I can:

- Create public, protected and private attributes.
- Use getter and setter methods.
- Understand why encapsulation is important.
- Use @property to simplify getter and setter implementations.

---

## 🚀 Next Topic

➡️ Day 19 — Polymorphism