from django.contrib import admin

from .models import Statistics, Category

# Register your models here.
@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('info', 'value', 'logo')
    search_fields = ('info', 'value', 'logo')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name', )
