# Import Data Module
from Data.Historical import get_historical_data
from Data.Quotes import get_quote

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters
from Indicators.LeastSquares import get_least_squares
from Indicators.DecisionTree import get_decision_tree
from Indicators.Ridge import get_ridge
from Indicators.BayesRidge import get_bayes_ridge

# Import Account Module
from Account.Client import Order
from Account.Orders import place_equity_order

# Import Python Libraries
import time

def live_trading(client, indicator, quantity):
    """
    After backtesting a select strategy, begin live trading or paper trading
    """

    # Fetch Historical Data
    ohlc = get_historical_data(client)
    position = False

    while True:

        # Fetch Quote 
        print("Fetching Stock Price")
        quote = get_quote(client)
        stock_price = quote
        print("Stock Price: ", stock_price)

        # Compute Indicator
        period = par.period
        projection = 0
        par = Parameters(period, projection)

        open = ohlc.open[period:]
        high = ohlc.high[period:]
        low = ohlc.low[period:]
        close = ohlc.close[period:]

        print("Computing Indicator")
        indicator_average = indicator(par, close)
        print("Indicator: ", indicator_average[-1])

        # Enter Long Position
        if stock_price < indicator_average[-1] and position == False:

            order = Order(client.accountid, client.ticker, "buy", quantity, "Limit", "day", stock_price)
            place_equity_order(client, order)
            print("Long Position Entry")

        # Exit Long Position
        if stock_price > indicator_average[-1] and position == True:

            order = Order(client.accountid, client.ticker, "sell", quantity, "Limit", "day", stock_price)
            place_equity_order(client, order)
            print("Long Position Exit")

        # Enter Short Position
        if stock_price > indicator_average[-1] and position == False:

            order = Order(client.accountid, client.ticker, "sell_short", quantity, "Limit", "day", stock_price)
            place_equity_order(client, order)
            print("Short Position Entry")

        # Exit Short 
        if stock_price < indicator_average[-1] and position == True:

            order = Order(client.accountid, client.ticker, "buy_to_cover", quantity, "Limit", "day", stock_price)
            place_equity_order(client, order)
            print("Short Position Exit")

        print("Sleeping for 15 Minutes")
        time.Sleep(15)

    return 0