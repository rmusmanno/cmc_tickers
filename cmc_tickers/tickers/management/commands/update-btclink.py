from django.core.management.base import BaseCommand
from  tickers.models import Ticker, TickerHistory

from datetime import timedelta

class Command(BaseCommand):
    help = 'Update tickerId to "symbol_name".'

    def handle(self, *args, **options):
        print("Updating btc link ticker histories...")
        ths = TickerHistory.objects.all()
        for t in ths:
            btcTicker = ths.filter(symbol="BTC", lastAnalyzed__range=[t.lastAnalyzed - timedelta(minutes=10), t.lastAnalyzed]).first()
            t.btcLink = btcTicker
            t.save()