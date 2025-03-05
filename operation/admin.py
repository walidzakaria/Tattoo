from django.contrib import admin

from .models import Statistics

# Register your models here.
@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('info', 'value', 'logo')
    search_fields = ('info', 'value', 'logo')

