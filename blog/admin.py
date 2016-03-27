from django.contrib import admin

from .models import  Post, Thread, Topic, Comment

admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(Topic)
admin.site.register(Comment)

