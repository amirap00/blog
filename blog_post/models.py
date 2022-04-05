from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# unique_for_date='pub_date'


class Category(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# با این کد base queryset را شخصی سازی میکنیم
class CustomManager(models.Manager):
    def get_queryset(self):
        return super(CustomManager, self).get_queryset().filter(status=True)


# اضافه کردن یه سری ویژگی های دلخواه به manager
# class ArticleManager(models.Manager):
#     def counter(self):
#         return len(self.all())


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=70)
    category = models.ManyToManyField(Category)
    body = models.TextField()
    image = models.ImageField(upload_to='images/article')
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    # به جای ایدی به ما یک نوشته با معنی نشان میدهد
    slug = models.SlugField(null=True, blank=True, unique=True)
    objects = models.Manager()
    custom_manager = CustomManager()
    # pub_date = models.DateField(default=timezone.now)


    # class Meta:
    #     ordering = ('-date',)


    # با این کار به جای پر کردن slug  به صورت دستی title به صورت خودکار جایگزین slug میشود و به جای space از dash استفاده میکند
    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog_post:article_detail', args=[self.slug])
        # return reverse('blog_post:article_detail', kwargs={'id': self.id})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"
