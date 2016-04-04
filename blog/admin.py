from django.contrib import admin

from .models import *

admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Tag)

