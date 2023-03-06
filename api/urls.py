from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BooksViewSet

app_name = 'api'

router = DefaultRouter()
router.register('books', BooksViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
]
