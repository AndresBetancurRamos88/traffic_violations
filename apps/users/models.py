from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )


class UserManager(BaseUserManager):
    def _create_user(self, user_id, name, last_name, is_staff,
                     is_superuser, password, **extra_fields
                     ):

        user = self.model(
            user_id=user_id,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, user_id, name, last_name,
                    password=None, **extra_fields
                    ):
        return self._create_user(user_id, name, last_name,
                                 False, False, password, **extra_fields
                                 )

    def create_superuser(self, user_id, name, last_name,
                         password=None, **extra_fields
                         ):
        return self._create_user(user_id, name, last_name,
                                 True, True, password, **extra_fields
                                 )


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.IntegerField('User id', unique=True)
    name = models.CharField('Name', max_length=50, blank=True, null=True)
    last_name = models.CharField(
        'last name',
        max_length=50,
        blank=True,
        null=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Officer'
        verbose_name_plural = 'Officers'

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name', 'last_name']

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
