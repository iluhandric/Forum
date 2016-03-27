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
    body = models.TextField(blank=True, null=True)


class Comment(models.Model):
    text = models.CharField(max_length=100)
    parent = None  # getting by Thread.objects.get(pk=self.parent)

    def add_comment(self):
        self.save()
        Thread.objects.get(pk=self.parent).comments.add(self)

    def get_parent(self):
        return Thread.objects.get(pk=self.parent)

    def remove(self):
        self.delete()

    def __str__(self):
        return self.text


class Thread(models.Model):
    title = models.CharField(max_length=100)
    parent = 10  # getting by Topic.objects.get(pk=self.parent)
    comments = models.ManyToManyField(Comment, blank=True)

    def get_parent(self):
        return Topic.objects.get(pk=self.parent)

    def add_thread(self):
        self.save()
        Topic.objects.get(pk=self.parent).threads.add(self)

    def remove(self):
        self.delete()

    def __str__(self):
        return self.title

import os
def get_image_path(instance, filename):
    return os.path.join('./media', str(instance.id), filename)


class Topic(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='')
    threads = models.ManyToManyField(Thread, blank=True)
    colnum = models.BigIntegerField(blank=False)

    def add_topic(self):
        self.save()

    def remove(self):
        self.delete()

    def __str__(self):
        return self.title
