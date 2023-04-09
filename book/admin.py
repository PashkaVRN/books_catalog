from django.contrib import admin

from .models import Books, BooksRent, Readers


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    """Админ панель управления книгами.
    ||
    Books admin zone.
    """

    list_display = ('title', 'author', 'description', 'genre', 'rented_by')
    search_fields = ('title', 'author', 'genre')
    empty_value_display = 'В наличии'


@admin.register(Readers)
class ReadersAdmin(admin.ModelAdmin):
    """Админ панель управления читателями.
    ||
    Readers admin zone.
    """

    list_display = (
        'username', 'first_name', 'last_name',
        'email', 'phone_number', 'score'
    )
    search_fields = ('username', 'first_name', 'last_name')
    empty_value_display = '-пусто-'


@admin.register(BooksRent)
class BooksRentAdmin(admin.ModelAdmin):
    """Админ панель выдачи книг читателям."""

    list_display = ('book', 'reader', 'rented_at', 'returned_date')
    search_fields = ('book', 'reader')
    empty_value_display = '-пусто-'
