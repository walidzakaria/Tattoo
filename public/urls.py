from django.urls import path, include, re_path

from  .views import set_language, index, services, faq, gallery, confirmation

urlpatterns = [
    path('set-language/', set_language, name='set_language'),
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('faq/', faq, name='faq'),
    path('gallery/', gallery, name='gallery'),
    # path('confirmation/', confirmation, name='confirmation'),
    
]
