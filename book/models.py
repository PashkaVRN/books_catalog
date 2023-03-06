from django.db import models


# Добавить в будущем реализацию фотографии книги(с двух сторон),
# нахождение ее у конкретного клиента библиотеки
class Books(models.Model):
    """ Модель книги. """

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

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
