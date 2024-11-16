**Create Operation:**
Create a file named `create.md` with the following content:
```markdown
# create.md
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected Output: <Book: Book object (1)>
```
```