# Import Backtesting Module
from Backtesting.Statistics import Statistics
from Backtesting.PairsBacktest import get_pairs_backtest

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

# Import Python Libraries
import matplotlib.pyplot as plt

from Examples.Volatility import plot_vol_metrics
from Examples.Correlation import plot_corr_metrics

def pairs_backtest(ohlcA, ohlcB):
    """
    Computes Results for a Pairs Backtest
    """

    # Step Three: Initialize Parameters
    period = 20
    projection = 0
    par = Parameters(period, projection)
    plot_vol_metrics(ohlcA, par)
    plot_corr_metrics(ohlcA, ohlcB, par)

    openA = ohlcA.open[period:]
    highA = ohlcA.high[period:]
    lowA = ohlcA.low[period:]
    closeA = ohlcA.close[period:]

    openB = ohlcB.open[period:]
    highB = ohlcB.high[period:]
    lowB = ohlcB.low[period:]
    closeB = ohlcB.close[period:]

    # Step Four: Calculate Indicators
    least_squares_averageA = get_least_squares(par, closeA)
    least_squares_averageB = get_least_squares(par, closeB)

    # Step Five: Initialize Statistics
    lot_size = 1
    least_squares_open = Statistics(lot_size, len(openA[period:]))
    least_squares_high = Statistics(lot_size, len(highA[period:]))
    least_squares_low = Statistics(lot_size, len(lowA[period:]))
    least_squares_close = Statistics(lot_size, len(closeA[period:]))

    # Step Six: Run Backtest
    least_squares_open = get_pairs_backtest(least_squares_open, openA[period:], least_squares_averageA, openB[period:], least_squares_averageB)
    least_squares_high = get_pairs_backtest(least_squares_high, highA[period:], least_squares_averageA, highB[period:], least_squares_averageB)
    least_squares_low = get_pairs_backtest(least_squares_low, lowA[period:], least_squares_averageA, lowB[period:], least_squares_averageB)
    least_squares_close = get_pairs_backtest(least_squares_close, closeA[period:], least_squares_averageA, closeB[period:], least_squares_averageB)

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