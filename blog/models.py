from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

"""
class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followees', symmetrical=False)
"""


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def remove(self):
        self.delete()

    def __str__(self):
        return self.title


class Photo(models.Model):
    post = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField(upload_to="%Y/%m/%d")