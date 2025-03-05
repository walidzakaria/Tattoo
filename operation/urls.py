from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatisticsViewSet, CategoryViewSet

router = DefaultRouter()

router.register('statistics', StatisticsViewSet, basename='statistics')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = router.urls

