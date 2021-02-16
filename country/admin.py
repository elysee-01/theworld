from django.contrib import admin
from actions.action import Action
from django.utils.safestring import mark_safe
from . import models
from city import models as models_city


class CityInline(admin.TabularInline):
    model = models_city.City
    extra = 0


@admin.register(models.Country)
class CountryAdmin(Action):
    list_display = ('name', 'iso', 'iso3', 'telephone_prefix', 'capital', 'continent', 'activation', 'drp')
    list_display_links = ['name', 'iso', 'iso3', 'telephone_prefix', 'capital', 'continent']
    list_filter = ['status', 'continent']
    search_fields = ['name', 'iso', 'iso3', 'capital', 'continent']

    inlines = [CityInline]

    def drp(self, obj):
        try:
            return mark_safe(f'<img src="{obj.drapeau.url}" style="height:10px; width:15px">')
        except (FileNotFoundError, ValueError) as e:
            return 'Aucun Fichier'
    drp.short_description = 'Drapeau'

    def get_contextmenu_items(self, obj):
        return [
            {'title': 'Lien 1', 'url': '/'},
            {'title': 'Lien 2', 'url': '/'},
        ]
