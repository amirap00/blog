from django.urls import path
from . import views

app_name = 'blog_post'
urlpatterns = [
    path('detail/<slug>', views.blog, name='article_detail')
]