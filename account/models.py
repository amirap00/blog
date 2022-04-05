from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=25)
    national_code = models.IntegerField()
    image = models.ImageField(upload_to='profile/images', null=True, blank=True)

    def __str__(self):
        return self.user.username



class New(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.replace(' ', '-')
        super(New, self).save(args, kwargs)