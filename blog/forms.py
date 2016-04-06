from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'tags', 'body',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
           'text': forms.Textarea(attrs={'style': 'height: 100px; width: 100%'})
        }
#  add
#  'rows': 3,'cols': 50,
#  to make field size constant
