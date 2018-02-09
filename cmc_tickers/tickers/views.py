from rest_framework import generics, permissions
from rest_framework.response import Response

from django.http import Http404
from django.shortcuts import render, redirect
from django.conf import settings
from datetime import timedelta

import tickers.models
import tickers.serializers

from tickers.models import TickerHistory, Ticker

"""
TICKER
"""


class TickerListCreate(generics.ListCreateAPIView):
    serializer_class = tickers.serializers.TickerSerializer
    queryset = tickers.models.Ticker.objects.all()


class TickerDetail(generics.RetrieveUpdateAPIView):
    serializer_class = tickers.serializers.TickerSerializer
    queryset = tickers.models.Ticker.objects.all()


class TickerWithId(generics.ListAPIView):
    serializer_class = tickers.serializers.TickerSerializer

    def get_queryset(self):
        tickerId = self.kwargs['tickerId']
        return tickers.models.Ticker.objects.filter(tickerId=tickerId)


def rank_chart(request, tickerId):
    try:
        th = TickerHistory.objects.filter(tickerId=tickerId)
    except TickerHistory.DoesNotExist:
        raise Http404("Ticker does not exist")
    return render(request, 'tickers/chart.html', {'ticker_history': th, 'ticker_id': tickerId})

def index(request):
    tickers = Ticker.objects.all()
    return render(request, 'tickers/chart_list.html', {'tickers': tickers})

def updateTickerPercents(request):
    ths = TickerHistory.objects.all()
    for th in ths:
        onceCalculateVariations(th)

    ts = Ticker.objects.all()
    for t in ts:
        t.save()

    return redirect('index')


def onceCalculateVariations(instance):

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

    instance.save()