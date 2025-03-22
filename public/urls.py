from django.urls import path, include, re_path

from  .views import set_language, index, confirmation

urlpatterns = [
    path('set-language/', set_language, name='set_language'),
    path('', index, name='index'),
    path('confirmation/', confirmation, name='confirmation'),
    # path('confirmation/', views.confirmation, name='confirmation'),
]
