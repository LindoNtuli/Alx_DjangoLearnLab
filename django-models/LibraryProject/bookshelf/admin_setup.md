# Admin Setup for Bookshelf App

## Registering the Book Model with the Django Admin

1. Open the `bookshelf/admin.py` file.
2. Import the `Book` model:
    ```python
    from .models import Book
    ```
3. Register the `Book` model with the admin site:
    ```python
    admin.site.register(Book)
    ```

## Customizing the Admin Interface

1. Create a custom admin class for the `Book` model:
    ```python
    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'publication_year')
        list_filter = ('author', 'publication_year')
        search_fields = ('title', 'author')
    ```
2. Register the `Book` model with the custom admin class:
    ```python
    admin.site.register(Book, BookAdmin)
    ```

## Enhancements

- The `list_display` attribute shows the `title`, `author`, and `publication_year` fields in the admin list view.
- The `list_filter` attribute adds filters for `author` and `publication_year`.
- The `search_fields` attribute enables search functionality for `title` and `author`.

This setup improves the management and visibility of book data within the Django admin interface.
```