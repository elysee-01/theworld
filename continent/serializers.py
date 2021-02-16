
from rest_framework import serializers
from . import models
from country.models import Country


class NewCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'name',
            'official_name',
            'iso',
            'iso3',
            'telephone_prefix',
            'capital',
            'drapeau'
        )


class ContinentSerializer(serializers.ModelSerializer):
    continent_countries = NewCountrySerializer(many=True, required=False)
    class Meta:
        model = models.Continent
        fields = '__all__'
