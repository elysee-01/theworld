from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('continent/', include('continent.urls')),
    path('country/', include('country.urls')),
    path('city/', include('city.urls')),
]



from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
