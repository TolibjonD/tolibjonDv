from django import forms
from .models import Posts, PostComments


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("title", "body", "image")


class PostCommentsForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ("ismingiz", "fikringiz")
