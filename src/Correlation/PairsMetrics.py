import numpy as np
from numba import jit 
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import BayesianRidge

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

    # Least Squares
    least_squares = LinearRegression().fit(log_a.reshape((-1, 1)), log_b.reshape((-1, 1)))
    ls = least_squares.predict(log_a.reshape((-1, 1)))

    # Ridge 
    ridge = Ridge(alpha = 1)
    ridge.fit(log_a.reshape((-1, 1)), log_b.reshape((-1, 1)))
    r = ridge.predict(log_a.reshape((-1, 1)))

    # Decision Tree
    rng = np.random.RandomState(1)
    ada = AdaBoostRegressor(DecisionTreeRegressor(max_depth = 3), n_estimators = 100, random_state = rng)
    ada.fit(log_a.reshape((-1, 1)), log_b.reshape((-1, 1)))
    dt = ada.predict(log_a.reshape((-1, 1)))

    # Bayes Ridge
    bayes = BayesianRidge().fit(log_a.reshape((-1, 1)), log_b.reshape((-1, 1)))
    br = bayes.predict(log_a.reshape((-1, 1)))
    
    return log_a, log_b, ls, r, dt, br




