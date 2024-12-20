from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.forms.widgets import HiddenInput
from django.utils.text import slugify
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


# comment form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# create and update post form
class PostForm(forms.ModelForm,):
    class Meta:
        model = Post
        fields = ['featured_image', 'title', 'slug', 'content', 'status']
        labels = {
            'slug': "",
                 }
        widgets = {
           'content': CKEditorWidget(),
                  }







 
      

   





    



