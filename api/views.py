from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from django.core.exceptions import PermissionDenied

from book.models import Books, BooksRent
from user.models import Readers

from .permissions import IsAdminModeratorOrSuperUser, IsAdminOrReadOnly
from .serializers import BooksSerializers, UserSerializer


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
