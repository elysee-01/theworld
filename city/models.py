from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey("country.Country", on_delete=models.SET_NULL, related_name='country_city', null=True, blank=True)
    area = models.FloatField(max_length=255, help_text='km²', null=True, blank=True) # superficie
    longitude = models.FloatField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(max_length=255, null=True, blank=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return str(self.name)
