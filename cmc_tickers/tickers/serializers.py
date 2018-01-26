from rest_framework import serializers

import tickers.models


class TickerSerializer(serializers.ModelSerializer):

    class Meta:
        model = tickers.models.Ticker
        fields = '__all__'