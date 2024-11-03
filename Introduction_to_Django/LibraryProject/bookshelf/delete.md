#Djabgo delete model.

book_delete = Book.objects.get(publication_year = 1949)

book_delete.delete()

#output

(1, {'bookshelf.Book': 1})