# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title, updated_book.author, updated_book.publication_year)
# Expected output: Nineteen Eighty-Four George Orwell 1949
