from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('licence_plate', 'branch', 'color', 'person')
    list_filter = ('licence_plate', 'person')


admin.site.register(Vehicle, VehicleAdmin)