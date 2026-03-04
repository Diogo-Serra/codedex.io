#!/usr/bin/env python3

books = [
    'Harry Potter',
    '1984',
    'The Fault in Our Stars',
    'The Mom Test',
    'Life in Code']
books.append("Pachinko")
books.pop(1)
books.pop(1)
for book in books:
    print(book)
