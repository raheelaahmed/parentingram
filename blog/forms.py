from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.forms.widgets import HiddenInput
from django.utils.text import slugify






class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['featured_image', 'title','author','slug', 'content', 'status']
       
      
        labels = {
            'slug': "",
            
        }
        
  
   
    widgets = {
            'content': SummernoteWidget(),
           
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget = forms.TextInput() 
        

      

   





    



