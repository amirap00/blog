from blog_post.models import Article

def recent_articles(request):
    recent_article = Article.objects.order_by('-date')
    return {'recent_article': recent_article}