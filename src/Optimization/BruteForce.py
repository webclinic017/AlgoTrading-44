import numpy as np

# Import Backtesting Module
from Backtesting.Statistics import Statistics
from Backtesting.Backtest import get_vanilla_backtest, get_bands_backtest

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters

def brute_force_optimization(a, b, ohlc, indicator):

    open_pnl = np.zeros(b - a)
    high_pnl = np.zeros(b - a)
    low_pnl = np.zeros(b - a)
    close_pnl = np.zeros(b - a)

    for i in range(b - a):

        period = a + i
        projection = 0
        par = Parameters(period, projection)

        open = ohlc.open[period:]
        high = ohlc.high[period:]
        low = ohlc.low[period:]
        close = ohlc.close[period:]

        indicator_average = indicator(par, close)

        lot_size = 1
        indicator_open = Statistics(lot_size, len(open[period:]))
        indicator_high = Statistics(lot_size, len(high[period:]))
        indicator_low = Statistics(lot_size, len(low[period:]))
        indicator_close = Statistics(lot_size, len(close[period:]))

        indicator_open = get_vanilla_backtest(indicator_open, open[period:], indicator_average)
        indicator_high = get_vanilla_backtest(indicator_high, high[period:], indicator_average)
        indicator_low = get_vanilla_backtest(indicator_low, low[period:], indicator_average)
        indicator_close = get_vanilla_backtest(indicator_close, close[period:], indicator_average)

        open_pnl[i] = np.sum(indicator_open.trade_results)
        high_pnl[i] = np.sum(indicator_high.trade_results)
        low_pnl[i] = np.sum(indicator_low.trade_results)
        close_pnl[i] = np.sum(indicator_close.trade_results)

    return open_pnl, high_pnl, low_pnl, close_pnl