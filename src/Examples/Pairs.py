# Import Backtesting Module
from Backtesting.Indicators import PairsIndicators
from Backtesting.Variables import Statistics
from Backtesting.PairsBacktest import get_pairs_backtest

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters
from Indicators.LeastSquares import get_least_squares
from Indicators.DecisionTree import get_decision_tree
from Indicators.Ridge import get_ridge
from Indicators.BayesRidge import get_bayes_ridge

# Import Helper Methods Module
from HelperMethods.Helpers import print_results
from HelperMethods.Helpers import plot_backtest_pnl, plot_backtest_distribution

# Import Python Libraries
import matplotlib.pyplot as plt

from Correlation.CorrelationClusters import get_corr_clusters
from Volatility.VolClusters import get_vol_clusters
from Examples.Volatility import plot_vol_metrics
from Examples.Correlation import plot_corr_metrics, plot_pairs_testing

def pairs_backtest(ohlcA, ohlcB, isDisplay):
    """
    Computes Results for a Pairs Backtest
    """

    # Step Three: Initialize Parameters
    period = 20
    projection = 0
    par = Parameters(period, projection)

        # Volatility Clusters
    if isDisplay == True:
        plot_vol_metrics(ohlcA, par)
        plot_corr_metrics(ohlcA, ohlcB, par)
        plot_pairs_testing(ohlcA.close, ohlcB.close)

    VS = get_vol_clusters(ohlcA, period)
    CS = get_corr_clusters(ohlcA, ohlcB, period)

    openA = ohlcA.open[period:]
    highA = ohlcA.high[period:]
    lowA = ohlcA.low[period:]
    closeA = ohlcA.close[period:]

    openB = ohlcB.open[period:]
    highB = ohlcB.high[period:]
    lowB = ohlcB.low[period:]
    closeB = ohlcB.close[period:]

    # Step Four: Calculate Indicators
    long_cluster = 1
    short_cluster = 2
    least_squares_averageA = get_least_squares(par, closeA)
    least_squares_averageB = get_least_squares(par, closeB)
    IndicatorsObj = PairsIndicators(least_squares_averageA, least_squares_averageB, VS.cvol, VS.cvol_clusters, VS.cvol_vol, VS.cvol_vol_clusters, CS.ccorr, CS.ccorr_vol, CS.ccorr_vol_clusters, long_cluster, short_cluster)

    # Step Five: Initialize Statistics
    lot_size = 1
    least_squares_open = Statistics(lot_size, len(openA[period:]), period)
    least_squares_high = Statistics(lot_size, len(highA[period:]), period)
    least_squares_low = Statistics(lot_size, len(lowA[period:]), period)
    least_squares_close = Statistics(lot_size, len(closeA[period:]), period)

    # Step Six: Run Backtest
    contrarian = False
    least_squares_open = get_pairs_backtest(least_squares_open, openA[period:], least_squares_averageA, openB[period:], least_squares_averageB, contrarian)
    least_squares_high = get_pairs_backtest(least_squares_high, highA[period:], least_squares_averageA, highB[period:], least_squares_averageB, contrarian)
    least_squares_low = get_pairs_backtest(least_squares_low, lowA[period:], least_squares_averageA, lowB[period:], least_squares_averageB, contrarian)
    least_squares_close = get_pairs_backtest(least_squares_close, closeA[period:], least_squares_averageA, closeB[period:], least_squares_averageB, contrarian)

    # Step Seven: Print Statistics
    stats_list = [least_squares_open, least_squares_high, least_squares_low, least_squares_close]
    names_list = ["Least Squares Open", "Least Squares High", "Least Squares Low", "Least Squares Close"]
    print_results(stats_list, names_list)

    # Final Step !!!
    # Visualize Backtest Results
    plot_backtest_pnl(stats_list)
    plot_backtest_distribution(stats_list)

    return 0