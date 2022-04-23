import numpy as np
from numba import jit 

@jit(nopython = True)
def get_standard_deviation(Y):

    std = np.std(Y)

    return std

@jit(nopython = True, parallel = True)
def get_bollinger_bands(par, ohlc):

    length = len(ohlc)
    bands = np.zeros(length - par.period)

    index = 0
    for i in range(par.period, length):

        Y = np.zeros(par.period)
        count = 0

        for j in range(i, i - par.period, -1):

            Y[count] = ohlc[j]
            count+=1

        bands[index] = get_standard_deviation(Y)
        index+=1

    return bands