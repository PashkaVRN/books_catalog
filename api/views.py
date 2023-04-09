from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from book.models import Books, BooksRent
from user.models import Readers

from .serializers import BooksSerializers, ReadersSerializer, UserSerializer


class UserViewSet(UserViewSet):
    """Представление Пользователя.
    ||
    User viewset.
    """

    queryset = Readers.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination


class BooksViewSet(viewsets.ModelViewSet):
    """Представление Книг.
    ||
    Books viewset.
    """

    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    throttle_classes = (AnonRateThrottle,)

    def get_permissions(self):
        """
        Переопределение метода get_permissions,
        Вставлять разрешения в зависимости от запроса.
        ||
        Redefining the get_permissions method,
        Insert permissions depending on the request.
        """

        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return super(BooksViewSet, self).get_permissions()


class RentLateReturnViewSet(viewsets.ModelViewSet):
    """Аренда/Возврат книги.
    ||
    Book rental/return viewset.
    """
# пересмотреть метод патча
    permission_classes = (permissions.IsAdminUser,)
    pagination_class = PageNumberPagination

    def patch(self, request, rent_id):
        """"Считаем репутацию Читателя.
        || 
        Method counts reader's reputation.
        """

        rent = get_object_or_404(BooksRent, id=rent_id)
        if rent.is_late:
            rent.reader.score -= 1
            rent.reader.score.save()
        else:
            rent.reader.score += 1
            rent.reader.score.save()
        return Response({'success': True})


class ReaderListViewSet(viewsets.ModelViewSet):
    """Представление Читателей.
    ||
    Readers viewset.
    """

    permission_classes = (permissions.IsAdminUser,)
    queryset = Readers.objects.all()
    serializer_class = ReadersSerializer
    pagination_class = PageNumberPagination
