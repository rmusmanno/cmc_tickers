from rest_framework import generics, permissions
from rest_framework.response import Response

from django.http import Http404
from django.shortcuts import render

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
