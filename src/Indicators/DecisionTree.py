import numpy as np
from numba import jit
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

def get_decision_tree_regression(X, Y, projection):
    """
    Returns Linear Regression Slice
    """

    rng = np.random.RandomState(1)
    ada = AdaBoostRegressor(DecisionTreeRegressor(max_depth = 4), n_estimators = 300, random_state = rng)
    ada.fit(X, Y)

    ridge = ada.predict(X)

    return ridge[projection]

# @jit(nopython = True)
def get_decision_tree(par, ohlc):
    """
    Returns the Decision Tree Moving Average
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

        least_squares[index] = get_decision_tree_regression(X, Y, par.projection)
        index+=1

    return least_squares