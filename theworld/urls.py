from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

from country import api as api_country
from continent import api as api_continent


rooter = routers.DefaultRouter()
rooter.register('country', api_country.CountryViewSet, basename='base-api-country')
rooter.register('continent', api_continent.ContinentViewSet, basename='base-api-continent')


schema_view = get_schema_view(
    openapi.Info(
        title="The World API",
        default_version='v1',
        description="Documentation de l'API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="elyseekevin49@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('continent/', include('continent.urls')),
    path('country/', include('country.urls')),
    path('city/', include('city.urls')),

    path('api/', include(rooter.urls)),

    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
