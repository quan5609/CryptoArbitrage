import urllib.request
import urllib.error
import urllib.parse
import json
from market_models import WhiteBit, LBank, MarketFactory
from observer import Observer
import os


market_list = ['WHITEBIT', 'LBANK']
factory = MarketFactory(market_list)
observer = Observer({market: factory.produce(market)
                    for market in market_list})

observer.alert()
