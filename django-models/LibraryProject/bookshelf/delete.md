**Delete Operation:**
Create a file named `delete.md` with the following content:
```markdown
# delete.md
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
books = Book.objects.all()
print(books)
# Expected Output: <QuerySet []>
```
```