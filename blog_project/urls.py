from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('account.urls')),
    path('articles/', include('blog_post.urls')),
    # path('', include('blog_post.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
