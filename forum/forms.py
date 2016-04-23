from django import forms
from .models import *


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'tags', 'text', 'image',)
        widgets = {
            'text': forms.Textarea(attrs={'cols':60, 'style': 'height: 100px; min-width: 100%; max-width : 100%',
                                          'placeholder': "If you wish, print text here..."}),
            'tags': forms.Textarea(attrs={'style': 'max-height: 30px; min-height: 30px; height: 30px; width: 100%; max-width : 100%',
                                           'placeholder': "If you wish, print tags here..."}),
            'title': forms.Textarea(attrs={'style': 'max-height: 30px; min-height: 30px; height: 30px; width: 100%; max-width : 100%',
                                           'placeholder': "Name your thread..."}),
            'image': forms.FileInput(attrs={'id':'file'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'image')
        widgets = {
           'text': forms.Textarea(attrs={'style': 'height: 100px; width: 100%; max-width : 100%', 'align': 'center',
                                         'placeholder': "Your comment...", 'name': 'text'}),
             'image': forms.FileInput(attrs={'multiple accept': 'image/*', 'class': "file", 'name': 'file', 'type': "input", 'id': 'file',
                                             'style': 'height: 20px; width: 20px; font-size: 0; opacity:0'})
        }

#  add
#  'rows': 3,'cols': 50,
#  to make field size constant
