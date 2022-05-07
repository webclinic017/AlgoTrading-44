import numpy as np
from numba import float64 
from numba.experimental import jitclass 

spec = [
    ('calmar_ratio', float64[:]),
    ('sharpe_ratio', float64[:]),
    ('sortino_ratio', float64[:]),
    ('treynor_ratio', float64[:]),
    ('backtest_drawdown', float64[:]),
    ('benchmark_drawdown', float64[:])
]

@jitclass(spec)
class Stats:
    """
    Object that wraps all performance statistics
    """

    def __init__(self, length, period):
        self.calmar_ratio = np.zeros(length - period)
        self.sharpe_ratio = np.zeros(length - period)
        self.sortino_ratio = np.zeros(length - period)
        self.treynor_ratio = np.zeros(length - period)
        self.backtest_drawdown = np.zeros(length)
        self.benchmark_drawdown = np.zeros(length)

