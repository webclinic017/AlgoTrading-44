import numpy as np 
from numba import jit 

@jit(nopython = True, parallel = True)
def get_correlation_coeff(ohlcA, ohlcB, period):
    """
    Compute Correlation of OHLC
    """

    index = 0
    open_corr = np.zeros(len(ohlcA.close))
    high_corr = np.zeros(len(ohlcA.close))
    low_corr = np.zeros(len(ohlcA.close))
    close_corr = np.zeros(len(ohlcA.close))

    for i in range(period, len(ohlcA.close)):

        TA_open = np.zeros(period)
        TB_open = np.zeros(period)
        TA_high = np.zeros(period)
        TB_high = np.zeros(period)
        TA_low = np.zeros(period)
        TB_low = np.zeros(period)
        TA_close = np.zeros(period)
        TB_close = np.zeros(period)

        count = 0
        for j in range(i, i - period, -1):

            TA_open[count] = ohlcA.open[j]
            TA_high[count] = ohlcA.high[j]
            TA_low[count] = ohlcA.low[j]
            TA_close[count] = ohlcA.close[j]

            TB_open[count] = ohlcB.open[j]
            TB_high[count] = ohlcB.high[j]
            TB_low[count] = ohlcB.low[j]
            TB_close[count] = ohlcB.close[j]

            count+=1

        open_corr[index] = np.corrcoef(TA_open, TB_open, rowvar = False)[0][1]
        high_corr[index] = np.corrcoef(TA_high, TB_high, rowvar = False)[0][1]
        low_corr[index] = np.corrcoef(TA_low, TB_low, rowvar = False)[0][1]
        close_corr[index] = np.corrcoef(TA_close, TB_close, rowvar = False)[0][1]

        index+=1

    return open_corr, high_corr, low_corr, close_corr