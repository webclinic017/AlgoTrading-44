import numpy as np
from numba import jit 

@jit(nopython = True)
def get_volatilty_methods(ohlc, period):
    """
    Compute all Volatility Metrics
    """

    hv = h_vol(ohlc, period)
    ov = o_vol(ohlc, period)
    iv = i_vol(ohlc, period)

    return hv, ov, iv

@jit(nopython = True)
def h_vol(ohlc, period):
    """
    Close to Close Volatility
    """

    log_returns = np.zeros(len(ohlc.close))

    for i in range(len(log_returns)):

        log_returns[i] = np.log(ohlc.close[i + 1]) / np.log(ohlc.close[i])

    index = 0
    vol = np.zeros(len(log_returns))

    for i in range(period, len(log_returns)):

        avg = 0

        for j in range(i, i - period):

            avg += log_returns[j]

        s = 0
        avg /= period

        for k in range(i, i - period):

            s += (log_returns[k] - avg)**2

        vol[index] = np.sqrt(s / period) * np.sqrt(252)
        index+=1

    return vol

@jit(nopython = True)
def o_vol(ohlc, period):
    """
    Overnight Volatility
    """

    log_returns = np.zeros(len(ohlc.close))

    for i in range(len(log_returns)):

        log_returns[i] = np.log(ohlc.open[i + 1]) / np.log(ohlc.close[i])

    index = 0
    vol = np.zeros(len(log_returns))

    for i in range(period, len(log_returns)):

        avg = 0

        for j in range(i, i - period):

            avg += log_returns[j]

        s = 0
        avg /= period

        for k in range(i, i - period):

            s += (log_returns[k] - avg)**2

        vol[index] = np.sqrt(s / period) * np.sqrt(252)
        index+=1

    return vol

@jit(nopython = True)
def i_vol(ohlc, period):
    """
    Intraday Volatility
    """

    log_returns = np.zeros(len(ohlc.close))

    for i in range(len(log_returns)):

        log_returns[i] = np.log(ohlc.close[i]) / np.log(ohlc.open[i])

    index = 0
    vol = np.zeros(len(log_returns))

    for i in range(period, len(log_returns)):

        avg = 0

        for j in range(i, i - period):

            avg += log_returns[j]

        s = 0
        avg /= period

        for k in range(i, i - period):

            s += (log_returns[k] - avg)**2

        vol[index] = np.sqrt(s / period) * np.sqrt(252)
        index+=1

    return vol





