import numpy as np
from numba import jit
from sklearn.linear_model import Ridge

def get_ridge_regression(X, Y, projection):
    """
    Returns Linear Regression Slice
    """

    reg = Ridge(alpha = 1)
    reg.fit(X, Y)

    alpha = reg.intercept_
    beta = reg.coef_
    ridge = alpha + beta * projection

    return ridge

# @jit(nopython = True)
def get_ridge(par, ohlc):
    """
    Returns the Ridge Moving Average
    """

    length = len(ohlc)
    least_squares = np.zeros(length - par.period)
    X = np.linspace(0, par.period, par.period).reshape((-1, 1))

    index = 0
    for i in range(par.period, length):

        Y = np.zeros(par.period)
        count = 0

        for j in range(i, i - par.period, -1):

            Y[count] = ohlc[j]
            count+=1

        least_squares[index] = get_ridge_regression(X, Y, par.projection)
        index+=1

    return least_squares