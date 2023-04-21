from django.contrib import admin

from .models import Readers, DeletedReaders


@admin.register(Readers)
class ReadersAdmin(admin.ModelAdmin):
    """Админ панель управления читателями.
    ||
    Readers admin zone.
    """

    list_display = ('username', 'first_name', 'last_name', 'email',
                    'phone_number', 'reputation', 'id')
    search_fields = ('username', 'first_name', 'last_name', 'phone_number')
    list_filter = ('reputation', 'role')
    empty_value_display = '-пусто-'


@admin.register(DeletedReaders)
class DeletedReadersAdmin(admin.ModelAdmin):
    """Админ панель управления удаленными пользователями. """

    list_display = ('username', 'first_name', 'last_name', 'email',
                    'phone_number', 'reputation', 'id', 'deleted_at')
    search_fields = ('username', 'first_name', 'last_name',
                     'phone_number', 'deleted_at')
    empty_value_display = '-пусто-'
