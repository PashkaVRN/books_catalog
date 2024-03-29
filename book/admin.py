from django.contrib import admin

from .models import Books, BooksRent, BookReserved


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    """Админ панель управления книгами.
    ||
    Books admin zone.
    """

    list_display = ('title', 'author', 'description',
                    'genre', 'rented_by', 'id', 'is_available')
    search_fields = ('title', 'author', 'genre')
    empty_value_display = 'В наличии'


@admin.register(BooksRent)
class BooksRentAdmin(admin.ModelAdmin):
    """Админ панель выдачи книг читателям."""

    list_display = ('book', 'reader', 'rented_at',
                    'fixed_returned_at', 'fact_returned_at')
    search_fields = ('book', 'reader')
    empty_value_display = '-пусто-'


@admin.register(BookReserved)
class BookReservedAdmin(admin.ModelAdmin):
    """Админ панель бронирования книг читателям. """

    list_display = ('book', 'reader', 'reserved_from',
                    'is_active')
    search_fields = ('book', 'reader')
    empty_value_display = '-пусто-'
