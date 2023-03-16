from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have "is_staff" = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have "is_superuser" = True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=150,
        verbose_name='Почта',
        unique='True'
    )
    avatar = models.ImageField(upload_to='avatar/', **NULLABLE, verbose_name='Аватарка')
    phone = models.CharField(max_length=20, **NULLABLE, verbose_name='Телефон')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна')
    password = models.CharField(max_length=150, help_text='', verbose_name='Пароль')
    verify_token = models.CharField(max_length=35, verbose_name='Токен верификации', **NULLABLE)
    verify_token_expired = models.DateTimeField(**NULLABLE, verbose_name='Дата истечения токена')
    new_password = models.CharField(verbose_name="новый пароль", max_length=128, **NULLABLE)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email} {self.country}'
