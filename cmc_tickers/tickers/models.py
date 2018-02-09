from django.db import models
from django.conf import settings

from django.db.models.signals import post_save, pre_save

import django.utils.timezone
from datetime import timedelta

from tickers.signals import UpdateCustomManager, post_update


class Ticker(models.Model):
    objects = UpdateCustomManager()

    tickerId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    rank = models.IntegerField()
    priceUsd = models.FloatField(null=True, blank=True)
    priceBtc = models.FloatField(null=True, blank=True)
    dayVolumeUsd = models.FloatField(null=True, blank=True)
    dayVolumeBtc = models.FloatField(null=True, blank=True)
    dayVolumeBtcVariation = models.FloatField(null=True, blank=True)
    marketCapUsd = models.FloatField(null=True, blank=True)
    marketCapBtc = models.FloatField(null=True, blank=True)
    availableSupply = models.FloatField(null=True, blank=True)
    totalSupply = models.FloatField(null=True, blank=True)
    maxSupply = models.FloatField(null=True, blank=True)
    percentChange1h = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2)
    percentChange24h = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2)
    percentChange7d = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2)

    btcPercentChange1h = models.FloatField(null=True, blank=True)
    btcPercentChange24h = models.FloatField(null=True, blank=True)
    btcPercentChange7d = models.FloatField(null=True, blank=True)

    lastUpdated = models.DateTimeField()

    dateAdded = models.DateTimeField(default=django.utils.timezone.now)
    lastAnalyzed = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name


class TickerHistory(models.Model):
    tickerId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    rank = models.IntegerField()
    priceUsd = models.FloatField(null=True, blank=True)
    priceBtc = models.FloatField(null=True, blank=True)
    dayVolumeUsd = models.FloatField(null=True, blank=True)
    dayVolumeBtc = models.FloatField(null=True, blank=True)
    dayVolumeBtcVariation = models.FloatField(null=True, blank=True)
    marketCapUsd = models.FloatField(null=True, blank=True)
    marketCapBtc = models.FloatField(null=True, blank=True)
    availableSupply = models.FloatField(null=True, blank=True)
    totalSupply = models.FloatField(null=True, blank=True)
    maxSupply = models.FloatField(null=True, blank=True)
    percentChange1h = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2)
    percentChange24h = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2)
    percentChange7d = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2)

    btcPercentChange1h = models.FloatField(null=True, blank=True)
    btcPercentChange24h = models.FloatField(null=True, blank=True)
    btcPercentChange7d = models.FloatField(null=True, blank=True)

    lastUpdated = models.DateTimeField()

    dateAdded = models.DateTimeField()
    lastAnalyzed = models.DateTimeField()

    def __str__(self):
        return self.name + " [" + str(self.lastAnalyzed) + "]"

    class Meta:
        verbose_name_plural = 'ticker histories'


def calculate_variation(sender, instance, *args, **kwargs):

	# Day volume variation
    x = settings.DAILY_HOUR_VARIATION_ERROR
    lastDayInstance = TickerHistory.objects.filter(
        lastAnalyzed__range=[instance.lastAnalyzed - timedelta(hours=24+x), instance.lastAnalyzed - timedelta(hours=24-x)]).order_by('-lastAnalyzed').first()

    if lastDayInstance:
        if instance.dayVolumeBtc and lastDayInstance.dayVolumeBtc:
            instance.dayVolumeBtcVariation = instance.dayVolumeBtc - lastDayInstance.dayVolumeBtc
        else:
            instance.dayVolumeBtcVariation = None
    else:
        instance.dayVolumeBtcVariation = None

    # BTC percent change 1h
    x = settings.HOUR_VARIATION_ERROR
    lastHour = TickerHistory.objects.filter(
        lastAnalyzed__range=[instance.lastAnalyzed - timedelta(minutes=60+x), instance.lastAnalyzed - timedelta(minutes=60-x)]).all()

    if lastHour:
        instance.btcPercentChange1h = sum(l.priceBtc for l in lastHour) / len(lastHour)
    else:
        instance.btcPercentChange1h = None

    # BTC percent change 24h
    x = settings.DAILY_HOUR_VARIATION_ERROR
    lastDay = TickerHistory.objects.filter(
        lastAnalyzed__range=[instance.lastAnalyzed - timedelta(hours=24+x), instance.lastAnalyzed - timedelta(hours=24-x)]).all()

    if lastDay:
        instance.btcPercentChange24h = sum(l.priceBtc for l in lastDay) / len(lastDay)
    else:
        instance.btcPercentChange24h = None

    # BTC percent change 7d
    x = settings.WEEKLY_HOUR_VARIATION_ERROR
    lastWeek = TickerHistory.objects.filter(
        lastAnalyzed__range=[instance.lastAnalyzed - timedelta(hours=168+x), instance.lastAnalyzed - timedelta(hours=168-x)]).all()

    if lastWeek:
        instance.btcPercentChange7d = sum(l.priceBtc for l in lastWeek) / len(lastWeek)
    else:
        instance.btcPercentChange7d = None


def save_ticker_history(sender, instance, created, **kwargs):
    TickerHistory.objects.create(tickerId=instance.tickerId,
                                 name=instance.name,
                                 symbol=instance.symbol,
                                 rank=instance.rank,
                                 priceUsd=instance.priceUsd,
                                 priceBtc=instance.priceBtc,
                                 dayVolumeUsd=instance.dayVolumeUsd,
                                 dayVolumeBtc=instance.dayVolumeBtc,
                                 marketCapUsd=instance.marketCapUsd,
                                 marketCapBtc=instance.marketCapBtc,
                                 availableSupply=instance.availableSupply,
                                 totalSupply=instance.totalSupply,
                                 maxSupply=instance.maxSupply,
                                 percentChange1h=instance.percentChange1h,
                                 percentChange24h=instance.percentChange24h,
                                 percentChange7d=instance.percentChange7d,
                                 btcPercentChange1h=instance.btcPercentChange1h,
                                 btcPercentChange24h=instance.btcPercentChange24h,
                                 btcPercentChange7d=instance.btcPercentChange7d,
                                 lastUpdated=instance.lastUpdated,
                                 dateAdded=instance.dateAdded,
                                 lastAnalyzed=instance.lastAnalyzed)

pre_save.connect(calculate_variation, sender=Ticker)
post_save.connect(save_ticker_history, sender=Ticker)
post_update.connect(save_ticker_history, sender=Ticker)
