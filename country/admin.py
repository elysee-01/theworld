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
    list_display = ('name', 'official_name', 'iso', 'iso3', 'capital', 'continent', 'telephone_prefix', 'activation', 'drp')
    list_display_links = ['name', 'official_name', 'iso', 'iso3', 'capital', 'continent', 'telephone_prefix', 'drp']

    inlines = [CityInline]

    def drp(self, obj):
        try:
            return mark_safe(f'<img src="{obj.drapeau.url}" style="height:100px; width:100px">')
        except (FileNotFoundError, ValueError) as e:
            return 'Aucun Fichier'
    drp.short_description = 'Drapeau'
