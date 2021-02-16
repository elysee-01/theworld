from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    superficie = models.FloatField(max_length=255, help_text='km²', null=True, blank=True)
    image = models.FileField(upload_to='images/continent', null=True, blank=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Continent'
        verbose_name_plural = 'Continents'

    def __str__(self):
        return str(self.name)
