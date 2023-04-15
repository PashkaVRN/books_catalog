from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Readers(AbstractUser):
    """Модель Юзера/Читателя/Посетителя библиотеки.
    ||
    Library User/Reader/Visitor Model.
    """

    USER_ROLE = 'reader'
    MODERATOR_ROLE = 'moderator'
    ADMIN_ROLE = 'admin'
    ROLE_CHOICES = (
        (USER_ROLE, 'reader'),
        (MODERATOR_ROLE, 'moderator'),
        (ADMIN_ROLE, 'admin')
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=100,
        unique=True,
        validators=(UnicodeUsernameValidator(), ),
        help_text='Введите username пользователя'
    )
    first_name = models.CharField(
        verbose_name='Имя читателя',
        max_length=50,
        help_text='Введите Имя'
    )
    last_name = models.CharField(
        verbose_name='Фамилия читателя',
        max_length=50,
        help_text='Введите Фамилию'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='email читателя',
        help_text='Введите электронную почту'
    )
    phone_number = PhoneNumberField(
        unique=True,
        null=False,
        blank=False,
    )
    reputation = models.IntegerField(
        default=10,
        verbose_name='Рейтинг Читателя'
    )
    role = models.CharField(
        max_length=max((len(item) for _, item in ROLE_CHOICES)),
        choices=ROLE_CHOICES,
        default=USER_ROLE,
        verbose_name='Пользовательская роль',
        help_text='Выберите роль пользователя'
    )

    class Meta:
        ordering = ('username', )
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.username

    @property
    def is_moderator(self):
        """True для пользователей с правами модератора. """

        return self.role == Readers.MODERATOR_ROLE

    @property
    def is_admin(self):
        """True для пользователей с правами админа и суперпользователей. """

        return (
            self.role == Readers.ADMIN_ROLE
            or self.is_staff
            or self.is_superuser
        )
