**Retrieve Operation:**
Create a file named `retrieve.md` with the following content:
```markdown
# retrieve.md
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
# Expected Output: 1984 George Orwell 1949
```
```