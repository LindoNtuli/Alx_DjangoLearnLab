# CRUD_operations.md

## Create Operation
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected Output: <Book: Book object (1)>


## Retrieve Operation
from bookshelf.models import Book
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
# Expected Output: 1984 George Orwell 1949


## Update Operation
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Expected Output: Nineteen Eighty-Four

## Delete Operation
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
books = Book.objects.all()
print(books)
# Expected Output: <QuerySet []>