from django.db import models


class Ticker(models.Model):
    tickerId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    rank = models.IntegerField()
    priceUsd = models.FloatField(null=True, blank=True)
    priceBtc = models.FloatField(null=True, blank=True)
    dayVolumeUsd = models.FloatField(null=True, blank=True)
    markedCapUsd = models.FloatField(null=True, blank=True)
    availableSupply = models.FloatField(null=True, blank=True)
    totalSupply = models.FloatField(null=True, blank=True)
    maxSupply = models.FloatField(null=True, blank=True)
    percentChange1h = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    percentChange24h = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    percentChange7d = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    lastUpdated = models.DateTimeField()

    dateAdded = models.DateTimeField()
    lastAnalyzed = models.DateTimeField()

    def __str__(self):
        return self.name
