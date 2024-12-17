from django.db import models


# Create your models here.
class Book(models.Model):
    class GenreChoices(models.TextChoices):
        CRIME = 'C'
        NON_FICTION = 'N'
        OTHER = 'O'
        SCI_FI = 'S'

    name = models.CharField(max_length=128)
    price = models.FloatField()
    number_in_stock = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=1, choices=GenreChoices.choices)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=128)
