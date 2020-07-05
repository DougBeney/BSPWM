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

print(
    'BTC', str(getCryptoPrice('btc')), '  ',
    'ETH', str(getCryptoPrice('eth')), '  ',
    'XRP', str(getCryptoPrice('xrp')), '  ',
    'LTC', str(getCryptoPrice('ltc')), '  ',
)
