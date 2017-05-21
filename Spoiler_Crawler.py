import yahoo_finance

class Crawler(object):
    """ A class to download stock-prices """
    
    def __init__(self, stocks):
        self.stocks = stocks
        
    def __repr__(self):
        return ", ".join(self.stocks)
    
    @staticmethod
    def get_stock_price(stock):
        """ This takes a stock and returns the price of today """
        stock = yahoo_finance.Share(stock)
        return stock.get_price()
    
    def get_prices(self):
        """ Returns a dict of all stocks and their prices """
        return {x:float(self.get_stock_price(x)) for x in self.stocks}




if __name__ == "__main__":
    c = Crawler(["AAPL", "GOOG"])
    result = c.get_prices()
    # Asserts that there are enough results and that they are floats.
    assert len(result) == len(c.stocks)
    assert all(isinstance(x, float) for x in result.values())
    print("Passed Crawlertest!")





