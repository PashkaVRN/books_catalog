from rest_framework import viewsets

from book.models import Books

from .serializers import BooksSerializers


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
