# Tuples

A tuple in Python is an ordered, immutable collection of elements enclosed in parentheses (). Unlike lists, tuples cannot be modified after creation, making them ideal for storing fixed data that shouldn't change.
Tuples are used to store multiple items in a single variable.

**Key Features of Tuples**
✔ Ordered – Elements maintain their position.
✔ Immutable – Cannot be modified after creation.
✔ Heterogeneous – Can store different data types (int, str, list, etc.).
✔ Indexed – Access elements using indices (starts at 0).
✔ Hashable – Can be used as dictionary keys (unlike lists).

#### Creating a Tuple

Empty tuple

```python
empty_tuple = ()
```

#### Single-element tuple (requires a comma)

```python
single_tuple = (5,)  # Not (5)
```

#### Multiple elements

```python
fruits = ("apple", "banana", "cherry")
mixed_data = (1, "Python", 3.14, [10, 20])
```

### Accessing Tuple Elements

**1. Indexing**

```python
numbers = (10, 20, 30, 40, 50)
print(numbers[0])   # 10 (first element)
print(numbers[-1])  # 50 (last element)
```

**2. Slicing**

```python
print(numbers[1:4])  # (20, 30, 40)
print(numbers[:3])   # (10, 20, 30)
print(numbers[2:])   # (30, 40, 50)
```

**3. length**

```Python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) // output: 3
```

### Modifying Tuples (Indirectly)

Since tuples are immutable, you cannot change them directly. However, you can:

**1. Convert to List, Modify, and Convert Back**

```python
my_tuple = (1, 2, 3)
temp_list = list(my_tuple)  # Convert to list
temp_list.append(4)         # Modify
my_tuple = tuple(temp_list) # Convert back
print(my_tuple)  # (1, 2, 3, 4)
```

**2. Concatenate Tuples (Create New One)**

```python
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4)
```

## Tuple Operations

| Operation             | Example                          | Output               |
| --------------------- | -------------------------------- | -------------------- |
| **Length**            | `len((1, 2, 3))`                 | `3`                  |
| **Count Occurrences** | `(1, 2, 2, 3).count(2)`          | `2`                  |
| **Find Index**        | `(10, 20, 30).index(20)`         | `1`                  |
| **Membership Check**  | `"apple" in ("apple", "banana")` | `True`               |
| **Repetition**        | `(1, 2) * 3`                     | `(1, 2, 1, 2, 1, 2)` |

### difference between unpacking and destructuring

| Feature             | Python (Tuple Unpacking)    | JavaScript (Destructuring) |
| ------------------- | --------------------------- | -------------------------- |
| **Syntax**          | `x, y = (1, 2)`             | `[x, y] = [1, 2]`          |
| **Ignoring Values** | Use `_`                     | Use empty `,`              |
| **Rest Operator**   | `*rest`                     | `...rest`                  |
| **Works With**      | Tuples, lists, any iterable | Arrays, objects            |
