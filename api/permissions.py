from django.contrib.auth import get_user_model
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework import permissions

User = get_user_model()


class IsAdminOrReadOnly(BasePermission):
    """
    Пользователь является супрюзером джанго
    или имеет роль администратора.
    Просмотр доступен всем пользователям.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or (request.user.is_authenticated
                and request.user.is_admin)
        )


class IsAdminModeratorOrSuperUser(permissions.IsAdminUser):
    """
    Пользователь является суперюзером джанго
    или имеет роль администратора или модератора
    для просмотра информации.
    """

    def has_permission(self, request, view):
        return request.user and (
            request.user.is_superuser or request.user.is_staff)
