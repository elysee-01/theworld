
from rest_framework import serializers
from . import models


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Continent
        fields = '__all__'
        # depth = 1

