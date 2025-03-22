from django.contrib import admin
from .models import Appointment, Subscription


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'service', 'date', 'artist', 'comment', 'time_created']
    search_fields = ['name', 'email', 'phone', 'service', 'artist', 'comment']
    list_filter = ['service', 'artist', 'date']
    readonly_fields = ['time_created']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']
    search_fields = ['email']
    readonly_fields = ['subscribed_at']
