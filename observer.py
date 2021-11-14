class Observer:
    def __init__(self, market_dict):
        self.market_dict = market_dict
        self.THRESHHOLD = 5/100

    def alert(self):
        symbol_list = [market.get_symbol()
                       for market in self.market_dict.values()]
        coin_headers = zip(*symbol_list)

        for header in coin_headers:
            arbitrage_list = [float(market.get_pair(
                header[id])) for id, market in enumerate(self.market_dict.values())]
            arbitrage_score = abs(
                arbitrage_list[0] - arbitrage_list[1]) / min(arbitrage_list)
            if arbitrage_score > self.THRESHHOLD:

                print("ALERT!!!!", header, arbitrage_score)

            else:
                print("NORMAL!!!!", header, arbitrage_score)
