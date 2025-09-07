# Delete the book
book.delete()

# Confirm deletion
books = Book.objects.all()
print(list(books))

# Expected output: []