# Python Basics

# 1️⃣ What is Python?

Python is a high-level, interpreted programming language designed for simplicity and readability. It was created by **Guido van Rossum** in **1991** and is widely used in various fields like web development, data science, artificial intelligence, automation, and more.

---

## 🔹 Key Features of Python:

- ✔ **Easy to Learn** – Simple and readable syntax
- ✔ **Dynamically Typed** – No need to declare variable types
- ✔ **Interpreted Language** – Code runs line by line (no compilation required)
- ✔ **Cross-platform** – Works on Windows, macOS, and Linux
- ✔ **Extensive Libraries** – NumPy, Pandas, TensorFlow, OpenCV, Pytorch, etc.

# 2️⃣ Why is Python So Popular?

Python is one of the most popular programming languages because of:

---

## 1️⃣ **Readability & Simplicity**

- Its syntax is close to the English language, making it beginner-friendly.

## 2️⃣ **Versatility**

- Used in **Web Development**, **AI**, **Machine Learning**, **Data Science**, **Automation**, **Cybersecurity**, and more.

## 3️⃣ **Large Community Support**

- Python has a huge developer community and many open-source libraries.

## 4️⃣ **Strong Libraries & Frameworks**

- **Django**, **Flask** (Web Development)
- **NumPy**, **Pandas** (Data Science)
- **TensorFlow**, **PyTorch** (AI/ML)

## 5️⃣ **Automation**

- Python is widely used for automating repetitive tasks.

# 3️⃣ Key Differences Between Python and JavaScript

| **Feature**            | **Python 🐍**                                | **JavaScript 🌐**                                          |
| ---------------------- | -------------------------------------------- | ---------------------------------------------------------- |
| **Syntax**             | Simple, easy to read                         | More symbols (`{}`, `;`)                                   |
| **Usage**              | AI, ML, Data Science, Backend                | Web Development (Frontend + Backend)                       |
| **Execution**          | Runs on a server or locally                  | Runs mainly in browsers (but also on servers with Node.js) |
| **Typing**             | Dynamically Typed (No need to declare types) | Also Dynamically Typed but has `var`, `let`, `const`       |
| **Backend Frameworks** | Django, Flask, FastAPI                       | Node.js, Express.js                                        |
| **Frontend Usage**     | Not used for frontend                        | Mainly used for frontend (React, Vue, Angular)             |

---

## 🔥 When to Use Python vs JavaScript?

- **Use Python** for Data Science, Machine Learning, AI, and Backend Development.
- **Use JavaScript** for Frontend Development, Web Applications, and Full-stack projects.

# 4️⃣ How Python Code is Executed? (Interpreted vs Compiled Languages)

---

## 🔹 **Compiled Languages** (C, C++, Java, etc.)

- The entire code is converted into **machine code** before execution.
- Needs a separate compiler (e.g., `gcc` for C, `javac` for Java).
- **Faster execution** but requires compilation every time the code changes.

---

## 🔹 **Interpreted Languages** (Python, JavaScript, PHP, etc.)

- Code is executed **line by line** by an interpreter (e.g., `python` for Python).
- No need for compilation – easier to debug but **slightly slower** than compiled languages.

💡 Python is an interpreted language because it runs code line by line using the Python interpreter

# Python Data Types

Python provides a variety of built-in data types that allow developers to work with different kinds of data. Below is an overview of the main data types in Python:

## **Numeric Types**

1. **int**: Represents integers (e.g., `1`, `42`, `-10`).
2. **float**: Represents floating-point numbers (e.g., `3.14`, `-0.001`).
3. **complex**: Represents complex numbers (e.g., `1+2j`, `-3+4j`).

## **Sequence Types**

1. **list**: An ordered, mutable collection of items (e.g., `[1, 2, 3]`).
2. **tuple**: An ordered, immutable collection of items (e.g., `(1, 2, 3)`).
3. **range**: Represents a sequence of numbers (e.g., `range(0, 10)`).

## **Text Type**

1. **str**: Represents text (e.g., `"Hello, World!"`).

## **Set Types**

1. **set**: An unordered collection of unique items (e.g., `{1, 2, 3}`).
2. **frozenset**: An immutable version of a set.

## **Mapping Type**

1. **dict**: A collection of key-value pairs (e.g., `{"name": "Alice", "age": 25}`).

## **Boolean Type**

1. **bool**: Represents truth values (`True` or `False`).

## **Binary Types**

1. **bytes**: Immutable sequence of bytes (e.g., `b"hello"`).
2. **bytearray**: Mutable sequence of bytes.
3. **memoryview**: Provides memory access to byte data without copying.

## **None Type**

1. **NoneType**: Represents the absence of a value (`None`).

example

```python
def get_amount(prompt):
    try:
        amount = float(input(prompt))
        return amount          # ✅ returns a valid number
    except ValueError:
        print("\n  ❌ Invalid amount. Please enter a number.")
        return None            # ❌ returns None (signals failure)
```

### What is None?

`None` is Python's way of saying "nothing" / "no value" / "empty". It's not zero, not False, not an empty string — it literally means nothing exists here.

```python
x = None
print(x)        # Output: None
print(type(x))  # Output: <class 'NoneType'>
```

### Why return None here?

The function has two possible outcomes:

```
User types "500"  → float("500") works  → return 500    ✅ (a real number)
User types "abc"  → float("abc") crashes → return None  ❌ (signals "it failed")
```

We use return None as a signal/flag to the caller saying — "something went wrong, I have no valid number to give you."

## not keyword

The `not` keyword is used in Python for **logical negation**. It reverses the truth value of a condition or expression.

##### What does not do?

not reverses/flips the truth value of something.

```python
not True → False
not False → True
```

##### What does not transactions mean?

In Python, an empty list [] is considered False, and a list with items is considered True

```python
transactions = []         # Empty list → False
not transactions          # not False  → True  ✅ (enters the if block)

transactions = ["something"]  # Has items → True
not transactions              # not True  → False ❌ (skips the if block)
```

##### You could also write it this way (same meaning):

```python
if len(transactions) == 0:   # longer way
    print("No transactions yet.")

if not transactions:          # shorter, more Pythonic way ✅
    print("No transactions yet.")
```

| **Original Expression** | **Python Translation** | **Reason**        |
| ----------------------- | ---------------------- | ----------------- |
| `x is not None`         | `x is not None`        | Identity operator |
| `x is not True`         | `x is not True`        | Identity operator |
| `x is not False`        | `x is not False`       | Identity operator |
| `x != 0`                | `x != 0`               | Equality operator |
| `x != 1`                | `x != 1`               | Equality operator |
| `""`                    | `""` or `''`           | Empty string      |
| `[]`                    | `[]`                   | Empty list        |
| `{}`                    | `{}`                   | Empty dict        |
| `None`                  | `None`                 | `None` value      |
| `True`                  | `True`                 | `True` boolean    |
| `False`                 | `False`                | `False` boolean   |

# is not None:

`is not None` checks if a value is **not** `None`. It's the Pythonic way to handle cases where a function might return `None` to indicate failure.

```python
amount = get_amount("  Enter deposit amount: $")
if amount is not None:
    deposit(amount)
```

##### Why check is not None?

After calling get_amount(), amount will be one of two things:

```
amount = 500.0   → valid number  → safe to deposit ✅
amount = None    → user typed garbage → DO NOT deposit ❌
```

##### So we check before calling deposit():

```
if amount is not None:
         ↓
Is amount a real number? → Yes → call deposit(amount) ✅
Is amount None?          → No  → skip deposit, do nothing ❌
```

##### Why use is not instead of != None?

```python
if amount is not None:   # ✅ Correct Pythonic way
if amount != None:       # ⚠️  Works but not recommended
```

**`is`** checks for **object identity** (are these the exact same object in memory?).
**`!=`** checks for **inequality** (are these different values?).

---
