import numpy as np
from numba import float64 
from numba.experimental import jitclass 

spec = [
    ('carlmar_ratio', float64[:]),
    ('sharpe_ratio', float64[:]),
    ('sortino_ratio', float64[:]),
    ('max_drawdown', float64[:]),
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
        self.max_drawdown = np.zeros(length - period)