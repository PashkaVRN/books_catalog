from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Readers(models.Model):
    """Модель Читателя/Посетителя библиотеки."""

    username = models.CharField(
        verbose_name='Username',
        max_length=100,
        unique=True,
        validators=(UnicodeUsernameValidator(), )
    )
    first_name = models.CharField(
        verbose_name='Имя читателя',
        max_length=50)
    last_name = models.CharField(
        verbose_name='Фамилия читателя',
        max_length=50)
    email = models.EmailField(
        unique=True,
        verbose_name='email читателя'
    )
    phone_number = PhoneNumberField(
        unique=True,
        null=False,
        blank=False,
    )
    score = models.IntegerField(
        default=10,
        verbose_name='Рейтинг Читателя'
    )

    class Meta:
        ordering = ('username', )
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.username


class Books(models.Model):
    """Модель книги."""

    title = models.CharField(
        verbose_name='Название книги',
        max_length=300,
        db_index=True,
        unique=True
    )
    author = models.CharField(
        verbose_name='Автор книги',
        max_length=300,
    )
    description = models.CharField(
        verbose_name='Краткое описание книги',
        max_length=3000
    )
    genre = models.CharField(
        verbose_name='Жанр книги',
        max_length=50,
    )
    rented_by = models.ForeignKey(
        Readers,
        verbose_name='На руках у ...',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rented_books'
    )

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class BooksRent(models.Model):
    """Модель выдачи книг."""

    book = models.ForeignKey(
        Books,
        verbose_name='Книга',
        on_delete=models.CASCADE
    )
    reader = models.ForeignKey(
        Readers,
        verbose_name='Читатель',
        on_delete=models.CASCADE
    )
    rented_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата выдачи книги',
    )
    returned_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата возврата книги',
    )

    class Meta():
        verbose_name = 'Книга в аренде'
        verbose_name_plural = 'Книги в аренде'

    def __str__(self):
        return f"{self.reader.username} > {self.book.title}"

    @property
    def is_late(self):
        """Проверка возвращена ли книга вовремя(14 дней с момента выдачи)."""

        if not self.return_date:
            return False
        return (
            self.returned_date > self.rented_at + timezone.timedelta(days=14))
