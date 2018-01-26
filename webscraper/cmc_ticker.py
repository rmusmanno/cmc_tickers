import urllib.request
import json
import requests
import datetime

coin_market_url = 'https://api.coinmarketcap.com/v1/ticker/?limit=100'
server_url = 'http://localhost:8000'


def parseTicker(data):
    ticker = {}

    ticker['tickerId'] = data['id']
    ticker['name'] = data['name']
    ticker['symbol'] = data['symbol']
    ticker['rank'] = data['rank']
    ticker['priceUsd'] = data['price_usd']
    ticker['priceBtc'] = data['price_btc']
    ticker['dayVolumeUsd'] = data['24h_volume_usd']
    ticker['markedCapUsd'] = data['market_cap_usd']
    ticker['availableSupply'] = data['available_supply']
    ticker['totalSupply'] = data['total_supply']
    ticker['maxSupply'] = data['max_supply']
    ticker['percentChange1h'] = data['percent_change_1h']
    ticker['percentChange24h'] = data['percent_change_24h']
    ticker['percentChange7d'] = data['percent_change_7d']
    ticker['lastUpdated'] = datetime.datetime.fromtimestamp(
        int(data['last_updated']))

    datenow = datetime.datetime.now()
    ticker['lastAnalyzed'] = datenow
    ticker['dateAdded'] = datenow

    return ticker


def readCoinMarket(market_url):
    with urllib.request.urlopen(market_url) as url:
        data = json.loads(url.read().decode())
        return data


def saveData(data):
    r = requests.post(server_url + '/tickers/', data=data)
    print(r.status_code, r.reason)
    print(r.content)


def updateData(data, data_id):
    r = requests.put(server_url + '/tickers/' + str(data_id) + '/', data=data)
    print(server_url + '/tickers/' + str(data_id) + '/')
    print(r.status_code, r.reason)
    print(r.content)


def getExistingData(data):
    with urllib.request.urlopen(server_url + '/tickersWithId/' + data['tickerId']) as url:
        data = json.loads(url.read().decode())
        return data


def run():
    coinMarketData = readCoinMarket(coin_market_url)

    for t in coinMarketData:
        ticker = parseTicker(t)
        existingTickers = getExistingData(ticker)

        if len(existingTickers) == 0:
            saveData(ticker)
        else:
            ticker['dateAdded'] = existingTickers[0]['dateAdded']
            updateData(ticker, existingTickers[0]['id'])

run()
