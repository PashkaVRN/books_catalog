from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from book.models import Books, BooksRent
from user.models import Readers


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
        model = Readers
        fields = (
            'email', 'username', 'first_name',
            'last_name', 'password', 'phone_number', 'id'
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
        model = Readers
        fields = (
             'email', 'id', 'username', 'reputation',
             'first_name', 'last_name', 'phone_number'
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
            'fact_returned_at'
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
