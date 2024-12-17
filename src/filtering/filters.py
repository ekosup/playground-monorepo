import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['name', 'author__name', 'price', 'genre']
