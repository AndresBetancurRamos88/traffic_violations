from django.db import models
from apps.base.models import BaseModel
from apps.person.models import Person


class Vehicle(BaseModel):
    id = models.AutoField(primary_key=True)
    licence_plate = models.CharField(verbose_name='Licence plate', blank=False, null=False, max_length=10)
    branch = models.CharField(verbose_name='Branch', blank=True, null=True, max_length=50)
    color = models.CharField(verbose_name='Color', blank=True, null=True, max_length=50)
    comment = models.TextField(verbose_name='Comments', blank=True, null=True,)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_p')

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles' 

    def __str__(self) -> str:
        return self.licence_plate      