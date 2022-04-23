import numpy as np
from numba import jit
from sklearn.linear_model import LinearRegression

def get_linear_regression(X, Y, projection):
    """
    Returns Linear Regression Slice
    """

    reg = LinearRegression().fit(X, Y)

    alpha = reg.intercept_
    beta = reg.coef_
    least_squares = alpha + beta * projection

    return least_squares

# @jit(nopython = True)
def get_least_squares(par, ohlc):
    """
    Returns the Least Squares Moving Average
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

        least_squares[index] = get_linear_regression(X, Y, par.projection)
        index+=1

    return least_squares