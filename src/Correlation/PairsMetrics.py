import numpy as np
from numba import jit 
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression

def get_correlations(ohlcA, ohlcB):
    """
    Returns the Regressions of a Pair of Stocks
    
    A is Independent
    B is Dependent
    """

    # Compute Log Returns
    log_a = np.zeros(len(ohlcA))
    log_b = np.zeros(len(ohlcB))

    for i in range(len(ohlcA) - 1):

        log_a[i] = np.log(ohlcA[i + 1] / ohlcA[i])
        log_b[i] = np.log(ohlcB[i + 1] / ohlcB[i])

    reg = LinearRegression().fit(log_a.reshape((-1, 1)), log_b.reshape((-1, 1)))

    reg = Ridge(alpha = 1)
    reg.fit(log_a.reshape((-1, 1)), log_b.reshape((-1, 1)))
    
    return log_a, log_b, reg.predict(log_a.reshape((-1, 1)))




