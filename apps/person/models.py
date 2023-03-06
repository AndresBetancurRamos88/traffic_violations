from django.db import models
from apps.base.models import BaseModel


class Person(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        verbose_name='Name',
        blank=False, null=False,
        max_length=50
        )
    last_name = models.CharField(
        verbose_name='Last name',
        blank=False, null=False,
        max_length=50
        )
    email = models.EmailField(
        verbose_name='Email',
        blank=False,
        null=False,
        unique=True
        )

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self) -> str:
        return self.name
