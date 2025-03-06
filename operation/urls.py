from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatisticsViewSet, CategoryViewSet, index, confirmation

router = DefaultRouter()

router.register('statistics', StatisticsViewSet, basename='statistics')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', index, name='index'),
    path('confirmation/', confirmation, name='confirmation'),
]

urlpatterns += router.urls

