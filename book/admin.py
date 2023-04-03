from django.contrib import admin

from .models import Books, Readers


class BooksAdmin(admin.ModelAdmin):
    """Админ панель управления книгами.
    ||
    Books admin zone.
    """

    list_display = ('title', 'author', 'description', 'genre', 'rented_by')
    search_fields = ('title', 'author', 'genre')
    empty_value_display = '-пусто-'

class ReadersAdmin(admin.ModelAdmin):
    """Админ панель управления читателями.
    ||
    Readers admin zone.
    """

    list_display = (
        'username', 'first_name', 'last_name',
        'email', 'phone_number', 'reputation'
    )
    search_fields = ('username', 'first_name', 'last_name')
    empty_value_display = '-пусто-'

admin.site.register(Books, BooksAdmin)
admin.site.register(Readers, ReadersAdmin)
