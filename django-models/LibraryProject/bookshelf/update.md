**Update Operation:**
Create a file named `update.md` with the following content:
```markdown
# update.md
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Expected Output: Nineteen Eighty-Four
```
```