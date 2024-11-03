#Updating elements in django CRUD.

update_book = Book.objects.filter(title = "1984")

update_book.update(title = "Nineteen Eighty-Four")