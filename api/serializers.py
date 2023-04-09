from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from book.models import Books, BooksRent, Readers


class UserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя.
    ||
    User creation serializer.
    """

    class Meta:
        """Мета параметры модели.
        ||
        Model's meta parameters.
        """
        model = User
        fields = (
            'email', 'username', 'first_name',
            'last_name', 'password'
        )


class UserSerializer(UserSerializer):
    """Сериализатор пользователя.
    ||
    User serializer.
    """

    class Meta:
        """Мета параметры модели.
        ||
        Model's meta parameters.
        """
        model = User
        fields = (
             'email', 'id', 'username',
             'first_name', 'last_name'
        )


class BooksRentSerializer(serializers.ModelSerializer):
    """Сериализатор аренды Книги.
    ||
    Book Lease Serializer.
    """

    class Meta:
        """Мета параметры модели.
        ||
        Model's meta parameters.
        """
        model = BooksRent
        fields = (
            'id', 'book', 'reader', 'rented_at',
            'returned_at', 'is_late'
        )


class BooksSerializers(serializers.ModelSerializer):
    """Сериализатор вывода Книг.
    ||
    Books output serializer.
    """

    rents = BooksRentSerializer(many=True, read_only=True)

    class Meta:
        """Мета параметры модели.
        ||
        Model's meta parameters.
        """
        model = Books
        fields = (
            'id', 'title', 'author', 'description',
            'genre', 'rented_by', 'rents'
        )


class ReadersSerializer(serializers.ModelSerializer):
    """Reader Serializer.
    ||
    Reader Reputation Serializer.
    """

    class Meta:
        """Мета параметры модели.
        ||
        Model's meta parameters.
        """
        model = Readers
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'phone_number', 'score'
        )
