from django.urls import path
from . import views

urlpatterns = [
    
]


from . import api
from rest_framework import routers

rooter = routers.DefaultRouter()

rooter.register('api/country', api.CountryViewSet, basename='base-api-country')
urlpatterns += rooter.urls

