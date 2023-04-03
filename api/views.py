from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from book.models import Books, BooksRent, Readers

from .serializers import (BooksSerializers, ReadersSerializer,
                          UserSerializer)

User = get_user_model()


class UserViewSet(UserViewSet):
    """Представление Пользователя.
    ||
    User viewset.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class BooksViewSet(viewsets.ModelViewSet):
    """Представление Книг.
    ||
    Books viewset.
    """

    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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

    permission_classes = (permissions.IsAdminUser,)

    def patch(self, request, rent_id):
        """"Считаем репутацию Читателя.
        || 
        Method counts reader's reputation."""

        rent = get_object_or_404(BooksRent, id=rent_id)
        if rent.is_late:
            rent.reader.reputation.score -= 1
            rent.reader.reputation.save()
        else:
            rent.reader.reputation.score += 1
            rent.reader.reputation.save()
        return Response({'success': True})


class ReaderListViewSet(viewsets.ModelViewSet):
    """Представление Читателей.
    ||
    Readers viewset.
    """

    permission_classes = (permissions.IsAdminUser,)
    queryset = Readers.objects.all()
    serializer_class = ReadersSerializer
