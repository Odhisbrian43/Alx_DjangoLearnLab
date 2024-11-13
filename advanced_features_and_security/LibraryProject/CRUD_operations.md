#Command to creat a create a new book.

Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)

#Output for successfull creation.

<Book: Book object (1)>

#Retrieving details about all books created.

specific_book = Book.objects.get(title = "1984")
>>> print(f"title : {specific_book.title} author : {specific_book.author} publication_year : {specific_book.publication_year}")

#Output

title : 1984 author : George Orwell publication_year : 1949

#Updating elements in django CRUD.

update_book = Book.objects.filter(title = "1984")

update_book.update(title = "Nineteen Eighty-Four")

#Djabgo delete model.

book_delete = Book.objects.get(publication_year = 1949)

book_delete.delete()

#output

(1, {'bookshelf.Book': 1})
