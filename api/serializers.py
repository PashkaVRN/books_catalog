from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from book.models import Books


class BooksSerializers(serializers.ModelSerializer):
    """Сериализатор вывода Книг. """

    class Meta:
        model = Books
        fields = ('title', 'author', 'description', 'genre')


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
