from django.db import models
from django.utils import timezone

from user.models import Readers


class Books(models.Model):
    """Модель книги.
    ||
    Books model.
    """

    title = models.CharField(
        verbose_name='Название книги',
        help_text='Введите название книги',
        max_length=300,
        db_index=True,
        unique=True
    )
    author = models.CharField(
        verbose_name='Автор книги',
        help_text='Введите Автора книги',
        max_length=300,
    )
    description = models.CharField(
        verbose_name='Краткое описание книги',
        help_text='Напишите описание для книги',
        max_length=3000
    )
    genre = models.CharField(
        verbose_name='Жанр книги',
        help_text='Напишите жанр книги',
        max_length=50,
    )
    rented_by = models.ForeignKey(
        Readers,
        verbose_name='На руках у ...',
        help_text='Укажите пользователя у которого книга находиться на руках',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rented_books'
    )

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        """String representation method."""
        return self.title


class BooksRent(models.Model):
    """Модель выдачи книг.
    ||
    Book lending model."""

    book = models.ForeignKey(
        Books,
        verbose_name='Книга',
        help_text='Укажите Книгу',
        on_delete=models.CASCADE
    )
    reader = models.ForeignKey(
        Readers,
        verbose_name='Читатель',
        help_text='Укажите Читателя',
        on_delete=models.CASCADE
    )
    rented_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата выдачи книги',
        help_text='Укажите дату выдачи книги читателю'
    )
    returned_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата возврата книги',
        help_text='Укажите дату возврата книги читателем'
    )

    class Meta():
        verbose_name = 'Книга в аренде'
        verbose_name_plural = 'Книги в аренде'

    def __str__(self):
        return f"{self.reader.username} > {self.book.title}"

    @property
    def is_late(self):
        """Проверка возвращена ли книга вовремя (14 дней с момента выдачи).
        ||
        Checking if the book was returned on time
        (14 days from the date of issue).
        """

        if not self.return_date:
            return False
        return (
            self.returned_date > self.rented_at + timezone.timedelta(days=14))
