import requests

# Step 1: Get all books from the API
response = requests.get("http://localhost:3000/books")
if response.status_code != 200:
    print("❌ Failed to fetch books")
    exit()

books = response.json()  # Assuming the API returns a list of books as JSON

# Make sure we have enough books to delete
if len(books) < 10:
    print("Not enough books to delete first and last 5.")
    exit()

# Step 2: Select first 5 and last 5 books
books_to_delete = books[:5] + books[-5:]

# Step 3: Delete each book by its ID (assuming 'id' field exists)
for book in books_to_delete:
    book_id = book.get("id")  # adjust the key if your ID field is named differently
    if not book_id:
        print("❌ Book ID not found, skipping...")
        continue

    del_response = requests.delete(f"http://localhost:3000/books/{book_id}")
    if del_response.status_code == 200 or del_response.status_code == 204:
        print(f"✅ Deleted book ID {book_id}")
    else:
        print(f"❌ Failed to delete book ID {book_id}: {del_response.status_code}")

