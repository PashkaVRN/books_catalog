from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from book.models import Books, BooksRent, ReaderReputation


class UserCreateSerializer(UserCreateSerializer):
    """ Сериализатор создания пользователя. """

    class Meta:
        model = User
        fields = (
            'email', 'username', 'first_name',
            'last_name', 'password')


class UserSerializer(UserSerializer):
    """ Сериализатор пользователя. """

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name')


class BooksRentSerializer(serializers.ModelSerializer):
    """ Сериализатор аренды Книги. """

    class Meta:
        model = BooksRent
        fields = ('id', 'book', 'reader',
                  'rented_at', 'returned_at', 'is_late')


class BooksSerializers(serializers.ModelSerializer):
    """Сериализатор вывода Книг. """

    rents = BooksRentSerializer(many=True, read_only=True)

    class Meta:
        model = Books
        fields = ('id', 'title', 'author', 'description', 'genre',
                  'rented_by', 'rents')


class ReaderReputationSerializer(serializers.ModelSerializer):
    """ Сериализатор репутации Читателя. """

    reader = serializers.CharField(source='reader.username', read_only=True)

    class Meta:
        model = ReaderReputation
        fields = ('id', 'reader', 'score')
