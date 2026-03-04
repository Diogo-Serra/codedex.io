# Write a program that converts a Roman numeral to an integer

def roman_to_int(s: str) -> int:
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev = 0
    for char in reversed(s.upper()):
        value = roman[char]
        if value < prev:
            result -= value
        else:
            result += value
        prev = value
    return result


print(roman_to_int("XIV"))   # 14
print(roman_to_int("MCMXCIX"))  # 1999


# Write a program that calculates the factorial of a number

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))   # 120
print(factorial(10))  # 3628800


# Write a program that generates a blog

def generate_blog(title: str, author: str, content: str) -> str:
    from datetime import date
    today = date.today().strftime("%B %d, %Y")
    blog = f"""
{'=' * 50}
{title.upper()}
{'=' * 50}
By {author} | {today}
{'-' * 50}
{content}
{'-' * 50}
"""
    return blog.strip()


blog = generate_blog(
    title="My First Blog Post",
    author="Jane Doe",
    content=(
        "Welcome to my blog! Today I'll be sharing some thoughts on "
        "Python programming and why it's such a fantastic language "
        "for beginners and experts alike."
    )
)
print(blog)
