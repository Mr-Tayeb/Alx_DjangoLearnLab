# Update title
novel.title = "Harry Potter"
novel.save()

# Confirmation
updated_book = Book.objects.get(id=novel.id)
print(updated_novel.title, updated_novel.author, updated_novel.publication_year)

# Expected output: Harry Potter Ten Hug 2022