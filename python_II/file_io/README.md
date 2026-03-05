# File I/O in Python

A beginner's guide to reading and writing files in Python.

---

## Opening a File

Use the built-in `open()` function. Always specify a **mode**:

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites file) |
| `"a"` | Append (adds to end) |
| `"x"` | Create (fails if file exists) |

Always use `with` — it automatically closes the file when done:

```python
with open("file.txt", "r") as f:
    # do something
```

---

## Reading

```python
# Read entire file as a string
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into a list
with open("file.txt", "r") as f:
    lines = f.readlines()
```

---

## Writing

```python
# Write to a file (creates it if it doesn't exist, overwrites if it does)
with open("file.txt", "w") as f:
    f.write("Hello, world!\n")

# Append without overwriting
with open("file.txt", "a") as f:
    f.write("Another line\n")
```

---

## Quick Tips

- `"r"` will throw an error if the file doesn't exist — use `"w"` or `"x"` to create it first.
- `f.write()` does **not** add a newline automatically — add `\n` yourself.
- `with open(...)` is always preferred over manually calling `f.close()`.
