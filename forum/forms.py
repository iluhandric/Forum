from django import forms
from .models import *


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'tags', 'text', 'image',)
        widgets = {
            'text': forms.Textarea(attrs={'style': 'height: 100px; width: 40%; max-width : 100%'}),
            'title': forms.Textarea(attrs={'style': 'height: 20px; width: 40%; max-width : 100%'}),
            # 'image': forms.ImageField()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'image')
        widgets = {
           'text': forms.Textarea(attrs={'style': 'height: 100px; width: 100%; max-width : 100%', 'align': 'center'}),

        }
#  add
#  'rows': 3,'cols': 50,
#  to make field size constant