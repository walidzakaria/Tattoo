
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView, RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

schema_view = get_schema_view(
    openapi.Info(
        title="Tattoo REST APIs",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="walidpiano@yahoo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('explorer/', include('explorer.urls')),
    path('api/', include('operation.urls'), name='api'),
    path('', include('public.urls'), name='public'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Tattoo Admin'
admin.site.site_title = 'Tattoo Admin'
admin.site.index_title = 'Welcome to Tattoo'
