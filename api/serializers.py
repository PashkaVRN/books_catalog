from rest_framework import serializers

from book.models import Books


class BooksSerializers(serializers.ModelSerializer):
    """Сериализатор вывода Книг. """

    class Meta:
        model = Books
        fields = ('title', 'author', 'description', 'genre')
