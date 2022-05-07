# Import Backtesting Module
from Backtesting.Indicators import Indicators
from Backtesting.Variables import Statistics
from Backtesting.Backtest import get_vanilla_backtest
from Backtesting.Statistics import get_statistics

# Import Volatility Module
from Volatility.VolClusters import get_vol_clusters

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters
from Indicators.LeastSquares import get_least_squares
from Indicators.DecisionTree import get_decision_tree
from Indicators.Ridge import get_ridge
from Indicators.BayesRidge import get_bayes_ridge

# Import Helper Methods Module
from HelperMethods.Helpers import print_results
from HelperMethods.Helpers import plot_backtest_pnl, plot_backtest_distribution, plot_performance_statistics

from .Volatility import plot_vol_metrics

# Import Python Libraries
import matplotlib.pyplot as plt

def individual_backtest(ohlc, rolling_period, projection, isDisplay):
    """
    Computes Results for a Single Backtest
    """

    # Step Three: Initialize Parameters
    par = Parameters(rolling_period, projection)

    # Volatility Clusters
    if isDisplay == True:
        plot_vol_metrics(ohlc, par)

    VS = get_vol_clusters(ohlc, rolling_period)

    open = ohlc.open[rolling_period:]
    high = ohlc.high[rolling_period:]
    low = ohlc.low[rolling_period:]
    close = ohlc.close[rolling_period:]

    # Step Four: Calculate Indicators
    long_cluster = 1
    short_cluster = 2
    least_squares_average = get_least_squares(par, close)
    IndicatorsObj = Indicators(least_squares_average, VS.cvol, VS.cvol_clusters, VS.cvol_vol, VS.cvol_vol_clusters, long_cluster, short_cluster)

    # Step Five: Initialize Statistics
    lot_size = 1
    least_squares_open = Statistics(lot_size, len(open[rolling_period:]), rolling_period)
    least_squares_high = Statistics(lot_size, len(high[rolling_period:]), rolling_period)
    least_squares_low = Statistics(lot_size, len(low[rolling_period:]), rolling_period)
    least_squares_close = Statistics(lot_size, len(close[rolling_period:]), rolling_period)

    # Step Six: Run Backtest
    isContrarian = False
    least_squares_open = get_vanilla_backtest(least_squares_open, open[rolling_period:], IndicatorsObj, rolling_period, isContrarian)
    least_squares_high = get_vanilla_backtest(least_squares_high, high[rolling_period:], IndicatorsObj, rolling_period, isContrarian)
    least_squares_low = get_vanilla_backtest(least_squares_low, low[rolling_period:], IndicatorsObj, rolling_period, isContrarian)
    least_squares_close = get_vanilla_backtest(least_squares_close, close[rolling_period:], IndicatorsObj, rolling_period, isContrarian)

    # Step Seven: Print Statistics
    stats_list = [least_squares_open, least_squares_high, least_squares_low, least_squares_close]
    names_list = ["Least Squares Open", "Least Squares High", "Least Squares Low", "Least Squares Close"]
    print_results(stats_list, names_list)

    # Performance Statistics
    PS = get_statistics(close, least_squares_close.pnl, rolling_period)    

    # Final Step !!!
    # Visualize Backtest Results
    if isDisplay == True:
        plot_backtest_pnl(stats_list)
        plot_backtest_distribution(stats_list)
        plot_performance_statistics(PS)

    return 0 