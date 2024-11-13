from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['featured_image', 'title','author', 'content', 'status']
        widgets = {
            'content': SummernoteWidget(),
        }






    



