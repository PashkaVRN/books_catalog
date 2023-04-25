from django.core.exceptions import PermissionDenied
from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle

from book.models import BookReserved, Books, BooksRent
from user.models import Readers

from .permissions import IsAdminModeratorOrSuperUser, IsAdminOrReadOnly
from .serializers import (BookReservedSerialier, BooksRentSerializer,
                          BooksSerializers, UserSerializer)


class UserViewSet(UserViewSet):
    """Представление Пользователя.
    ||
    User viewset.
    """

    queryset = Readers.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminModeratorOrSuperUser, )

    def list(self, request):
        """Запрет доступа к списку пользователей для всех,
           кроме администраторов,
           модераторов и суперпользователей. """

        if not request.user.is_superuser and not request.user.is_staff:
            raise PermissionDenied
        return super().list(request)


class BooksViewSet(viewsets.ModelViewSet):
    """Представление Книг.
    ||
    Books viewset.
    """

    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    pagination_class = PageNumberPagination
    throttle_classes = (AnonRateThrottle, )
    permission_classes = (IsAdminOrReadOnly, )


class RentLateReturnViewSet(viewsets.ModelViewSet):
    """Аренда/Возврат книги.
    ||
    Book rental/return viewset.
    """

    pagination_class = PageNumberPagination
    permission_classes = (IsAdminModeratorOrSuperUser, )
    queryset = BooksRent.objects.all()
    serializer_class = BooksRentSerializer

    def list(self, request):
        """Запрет доступа к списку арендованных книг для всех,
           кроме администраторов,
           модераторов и суперпользователей. """

        if not request.user.is_superuser and not request.user.is_staff:
            raise PermissionDenied
        return super().list(request)


class BookReservedViewSet(viewsets.ModelViewSet):
    """Бронировании книги Читателем. """

    queryset = BookReserved.objects.all()
    serializer_class = BookReservedSerialier
