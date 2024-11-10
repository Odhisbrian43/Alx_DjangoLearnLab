#Retrieving details about all books created.

specific_book = Book.objects.get(title = "1984")
>>> print(f"title : {specific_book.title} author : {specific_book.author} publication_year : {specific_book.publication_year}")

#Output

title : 1984 author : George Orwell publication_year : 1949