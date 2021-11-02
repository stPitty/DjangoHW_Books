import csv

from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('data.csv', 'r') as file:
            books = list(csv.DictReader(file, delimiter=','))

        for book in books:
            book_model = Book(
                name = book['buyer'],
                author = book['seller'],
                pub_date = book['created_at'].split(' ')[0]
            )
            book_model.save()
