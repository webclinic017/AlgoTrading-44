import numpy as np
from numba import jit 

def get_correlations(ohlcA, ohlcB, regression_type):
    """
    Returns the Regressions of a Pair of Stocks
    
    A is Independent
    B is Dependent
    """

    regression_type(ohlcA, ohlcB)

    return 0