from django import forms
from django.contrib import admin
from unfold.admin import ModelAdmin

from blog.models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'thumbnail']


@admin.register(Notes)
class NotesAdmin(ModelAdmin):
    form = NotesForm
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
