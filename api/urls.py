from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BooksViewSet, ReaderListViewSet, RentLateReturnViewSet,
                    UserViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('books', BooksViewSet, basename='books')
router.register('users', UserViewSet, basename='users')
router.register('readers', ReaderListViewSet, basename='readers')
router.register('rents', RentLateReturnViewSet, basename='rents')

urlpatterns = [
    path('', include(router.urls)),
]
