from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BooksViewSet, ReaderListView, RentLateReturnView,
                    UserViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('books', BooksViewSet, basename='books')
router.register('users', UserViewSet, basename='users')
router.register('readers', ReaderListView, basename='readers')
router.register('rents', RentLateReturnView, basename='rents')

urlpatterns = [
    path('', include(router.urls)),
]
