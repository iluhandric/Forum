from django.db import models
from django.utils import timezone
import uuid
import os


def get_image_path(instance, filename):
    return os.path.join('./media', str(instance.id), filename)

def get_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('./', filename)


class Blocked(models.Model):
    address = models.CharField(max_length=100, default='u')

    def __str__(self):
        return self.address


class Tag(models.Model):
    title = models.CharField(max_length=30)
    uses = models.BigIntegerField(blank=False)
    parent = models.BigIntegerField(blank=False)

    def __str__(self):
        return self.title


class Photo(models.Model):
    body = models.TextField(blank=True, null=True)


class Comment(models.Model):
    text = models.TextField(max_length=200)
    time_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=get_unique_path, blank=True)
    author_ip = models.CharField(max_length=100, default='unknown')

    def __str__(self):
        return self.text


class UserIp(models.Model):  # The model used to check user connection to the thread page
    ip = models.CharField(max_length=100, default='unknown')
    last_request = models.DateTimeField(default=None)

    def __str__(self):
        return self.ip


class Thread(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, max_length=500)
    parent = models.BigIntegerField(blank=False)
    comments = models.ManyToManyField(Comment, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    parsed_tags = models.ManyToManyField(Tag, blank=True)
    time_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=get_unique_path, blank=True)
    users = models.ManyToManyField(UserIp, blank=True)
    author_ip = models.CharField(max_length=100, default='unknown')

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=get_unique_path)
    threads = models.ManyToManyField(Thread, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def add_topic(self):
        self.save()

    def remove(self):
        self.delete()

    def __str__(self):
        return self.title

# Examples of previous models
#
# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=100)
#     text = models.TextField(blank=True, null=True)
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def remove(self):
#         self.delete()
#
#     def __str__(self):
#         return self.title
#
# class Admin(models.Model):
#     cur_ip = models.CharField(max_length=100, default='127.0.0.1')
#     password = models.CharField(max_length=100, default='password')
