from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(
        verbose_name='Creation Date', auto_now=False,
        auto_now_add=True
        )
    modified_date = models.DateTimeField(
        verbose_name='Modified Date',
        auto_now=True,
        auto_now_add=False
        )

    class Meta:
        abstract = True
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'
