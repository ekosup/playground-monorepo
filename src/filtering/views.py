from django import forms
from django.shortcuts import render

from .filters import BookFilter
from .models import Book


class BookNameFilterForm(forms.Form):
    name = forms.CharField()


# Create your views here.
def index(request):
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = {
        'form': BookNameFilterForm(),
        'books': book_filter.qs
    }
    return render(request, 'index.html', context)
