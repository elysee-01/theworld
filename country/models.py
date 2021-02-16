from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    official_name = models.CharField(max_length=255, null=True, blank=True)
    fr_name = models.CharField(max_length=255, null=True, blank=True)
    en_name = models.CharField(max_length=255, null=True, blank=True)
    iso = models.CharField(max_length=255, null=True, blank=True)
    iso3 = models.CharField(max_length=255, null=True, blank=True)
    telephone_prefix = models.CharField(max_length=255, null=True, blank=True, verbose_name='Prefix')
    longitude = models.FloatField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(max_length=255, null=True, blank=True)

    capital = models.OneToOneField("city.City", on_delete=models.SET_NULL, related_name='country_capital', null=True, blank=True)
    continent = models.ForeignKey("continent.Continent", on_delete=models.SET_NULL, related_name='country_capital', null=True, blank=True)

    drapeau = models.FileField(upload_to='flags/', null=True, blank=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return str(self.name)
