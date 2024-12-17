from django.core.management.base import BaseCommand

from filtering.models import Book, Author


class Command(BaseCommand):
    help: str = 'Load book data'

    def handle(self, *args, **options):
        # authors
        orwell = Author.objects.get_or_create(name='George Orwell')[0]
        zamyatin = Author.objects.get_or_create(name='yevgeny Zamyatin')[0]
        christie = Author.objects.get_or_create(name='Agatha Christie')[0]
        hawking = Author.objects.get_or_create(name='Stephen Hawking')[0]
        highsmith = Author.objects.get_or_create(name='Patricia Highsmith')[0]
        bradbury = Author.objects.get_or_create(name='Ray Bradbury')[0]

        # create book
        Book.objects.get_or_create(
            name='1984',
            author=orwell,
            price=10.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=4
        )

        Book.objects.get_or_create(
            name='A Brief History of Time',
            author=hawking,
            price=20.99,
            genre=Book.GenreChoices.NON_FICTION,
            number_in_stock=2
        )

        Book.objects.get_or_create(
            name='Murder on the Orient Express',
            author=christie,
            price=7.99,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=10
        )

        Book.objects.get_or_create(
            name='Death on the Nile',
            author=christie,
            price=18.99,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=1
        )

        Book.objects.get_or_create(
            name='We',
            author=zamyatin,
            price=11.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=8
        )

        Book.objects.get_or_create(
            name='Animal Farm',
            author=orwell,
            price=15.99,
            genre=Book.GenreChoices.OTHER,
            number_in_stock=5
        )

        Book.objects.get_or_create(
            name='Strangers on a Train',
            author=highsmith,
            price=15.99,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=10
        )

        Book.objects.get_or_create(
            name='Fahrenheit 451',
            author=bradbury,
            price=13.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=4
        )
