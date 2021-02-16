
from rest_framework import viewsets
from . import serializers
from . import models


class ContinentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContinentSerializer
    queryset = models.Continent.objects.filter(status=True)

