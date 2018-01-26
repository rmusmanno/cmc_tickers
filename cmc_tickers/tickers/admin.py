from django.contrib import admin

import tickers.models

admin.site.register(tickers.models.Ticker)