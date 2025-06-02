import requests
import random
from faker import Faker

fake = Faker()

for i in range(25):
    book = {
        "title": fake.catch_phrase(),
        "author": fake.name(),
        "isbn": fake.isbn13()
    }

    response = requests.post("http://localhost:3000/books", json=book)

    if response.status_code == 201:
        print(f" Added: {book['title']}")
    else:
        print(f" Failed: {response.status_code}")
