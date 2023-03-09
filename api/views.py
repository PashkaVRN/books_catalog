from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import permissions, viewsets

from book.models import Books

from .serializers import BooksSerializers, UserSerializer

User = get_user_model()


class BooksViewSet(viewsets.ModelViewSet):
    """ Представление Книг."""
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        """
        Переопределение метода get_permissions.
        Вставлять разрешения в зависимости от запроса
        """
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return super(BooksViewSet, self).get_permissions()


class UserViewSet(UserViewSet):
    """" Представление Пользователя. """
    queryset = User.objects.all()
    serializer_class = UserSerializer
