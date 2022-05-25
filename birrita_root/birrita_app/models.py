from django.db import models
from django.utils import timezone


class BeerBrewery(models.Model):
    name = models.CharField(max_length=120)
    web = models.URLField('Web Address', blank=True)

    def __str__(self):
        name = self.name
        return name


class BeersList(models.Model):
    beer_type = models.CharField(max_length=120)
    brewery = models.ForeignKey(
        BeerBrewery, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0.0)
    price_hh = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, default=0.0)
    data_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        beer_type = self.beer_type
        return beer_type
