# Testing in Python

A beginner's guide to unit testing with Python's built-in `unittest` framework.

---

## What is Unit Testing?

Unit testing means taking small pieces of your program (functions, methods, classes) and verifying they behave as expected — before bugs reach production.

---

## Setup

`unittest` is built into Python — no install needed:

```python
import unittest
```

---

## Writing Your First Test

Create a class that inherits from `unittest.TestCase`. Each test is a method prefixed with `test_`:

```python
import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

Run it with:
```bash
python3 test_myfile.py
```

---

## Assert Methods

| Method | Checks |
|---|---|
| `self.assertEqual(a, b)` | `a == b` |
| `self.assertNotEqual(a, b)` | `a != b` |
| `self.assertTrue(x)` | `x` is truthy |
| `self.assertFalse(x)` | `x` is falsy |
| `self.assertIn(a, b)` | `a` is in `b` |
| `self.assertNotIn(a, b)` | `a` is not in `b` |
| `self.assertRaises(Error)` | a specific error is raised |

---

## Edge Cases with `assertRaises()`

Use `assertRaises()` to verify that bad input raises the right error:

```python
class TestEdgeCases(unittest.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.assertIn('World', 123)  # 123 is not a string → TypeError
```

---

## Testing Classes with `setUp` and `tearDown`

When testing a class, use:
- `setUp()` — runs **before each test**, sets up a fresh object
- `tearDown()` — runs **after each test**, cleans up resources

```python
import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()  # fresh instance before each test

    def tearDown(self):
        self.calc = None  # clean up after each test

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

if __name__ == '__main__':
    unittest.main()
```

---

## Test Lifecycle

```
setUp()  →  test_method()  →  tearDown()
setUp()  →  test_method()  →  tearDown()
...      (once per test)   ...
```

Each test runs independently — a failure in one never affects the others.

---

## Quick Tips

- Name test files with a `test_` prefix: `test_calculator.py`.
- Name test methods with a `test_` prefix — otherwise `unittest` won't find them.
- One assertion per test is ideal — keeps failures easy to diagnose.
- `setUp()` and `tearDown()` are optional but essential when testing classes.
