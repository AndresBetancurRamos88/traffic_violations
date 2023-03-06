from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'id')
    list_filter = ('email',)


admin.site.register(Person, PersonAdmin)
