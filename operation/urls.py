from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatisticsViewSet

router = DefaultRouter()
router.register(r'statistics', StatisticsViewSet)

urlpatterns = [
    path('statistics', include(router.urls)),
]
