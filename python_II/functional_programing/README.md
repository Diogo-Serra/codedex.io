# Functional Programming in Python

A beginner's guide to writing cleaner, more expressive Python using functional programming concepts.

---

## What is Functional Programming?

Functional programming is a style of coding where you build programs using **functions** as the main building block. Key ideas:

- Functions should be **pure** — same input always gives same output, no side effects.
- Avoid changing data in place — create new data instead.
- Use built-in tools like `map()`, `filter()`, and `reduce()` to transform data.

---

## Pure Functions

A pure function has no side effects and doesn't rely on anything outside itself:

```python
# Pure — only depends on its input
def double(x):
    return x * 2

# Impure — modifies something outside the function
total = 0
def add_to_total(x):
    global total
    total += x  # side effect!
```

---

## Transformation Functions

### `map()`

Applies a function to **every element** in a list and returns a new list.

```python
def divide_by_2(x):
    return x / 2

result = map(divide_by_2, [1, 2, 3, 4, 5])
print(list(result))  # [0.5, 1.0, 1.5, 2.0, 2.5]
```

### `filter()`

Returns only the elements where the function returns **True**.

```python
def is_even(x):
    return x % 2 == 0

result = filter(is_even, [1, 2, 3, 4, 5])
print(list(result))  # [2, 4]
```

### `reduce()`

Combines all elements into a **single value** by applying a function repeatedly.
Must be imported from `functools`.

```python
from functools import reduce

def multiply(x, y):
    return x * y

result = reduce(multiply, [1, 2, 3, 4, 5])
print(result)  # 120
```

| Function | What it does | Returns |
|---|---|---|
| `map()` | Transform every element | New list (same length) |
| `filter()` | Keep elements that match a condition | New list (shorter or equal) |
| `reduce()` | Combine all elements into one value | Single value |

---

## Lambda Functions

A **lambda** is a short, anonymous function written in one line.
Useful when you don't want to define a full `def` function just for a small operation.

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(4))  # 16
```

Lambdas are commonly paired with `map()` and `filter()`:

```python
doubled = list(map(lambda x: x * 2, [1, 2, 3]))
# [2, 4, 6]

evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
# [2, 4]
```

---

## List Comprehensions

A concise way to build lists — often replacing `map()` + `filter()` in one line.

```python
# Syntax
[expression for item in dataset if condition]
```

```python
numbers = [1, 2, 3, 4, 5]

# Square every number
squares = [n ** 2 for n in numbers]
# [1, 4, 9, 16, 25]

# Only even numbers squared
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
# [4, 16]
```

Comparison with the loop approach:

```python
# Loop approach
squares = []
for n in numbers:
    squares.append(n ** 2)

# List comprehension — same result, one line
squares = [n ** 2 for n in numbers]
```

---

## Quick Tips

- Use `lambda` for short, throwaway functions — use `def` for anything more complex.
- `map()` and `filter()` return iterators — wrap with `list()` to see the output.
- `reduce()` must be imported: `from functools import reduce`.
- List comprehensions are usually preferred over `map()`/`filter()` in modern Python for readability.
