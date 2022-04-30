import numpy as np

# Import Backtesting Module
from Backtesting.Indicators import Indicators
from Backtesting.Statistics import Statistics
from Backtesting.Backtest import get_vanilla_backtest, get_bands_backtest

# Import Volatility Module
from Volatility.VolClusters import get_vol_clusters

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters

from Examples.Volatility import plot_vol_metrics

def brute_force_optimization(a, b, ohlc, indicator):
    """
    Returns the PnL of an interval of rolling periods

    Input:
    1. Lower Bound, Ex: 30 days
    2. Upper Bound, Ex: 90 days
    3. Price Data
    4. Statistical Indicator

    Output:
    1. The PnL per each rolling period
    """

    open_pnl = np.zeros(b - a)
    high_pnl = np.zeros(b - a)
    low_pnl = np.zeros(b - a)
    close_pnl = np.zeros(b - a)

    for i in range(b - a):

        period = a + i
        projection = 0
        par = Parameters(period, projection)

        # Volatility Clusters
        VS = get_vol_clusters(ohlc, period)

        open = ohlc.open[period:]
        high = ohlc.high[period:]
        low = ohlc.low[period:]
        close = ohlc.close[period:]

        long_cluster = 0
        short_cluster = 2
        moving_average = indicator(par, close)
        IndicatorsObj = Indicators(moving_average, VS.cvol, VS.cvol_clusters, VS.cvol_vol, VS.cvol_vol_clusters, long_cluster, short_cluster)

        lot_size = 1
        indicator_open = Statistics(lot_size, len(open[period:]), period)
        indicator_high = Statistics(lot_size, len(high[period:]), period)
        indicator_low = Statistics(lot_size, len(low[period:]), period)
        indicator_close = Statistics(lot_size, len(close[period:]), period)

        isContrarian = False
        indicator_open = get_vanilla_backtest(indicator_open, open[period:], IndicatorsObj, period, isContrarian)
        indicator_high = get_vanilla_backtest(indicator_high, high[period:], IndicatorsObj, period, isContrarian)
        indicator_low = get_vanilla_backtest(indicator_low, low[period:], IndicatorsObj, period, isContrarian)
        indicator_close = get_vanilla_backtest(indicator_close, close[period:], IndicatorsObj, period, isContrarian)

        open_pnl[i] = np.sum(indicator_open.trade_results)
        high_pnl[i] = np.sum(indicator_high.trade_results)
        low_pnl[i] = np.sum(indicator_low.trade_results)
        close_pnl[i] = np.sum(indicator_close.trade_results)

    return open_pnl, high_pnl, low_pnl, close_pnl