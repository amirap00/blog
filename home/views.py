from django.shortcuts import render
from blog_post.models import Article

def home(request):
    # articles = Article.objects.all()
    # print(Article.objects.counter())
    # articles = Article.objects.filter(status=True)
    articles = Article.custom_manager.all()
    return render(request, 'home_app/index.html', {'articles': articles})