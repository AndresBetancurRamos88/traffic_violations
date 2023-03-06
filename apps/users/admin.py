from django.contrib import admin
from .models import User

class PersonAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'last_name', 'id')
    list_filter = ('user_id',)

admin.site.register(User, PersonAdmin)