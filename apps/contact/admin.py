from django.contrib import admin

# Register your models here.
from apps.contact import models

class UserFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    list_filter = ('name', 'phone')
    search_fields = ('name', 'phone')
admin.site.register(models.User, UserFilterAdmin)