#!/usr/bin/env python3

import requests
import json
from time import sleep

def getCryptoPrice(ticker):
    URL = "https://www.bitstamp.net/api/v2/ticker/%susd/" % ticker
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)["last"])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

space = ''.join([' ' for i in range(0,4)])

print(
    '%{F#8BE9FD}',
    '%{T4}',
    'BTC', str(getCryptoPrice('btc')), space,
    'ETH', str(getCryptoPrice('eth')), space,
    'XRP', str(getCryptoPrice('xrp')), space,
    'LTC', str(getCryptoPrice('ltc')), space,
    '%{T-}',
    '%{B- F-}',
)
