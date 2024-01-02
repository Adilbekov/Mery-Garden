from django.contrib import admin

# Register your models here.
from apps.base import models

class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'description', 'prise')
    list_display = ('title', 'description')
    search_fields = ('title', 'description', 'prise')
admin.site.register(models.Slide, SlideFilterAdmin)

class ConditionFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions', 'phone' )
    list_display = ('descriptions', 'phone')
    search_fields = ('descriptions', 'phone') 
admin.site.register(models.Condition, ConditionFilterAdmin)

admin.site.register(models.News)
admin.site.register(models.Service)

class BossFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
    search_fields = ('title', 'description') 
admin.site.register(models.Boss, BossFilterAdmin)

class ComandsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',) 
admin.site.register(models.Comands, ComandsFilterAdmin)

class AssFilterAdmin(admin.ModelAdmin):
    list_filter = ('description', 'phone')
    list_display = ('description', 'phone')
    search_fields = ('description', 'phone') 
admin.site.register(models.Ass, AssFilterAdmin)

admin.site.register(models.Video)