from django.contrib import admin
from actions.action import Action
from . import models


@admin.register(models.City)
class CityAdmin(Action):
    list_display = ('name', 'country', 'area', 'longitude', 'latitude')
    list_display_links = ['name', 'country', 'area', 'longitude', 'latitude']
