# Import Data Module
from Data.Client import Client
from Data.Historical import get_historical_data

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters
from Indicators.BollingerBands import get_bollinger_bands
from Indicators.LeastSquares import get_least_squares
from Indicators.DecisionTree import get_decision_tree
from Indicators.Ridge import get_ridge
from Indicators.BayesRidge import get_bayes_ridge

# Import Examples Module
from Examples.Individual import individual_backtest
from Examples.Pairs import pairs_backtest
from Examples.Optimized import optimized_backtest
from Examples.Live import live_trading

if __name__ == "__main__":

    def main():

        # Step One: Initialize Client
        endpoint = "sandbox.tradier.com"
        api_key = "0qoGJZUqxFSc7zcBcAENRphluKVn"
        accountid = 0
        ticker = "AAPL"
        months = 60
        client = Client(endpoint, api_key, accountid, ticker, months)

        # Step Two: Fetch Historical Data
        ohlcA = get_historical_data(client)
        # individual_backtest(ohlcA)

        ticker = "MSFT"
        client = Client(endpoint, api_key, accountid, ticker, months)
        ohlcB = get_historical_data(client)

        pairs_backtest(ohlcA, ohlcB)

        # lower = 20
        # upper = 60
        # optimized_backtest(ohlcA, lower, upper, get_least_squares)

        return 0

    # Call Main Method
    main()







