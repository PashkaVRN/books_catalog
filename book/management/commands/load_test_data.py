import json

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from book.models import Books
from user.models import Readers


class Command(BaseCommand):
    help = ' Загрузить данные в модель Books и Readers '

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Старт команды'))
        with open('test_data/test_books.json', encoding='utf-8',
                  ) as data_file_test_book:
            test_book_data = json.loads(data_file_test_book.read())
            for books in test_book_data:
                Books.objects.get_or_create(**books)

        with open('test_data/test_users.json', encoding='utf-8',
                  ) as data_file_test_user:
            test_user_data = json.loads(data_file_test_user.read())
            for readers in test_user_data:
                # хешируем пароль
                readers['password'] = make_password(readers['password'])
                Readers.objects.get_or_create(**readers)

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
