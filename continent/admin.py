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
    list_display = ('code', 'name', 'superf', 'date_add', 'date_upd', 'activation', 'img')
    list_display_links = ['code', 'name', 'superf', 'date_add', 'date_upd', 'activation', 'img']
    ordering = ('name',)

    inlines = [CountryInline]

    def superf(self, obj):
        return f'{int(obj.superficie)} Km²'
    superf.short_description = 'superficie'


    def img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:100px; border-radius:50%;border:3px solid #fff;box-shadow: 0 0 20px #AAA">')
        except (FileNotFoundError, ValueError) as e:
            return 'Aucun Fichier'
    img.short_description = 'Image'


    def get_contextmenu_items(self, obj):
        return [
            {'title': f"Vue de l'API ({obj.code})", 'url': f'/api/continent/{obj.id}/'},
            {'title': "Base de l'API", 'url': '/api/continent/'},
        ]
