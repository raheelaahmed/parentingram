from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    summernote_fields = ('message',)