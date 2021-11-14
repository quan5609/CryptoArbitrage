from dotenv import load_dotenv
import json
import pandas as pd
import os
import urllib.request
import urllib.error
import urllib.parse
from assets import lbank_assets, whitebit_assets

load_dotenv()


class MarketFactory:
    def __init__(self, market_list):
        self.market_list = market_list
        self.available_maket = {
            'WHITEBIT': WhiteBit,
            'LBANK': LBank
        }

    def produce(self, name):
        return self.available_maket[name](name)


class Market:
    def __init__(self, name):
        self.URL = os.environ.get(name)
        self.meta_data = self.request_data()

    def update_meta_data(self):
        self.meta_data = self.request_data()

    def request_data(self):
        req = urllib.request.Request(self.URL, headers={
            'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        res = json.loads(res.read().decode("utf8"))
        return self.process_data(res)

    def get_pair(self, symbol):
        pass

    def process_data(self, res):
        pass

    def get_symbol():
        pass


class WhiteBit(Market):
    def get_symbol(self):
        return whitebit_assets.symbol

    def process_data(self, res):
        data = res['result']
        new_data = [{
            'symbol': k,
            'ticker': v['ticker'],
            'timestamp':v['at'],
        } for k, v in data.items()]
        return list(filter(lambda x: '_USDT' in x['symbol'], new_data))

    def get_pair(self, symbol):
        return list(filter(lambda x: x['symbol'] == symbol, self.request_data()))[0]['ticker']['last']


class LBank(Market):
    def get_symbol(self):
        return lbank_assets.symbol

    def process_data(self, res):
        return list(filter(lambda x: '_usdt' in x['symbol'], res['data']))

    def get_pair(self, symbol):
        return list(filter(lambda x: x['symbol'] == symbol, self.request_data()))[0]['ticker']['latest']
