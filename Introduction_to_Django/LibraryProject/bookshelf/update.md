#Updating elements in django CRUD.

book.title = Book.objects.filter(title = "1984")

update_book.update(title = "Nineteen Eighty-Four")