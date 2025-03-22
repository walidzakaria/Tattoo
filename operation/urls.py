from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, SubscriptionViewSet, confirmation

router = DefaultRouter()

router.register('appointments', AppointmentViewSet, basename='appointments')
router.register('subscriptions', SubscriptionViewSet, basename='subscriptions')

urlpatterns = [
    path('confirmation/', confirmation, name='confirmation'),
]

urlpatterns += router.urls

