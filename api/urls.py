from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BooksViewSet, ReaderListViewSet,
                    RentLateReturnViewSet, UserViewSet)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('books', BooksViewSet, basename='books')
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('readers', ReaderListViewSet, basename='readers')
router_v1.register('rents', RentLateReturnViewSet, basename='rents')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
