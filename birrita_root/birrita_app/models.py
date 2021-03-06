from django.db import models
from django.utils import timezone


class BarList(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        name = self.name
        return name


class BeersList(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        name = self.name
        return name


class BreweriesList(models.Model):
    name = models.CharField(max_length=120)
    web = models.URLField('Web Address', blank=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        brewery = self.name
        return brewery


class BreweryList(models.Model):
    bar_name = models.ForeignKey(
            BarList, null=True, on_delete=models.CASCADE)
    brewery = models.ForeignKey(
        BreweriesList, null=True, on_delete=models.CASCADE)
    beer_type = models.ForeignKey(
        BeersList, null=True, on_delete=models.CASCADE)

    price = models.IntegerField(default=0)
    price_hh = models.IntegerField(default=0)
    data_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-data_date"]

    def __str__(self):
        brewery = self.brewery
        return brewery
