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
    search_fields = ['name', 'iso', 'iso3']

    inlines = [CityInline]

    def drp(self, obj):
        try:
            return mark_safe(f'<img src="{obj.drapeau.url}" style="height:100px; width:150px;border-radius:5px;border:5px solid #fff;box-shadow: 0 0 20px #AAA">')
        except (FileNotFoundError, ValueError) as e:
            return 'Aucun Fichier'
    drp.short_description = 'Drapeau'

    def get_contextmenu_items(self, obj):
        return [
            {'title': f"Vue de l'API ({obj.iso})", 'url': f'/api/country/{obj.id}/'},
            {'title': "Base de l'API", 'url': '/api/country/'},
        ]
