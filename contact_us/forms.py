from django.forms import ModelForm
from .models import Contact
from django_summernote.widgets import SummernoteWidget


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']
        widgets = {
            'message': SummernoteWidget(),
        }