from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from book.models import Books, BooksRent
from user.models import Readers

from .permissions import IsAdminModeratorOrSuperUser, IsAdminOrReadOnly
from .serializers import BooksSerializers, UserSerializer
from datetime import timezone


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

    def list(self, request):
        """Запрет доступа к списку пользователей для всех,
           кроме администраторов,
           модераторов и суперпользователей. """

        if not request.user.is_superuser and not request.user.is_staff:
            raise PermissionDenied
        return super().list(request)

    def put(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        data = request.data
        reader_id = data.get('reader_id', None)
        rented_at = data.get('rented_at', None)
        returned_at = data.get('returned_at', None)
        # Ищем аренду, соответствующую переданным данным
        rent = BooksRent.objects.filter(
            book=book, reader=reader_id, rented_at=rented_at, returned_at=None
        ).first()

        if not rent:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rent.returned_at = timezone.now()
        rent.save()
        # Проверяем, была ли книга возвращена вовремя
        is_returned_on_time = rent.is_late()
        # Обновляем репутацию пользователя
        if is_returned_on_time:
            rent.reader.reputation += 1
        else:
            rent.reader.reputation -= 1
        rent.reader.save()
        return Response(status=status.HTTP_200_OK)
