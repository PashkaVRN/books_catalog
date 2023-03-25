from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from book.models import Books, BooksRent, ReaderReputation, Readers


class UserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя."""

    class Meta:
        model = User
        fields = (
            'email', 'username', 'first_name',
            'last_name', 'password')


class UserSerializer(UserSerializer):
    """Сериализатор пользователя."""

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name')


class BooksRentSerializer(serializers.ModelSerializer):
    """Сериализатор аренды Книги."""

    class Meta:
        model = BooksRent
        fields = ('id', 'book', 'reader',
                  'rented_at', 'returned_at', 'is_late')


class BooksSerializers(serializers.ModelSerializer):
    """Сериализатор вывода Книг."""

    rents = BooksRentSerializer(many=True, read_only=True)

    class Meta:
        model = Books
        fields = ('id', 'title', 'author', 'description', 'genre',
                  'rented_by', 'rents')


class ReaderReputationSerializer(serializers.ModelSerializer):
    """Сериализатор репутации Читателя."""

    reader = serializers.CharField(source='reader.username', read_only=True)

    class Meta:
        model = ReaderReputation
        fields = ('id', 'reader', 'score')


class ReadersSerializer(serializers.ModelSerializer):
    """Сериализатор Читателя."""

    reputation = ReaderReputationSerializer(many=False, read_only=True)
    
    class Meta:
        model = Readers
        fields = ('username', 'first_name', 'last_name',
                  'email', 'phone_number', 'reputation')

    # def create(self, validated_data):
    #     """Создание читателя."""

    #     reputation_data = validated_data.pop('reputation')
    #     reader = Readers.objects.create(**validated_data)
    #     ReaderReputation.objects.create(reader=reader, **reputation_data)
    #     return reader