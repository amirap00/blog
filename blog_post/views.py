from django.shortcuts import render, get_object_or_404
from blog_post.models import Article

def blog(request, slug):
    # articles = Article.objects.get(id=pk)
    articles = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/post-details.html', {'articles': articles})

