from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'time_posted', 'image', 'author_ip', )

    """
    text = models.TextField(max_length=200)
time_posted = models.DateTimeField(default=timezone.now)
image = models.ImageField(upload_to=get_unique_path, blank=True)
author_ip = models.CharField(max_length=100, default='unknown')
def __str__(self):
    return self.text
    """
