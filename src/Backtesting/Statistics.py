from .StatisticsObj import Stats
import numpy as np
from numba import jit

@jit(nopython = True)
def get_statistics(price, pnl, period):
    """
    Returns Backtest Statistics
    1. Max Drawdown
    2. Calmar Ratio
    3. Sharpe Ratio
    4. Sortino Ratio
    5. Treynor Ratio
    """

    S = Stats(len(pnl), period)
    S.sharpe_ratio = sharpe_ratio(price, pnl, period)
    S.sortino_ratio = sortino_ratio(price, pnl, period)
    S.treynor_ratio = treynor_ratio(price, pnl, period)
    S.benchmark_drawdown, S.backtest_drawdown, max_dd = max_drawdown(price, pnl, period)
    S.calmar_ratio = calmar_ratio(price, pnl, period, max_dd)
    
    return S

@jit(nopython = True, parallel = True)
def calmar_ratio(price, pnl, period, max_drawdown):

    calmar = np.zeros(len(pnl) - period)

    for i in range(period, len(pnl)):

        # Compute Log Returns
        benchmark_return = np.log(price[i] / price[i - period])
        backtest_return = np.log(pnl[i] / pnl[i - period])

        log_returns = np.zeros(period - 1, dtype = np.float64)

        index = i - period
        for j in range(period - 1):
            log_returns[j] = np.log(pnl[index + 1] / pnl[index])
            index+=1

        # Compute Calmar Ratio
        if max_drawdown == 0:
            calmar[i - period] = calmar[1 - period - 1]
        else:
            calmar[i - period] = (backtest_return - benchmark_return) / max_drawdown

    return calmar

@jit(nopython = True, parallel = True)
def sharpe_ratio(price, pnl, period):

    sharpe = np.zeros(len(pnl) - period)

    for i in range(period, len(pnl)):

        # Compute Log Returns
        benchmark_return = np.log(price[i] / price[i - period])
        backtest_return = np.log(pnl[i] / pnl[i - period])

        log_returns = np.zeros(period - 1, dtype = np.float64)

        index = i - period
        for j in range(period - 1):
            log_returns[j] = np.log(pnl[index + 1] / pnl[index])
            index+=1

        # Compute Standard Deviation of Backtest Log Returns
        std = np.std(log_returns) * np.sqrt(252)

        # Compute Sharpe Ratio
        if std == 0:
            sharpe[i - period] = sharpe[i - period - 1]
        else:
            sharpe[i - period] = (backtest_return - benchmark_return) / std

    return sharpe

@jit(nopython = True)
def downside_deviation(minimum_return, backtest_return):

    dd = 0

    for i in range(len(backtest_return)):

        temp = backtest_return[i] - minimum_return

        if temp < 0:
            dd += temp**2

    dd = np.sqrt(dd / len(backtest_return))

    return dd

@jit(nopython = True, parallel = True)
def sortino_ratio(price, pnl, period):

    sortino = np.zeros(len(pnl) - period)

    for i in range(period, len(pnl)):

        # Compute Log Returns
        benchmark_return = np.log(price[i] / price[i - period])
        backtest_return = np.log(pnl[i] / pnl[i - period])

        backtest_log = np.zeros(period - 1)

        index = i - period
        for j in range(period - 1):
            backtest_log[j] = np.log(pnl[index + 1] / pnl[index])
            index +=1

        # Compute Standard Deviation of Backtest Log Returns
        dd = downside_deviation(benchmark_return, backtest_log)

        # Compute Sortino Ratio
        if dd == 0:
            sortino[i - period] = sortino[i - period - 1]
        else:
            sortino[i - period] = (backtest_return - benchmark_return) / dd

    return sortino

@jit(nopython = True, parallel = True)
def treynor_ratio(price, pnl, period):

    treynor = np.zeros(len(pnl) - period)

    for i in range(period, len(pnl)):

        # Compute Log Returns
        benchmark_return = np.log(price[i] / price[i - period])
        backtest_return = np.log(pnl[i] / pnl[i - period])

        benchmark_log_returns = np.zeros(period - 1)
        backtest_log_returns = np.zeros(period - 1)

        for j in range(period - 1):
            benchmark_log_returns[j] = np.log(price[j + 1] / price[j])
            backtest_log_returns[j] = np.log(pnl[j + 1] / pnl[j])

        # Compute Beta of Backtest Log Returns
        beta = np.cov(benchmark_log_returns, backtest_log_returns)[0][1] / np.var(benchmark_log_returns)

        # Compute Treynor Ratio
        treynor[i - period] = (backtest_return - benchmark_return) / beta

    return treynor

@jit(nopython = True, parallel = True)
def max_drawdown(price, pnl, period):

    price = price[period:]

    historical_high = price[0]
    historical_low = price[0]
    historical_drawdown = np.zeros(len(price))

    backtest_high = pnl[0]
    backtest_low = pnl[0]
    backtest_drawdown = np.zeros(len(pnl))

    max_drawdown = 0

    # Compute Backtest, Price Drawdowns
    for i in range(1, len(pnl)):

        # Historical
        if price[i] < historical_low:

            historical_low = price[i]

        if price[i] > historical_high:

            historical_high = price[i]

        temp = np.log(price[i] / historical_high)

        if temp < 0:
            historical_drawdown[i] = temp 
        else:
            historical_drawdown[i] = 0

        # Backtest
        if pnl[i] < backtest_low:

            backtest_low = pnl[i]

        if pnl[i] > backtest_high:

            backtest_high = pnl[i]

        temp = np.log(pnl[i] / backtest_high) 

        if temp < max_drawdown:
            max_drawdown = temp

        if temp < 0:
            backtest_drawdown[i] = temp 
        else: 
            backtest_drawdown[i] = 0

    return historical_drawdown, backtest_drawdown, max_drawdown




