from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article
from .models import Booktemplates
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to your book list view
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_template.html', {'form': form})


def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('app_name.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@permission_required('app_name.can_create', raise_exception=True)
def article_create(request):
    # logic to create an article...
    pass

@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # logic to edit the article...
    pass

@permission_required('app_name.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # logic to delete the article...
    pass
