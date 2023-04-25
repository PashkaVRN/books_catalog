from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from book.models import BookReserved, Books, BooksRent
from user.models import Readers


class BooksSerializers(serializers.ModelSerializer):
    """Сериализатор вывода Книг.
    ||
    Books output serializer.
    """

    class Meta:
        model = Books
        fields = (
            'id', 'title', 'author', 'description',
            'genre', 'rented_by', 'is_available'
        )


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
    book = BooksSerializers(read_only=True)
    reader = serializers.StringRelatedField()

    class Meta:
        """Мета параметры модели.
        ||
        Model's meta parameters.
        """
        model = BooksRent
        fields = (
            'id', 'book', 'reader', 'rented_at', 'fact_returned_at'
        )


class BookReservedSerialier(serializers.ModelSerializer):
    """Сериализатор бронирования книги. """

    # reserved_from = serializers.DateTimeField(format='%d.%m.%Y')

    class Meta:
        model = BookReserved
        fields = (
            'id', 'book', 'reader', 'reserved_from', 'is_active'
        )

    # def to_representation(self, instance):
    #     # конвертируем дату строку формата "гггг-мм-ддТчч:мм:сс+HH:MM" в объект datetime
    #     reserved_from = datetime.fromisoformat(instance.reserved_from)
    #     # вызываем родительский метод to_representation для выполнения базовой сериализации данных
    #     data = super().to_representation(instance)
    #     # форматируем дату в заданный формат
    #     data['reserved_from'] = reserved_from.strftime('%d.%m.%Y')
    #     return data