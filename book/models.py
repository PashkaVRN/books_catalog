from django.db import models

from user.models import Readers
from django.conf import settings


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
        help_text='Укажите пользователя, у которого книга находиться на руках',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rented_books'
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступна'
    )

    class Meta():
        ordering = ('title', )
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class BooksRent(models.Model):
    """Модель выдачи книг.
    ||
    Book lending model."""

    book = models.ForeignKey(
        Books,
        verbose_name='Книга',
        help_text='Укажите Книгу',
        on_delete=models.SET_NULL,
        null=True,
    )
    reader = models.ForeignKey(
        Readers,
        verbose_name='Читатель',
        help_text='Укажите Читателя',
        on_delete=models.SET_NULL,
        null=True,
    )
    rented_at = models.DateField(
        verbose_name='Дата выдачи книги',
        help_text='Укажите дату выдачи книги читателю',
        null=True,
        blank=True,
    )
    fixed_returned_at = models.DateField(
        null=True,
        blank=True,
        verbose_name='Фиксированная дата возврата книги',
        help_text='Укажите фиксированную дату возврата книги читателем',
    )
    fact_returned_at = models.DateField(
        null=True,
        blank=True,
        verbose_name='Фактическая дата возврата книги',
        help_text='Укажите фактическую дату возврата книги читателем'
    )

    class Meta():
        ordering = ('fixed_returned_at', )
        verbose_name = 'Книгу в аренде'
        verbose_name_plural = 'Книги в аренде'

    def __str__(self):
        return f"{self.reader.username} взял {self.book.title}"

    def is_late(self):
        """Проверка возврата книги до фиксированной даты пользователем. """

        if not self.fixed_returned_at or not self.rented_at:
            return False
        returned_at = self.fact_returned_at or self.fixed_returned_at
        rental_duration = returned_at - self.rented_at
        # указываем фиксированное количество дней аренды
        return rental_duration.days > settings.FIX_DAYS_RETURN

    def save(self, *args, **kwargs):
        """Подсчет репутации пользователя
           в зависимости от фактической даты возврата книги.
        """

        if self.fixed_returned_at:
            is_returned_on_time = self.is_late()
            # если дата фактического возврата задана
            # и равна или раньше фиксированной, начисляем +1 репутацию
            if (self.fact_returned_at and
                    self.fact_returned_at <= self.fixed_returned_at):
                self.reader.reputation += 1
            # если дата фактического возврата еще не задана
            # и срок возврата просрочен, уменьшаем репутацию
            elif not self.fact_returned_at and is_returned_on_time:
                self.reader.reputation -= 1
            elif (self.fact_returned_at and
                    self.fact_returned_at > self.fixed_returned_at):
                self.reader.reputation -= 1
        self.reader.save()
        super().save(*args, **kwargs)


class BookReserved(models.Model):
    """Модель бронирования книг пользователем. """

    book = models.ForeignKey(
        Books,
        verbose_name='Книга',
        help_text='Выберите книгу для бронирования',
        related_name='reservations',
        on_delete=models.SET_NULL,
        null=True
    )
    reader = models.ForeignKey(
        Readers,
        verbose_name='Читатель',
        help_text='Укажите читателя который бронирует книгу',
        on_delete=models.SET_NULL,
        null=True
    )
    reserved_from = models.DateField(
        verbose_name='Дата бронирования'
    )
    is_active = models.BooleanField(
        verbose_name='Статус бронирования Активно/Нет',
        default=True
    )

    class Meta():
        ordering = ('reserved_from', )
        verbose_name = 'Забронированные книги'
        verbose_name_plural = 'Забронированные книги'

    def __str__(self):
        return f"{self.reader.username} забронировал {self.book.title}"
