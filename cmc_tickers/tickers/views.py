from rest_framework import generics, permissions
from rest_framework.response import Response

import tickers.models
import tickers.serializers

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