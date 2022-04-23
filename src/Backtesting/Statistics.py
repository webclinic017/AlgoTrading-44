from .Variables import Statistics
import numpy as np
from numba import jit

@jit(nopython = True)
def calmar_ratio(pnl):

    calmar = np.zeros(len(pnl))

    return calmar

@jit(nopython = True)
def sharpe_ratio(pnl):

    sharpe = np.zeros(len(pnl))

    return sharpe

@jit(nopython = True)
def sortino_ratio(pnl):

    sortino = np.zeros(len(pnl))

    return sortino

@jit(nopython = True)
def max_drawdown(pnl):

    drawdown = 0

    return drawdown

@jit(nopython = True)
def get_statistics():
    """
    Returns Backtest Statistics
    1. Max Drawdown
    2. Calmar Ratio
    3. Sharpe Ratio
    4. Sortino Ratio
    """

    return 0