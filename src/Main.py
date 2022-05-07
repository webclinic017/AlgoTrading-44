# Import Data Module
from Data.Client import Client
from Data.Historical import get_historical_data

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters
from Indicators.LeastSquares import get_least_squares
from Indicators.DecisionTree import get_decision_tree
from Indicators.Ridge import get_ridge
from Indicators.BayesRidge import get_bayes_ridge

# Import Examples Module
from Examples.Individual import individual_backtest
from Examples.Pairs import pairs_backtest
from Examples.Optimized import optimized_backtest
from Examples.Live import live_trading

import time 
import numpy as np
import matplotlib.pyplot as plt
from TickerSymbols import get_ticker_symbols

if __name__ == "__main__":

    def main():

        isDisplay = True

        # Semiconductor Stocks
        # tickers = np.array(["MU", "NVDA", "AMD", "QCOM", "INTC", "AMAT", "TXN", "LRCX", "TSM", "AVGO"])

        # Multidimensional Array
        tickers = get_ticker_symbols()

        for i in range(len(tickers)):

            # Step One: Initialize Client
            endpoint = "sandbox.tradier.com"
            api_key = "0qoGJZUqxFSc7zcBcAENRphluKVn"
            accountid = 0
            ticker = tickers[i]
            months = 60
            client = Client(endpoint, api_key, accountid, ticker, months)

            # Step Two: Fetch Historical Data
            ohlcA = get_historical_data(client)

            rolling_period = 10
            projection = 0
            # individual_backtest(ohlcA, rolling_period, projection, isDisplay)
            # print(tickers[i], ": Backtest Complete. ")

            ticker = "TXN"
            client = Client(endpoint, api_key, accountid, ticker, months)
            ohlcB = get_historical_data(client)
            pairs_backtest(ohlcA, ohlcB, isDisplay)

            # lower = 5
            # upper = 90
            # optimized_backtest(ohlcA, lower, upper, get_least_squares, projection, isDisplay)
            # print(tickers[i], ": Optimization Complete. ")

            print("Limiting API Calls")
            print("Sleeping...")
            time.sleep(2)
            break

        # Limit Number of Charts
        if isDisplay == True:
            plt.show()

        return 0

    # Call Main Method
    main()







