from django.contrib import admin
from actions.action import Action
from django.utils.safestring import mark_safe
from . import models
from country import models as models_country


class CountryInline(admin.TabularInline):
    model = models_country.Country
    extra = 0


@admin.register(models.Continent)
class ContinentAdmin(Action):
    list_display = ('code', 'name', 'superficie', 'date_add', 'date_upd', 'activation', 'img')
    list_display_links = ['code', 'name', 'superficie', 'date_add', 'date_upd', 'activation', 'img']

    inlines = [CountryInline]

    def img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:50px">')
        except (FileNotFoundError, ValueError) as e:
            return 'Aucun Fichier'
    img.short_description = 'Image'

    def get_contextmenu_items(self, obj):
        return [
            {'title': 'Lien 1', 'url': '/'},
            {'title': 'Lien 2', 'url': '/'},
        ]