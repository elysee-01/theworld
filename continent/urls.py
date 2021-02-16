from django.urls import path
from . import views

urlpatterns = [
    
]


from . import api
from rest_framework import routers

rooter = routers.DefaultRouter()

rooter.register('api/continent', api.ContinentViewSet, basename='base-api-continent')
urlpatterns += rooter.urls

