from django.contrib import admin
from actions.action import Action
from . import models


@admin.register(models.City)
class CityAdmin(Action):
    list_display = ('name', 'country', 'area', 'longitude', 'latitude')
    list_display_links = ['name', 'country', 'area', 'longitude', 'latitude']

    def get_contextmenu_items(self, obj):
        return [
            {'title': 'Lien 1', 'url': '/'},
            {'title': 'Lien 2', 'url': '/'},
        ]