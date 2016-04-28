from django.contrib import admin
import haystack

from .models import *
admin.site.register(Thread)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Blocked)
admin.site.register(UserIp)
