from django.core.management.base import BaseCommand
from  tickers.models import Ticker, TickerHistory

class Command(BaseCommand):
    help = 'Update tickerId to "symbol_name".'

    def handle(self, *args, **options):
        print("Updating tickers...")
        ts = Ticker.objects.all()
        for t in ts:
            t.tickerId = str(t.symbol) + '_' + str(t.name)
            t.save()
        print("Updating ticker histories...")
        ths = TickerHistory.objects.all()
        for t in ths:
            t.tickerId = str(t.symbol) + '_' + str(t.name)
            t.save()