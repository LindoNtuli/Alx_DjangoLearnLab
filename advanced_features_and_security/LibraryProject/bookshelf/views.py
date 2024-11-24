from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article

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
