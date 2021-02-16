
from rest_framework import viewsets
from . import serializers
from . import models


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CountrySerializer
    queryset = models.Country.objects.filter(status=True)

