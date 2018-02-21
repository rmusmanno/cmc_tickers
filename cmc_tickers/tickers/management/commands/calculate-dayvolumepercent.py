from django.core.management.base import BaseCommand
from  tickers.models import Ticker, TickerHistory

class Command(BaseCommand):
    help = 'Update ticker and tickerhistory day volume to market cap percent.'

    def handle(self, *args, **options):
        print("Updating tickers...")
        ts = Ticker.objects.all()
        for t in ts:
            t.dayVolumeToMCAPPercentUsd = (t.dayVolumeUsd * 100) / t.marketCapUsd
            t.dayVolumeToMCAPPercentBtc = (t.dayVolumeBtc * 100) / t.marketCapBtc
            t.save()
        print("Updating ticker histories...")
        ths = TickerHistory.objects.all()
        for t in ths:
            t.dayVolumeToMCAPPercentUsd = (t.dayVolumeUsd * 100) / t.marketCapUsd
            t.dayVolumeToMCAPPercentBtc = (t.dayVolumeBtc * 100) / t.marketCapBtc
            t.save()