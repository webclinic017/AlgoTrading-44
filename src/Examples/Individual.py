# Import Backtesting Module
from Backtesting.Statistics import Statistics
from Backtesting.Backtest import get_vanilla_backtest, get_bands_backtest

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters
from Indicators.BollingerBands import get_bollinger_bands
from Indicators.LeastSquares import get_least_squares
from Indicators.DecisionTree import get_decision_tree
from Indicators.Ridge import get_ridge
from Indicators.BayesRidge import get_bayes_ridge

# Import Helper Methods Module
from HelperMethods.Helpers import print_results
from HelperMethods.Helpers import plot_backtest_pnl, plot_backtest_distribution

from .Volatility import plot_vol_metrics

# Import Python Libraries
import matplotlib.pyplot as plt

def individual_backtest(ohlc):
    """
    Computes Results for a Single Backtest
    """

    # Step Three: Initialize Parameters
    period = 20
    projection = 0
    par = Parameters(period, projection)
    plot_vol_metrics(ohlc, par)

    open = ohlc.open[period:]
    high = ohlc.high[period:]
    low = ohlc.low[period:]
    close = ohlc.close[period:]

    # Step Four: Calculate Indicators
    least_squares_average = get_least_squares(par, close)

    # Step Five: Initialize Statistics
    lot_size = 1
    least_squares_open = Statistics(lot_size, len(open[period:]))
    least_squares_high = Statistics(lot_size, len(high[period:]))
    least_squares_low = Statistics(lot_size, len(low[period:]))
    least_squares_close = Statistics(lot_size, len(close[period:]))

    # Step Six: Run Backtest
    least_squares_open = get_vanilla_backtest(least_squares_open, open[period:], least_squares_average)
    least_squares_high = get_vanilla_backtest(least_squares_high, high[period:], least_squares_average)
    least_squares_low = get_vanilla_backtest(least_squares_low, low[period:], least_squares_average)
    least_squares_close = get_vanilla_backtest(least_squares_close, close[period:], least_squares_average)

    # Step Seven: Print Statistics
    stats_list = [least_squares_open, least_squares_high, least_squares_low, least_squares_close]
    names_list = ["Least Squares Open", "Least Squares High", "Least Squares Low", "Least Squares Close"]
    print_results(stats_list, names_list)

    # Final Step !!!
    # Visualize Backtest Results
    plot_backtest_pnl(stats_list)
    plot_backtest_distribution(stats_list)

    plt.show()

    return 0 