from django.contrib import admin
from apps.secondary import models
# Register your models here.

class ContactsFilterAdmin(admin.ModelAdmin):
    list_display = ('description', 'phone')
    list_filter = ('description',)
    search_fields = ('description',)
admin.site.register(models.Contact, ContactsFilterAdmin)
admin.site.register(models.Photo)
admin.site.register(models.Reservation)