from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    """Админ панель управления книгами """

    list_display = ('title', 'author', 'description', 'genre')
    search_fields = ('title', 'author', 'genre')
    empty_value_display = '-пусто-'


admin.site.register(Book, BookAdmin)
