from django.contrib import admin
import timeago
from  tickers.models import *
from  tickers.utils import * # get_time_ago, get_day_trading_of_mcap_percent, format_using_humanize
import datetime
from django.utils.safestring import mark_safe
import humanize
#admin.site.register(tickers.models.Ticker)
#admin.site.register(TickerHistory)

def format_time_ago_lastUpdated(obj):
    return get_time_ago(obj.lastUpdated, datetime.datetime.now())
    #return timeago.format(obj.lastUpdated.replace(tzinfo=None) , datetime.datetime.now().replace(tzinfo=None))
format_time_ago_lastUpdated.short_description = 'last Updated'
format_time_ago_lastUpdated.allow_tags = True
format_time_ago_lastUpdated.admin_order_field = 'lastUpdated'

def format_time_ago_dateAdded(obj):
    return get_time_ago(obj.dateAdded, datetime.datetime.now())

format_time_ago_dateAdded.short_description = 'date Added'
format_time_ago_dateAdded.allow_tags = True
format_time_ago_dateAdded.admin_order_field = 'dateAdded'


def format_day_trading_to_market_cap_percent(obj):
    return  get_day_trading_of_mcap_percent(obj.dayVolumeUsd, obj.marketCapUsd) #
format_day_trading_to_market_cap_percent.short_description = 'day trading/mcap'
format_day_trading_to_market_cap_percent.allow_tags = True
format_day_trading_to_market_cap_percent.admin_order_field = 'dayVolumeUsd'


# https://coinmarketcap.com/currencies/iostoken/
def format_name(obj):
    return  mark_safe('%s (%s)<br>'\
                    '<small>'\
                    '<a href="https://coinmarketcap.com/currencies/%s/" target=_blank>https://coinmarketcap.com/currencies/%s/</a>'\
                    '&nbsp;&nbsp;'\
                    '(<a href="/admin/tickers/tickerhistory/?q=%s" target=_blank>HF</a>)'\
                    '&nbsp;&nbsp;'\
                    '(<a href="https://www.tradingview.com/symbols/%sBTC/" target=_blank>TV</a>)'\
                    '</small><br><i>%s</i>' %
                    (obj.name, obj.symbol, str(obj.name).lower().replace(" ", "-"), str(obj.name).lower().replace(" ", "-"), obj.symbol.upper(), obj.symbol.upper(), obj.tickerId ))

format_name.short_description = 'name'
format_name.admin_order_field = 'name'


def format_marketCapUsd(obj):
    return format_using_humanize(obj.marketCapUsd, humanize.intword)
format_marketCapUsd.short_description = 'marketCapUsd'
format_marketCapUsd.admin_order_field = 'marketCapUsd'

def format_dayVolumeUsd(obj):
    return format_using_humanize(obj.dayVolumeUsd, humanize.intword)
format_dayVolumeUsd.short_description = 'dayVolumeUsd'
format_dayVolumeUsd.admin_order_field = 'dayVolumeUsd'


#

@admin.register(Ticker)
class TickerAdmin(admin.ModelAdmin):
    list_display = ('rank', format_name,  'priceBtc', 'priceUsd', format_dayVolumeUsd, 'percentChange24h', format_marketCapUsd,  format_time_ago_lastUpdated, format_time_ago_dateAdded, format_day_trading_to_market_cap_percent)
    ordering = ('rank', )
    list_filter = ('symbol',)
    search_fields = ['name', 'symbol' ]
    list_per_page = 500

@admin.register(TickerHistory)
class TickerHistoryAdmin(admin.ModelAdmin):
    list_display = ('rank', format_name,  'priceBtc', 'priceUsd', format_dayVolumeUsd,  'percentChange24h', format_marketCapUsd, format_time_ago_lastUpdated, format_day_trading_to_market_cap_percent)
    ordering = ('-lastUpdated', )
    list_filter = ('symbol', 'tickerId')
    search_fields = [ 'symbol', 'tickerId' ]
    list_per_page = 500
