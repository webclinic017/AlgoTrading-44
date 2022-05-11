import numpy as np
from numba import int64, float64 
from numba.experimental import jitclass

spec = [
    ('straddle', float64[:]),
    ('strangle', float64[:]),
    ('callbackspread', float64[:]),
    ('putbackspread', float64[:]),
    ('ironcondor', float64[:]),
    ('ironbutterfly', float64[:])
]

@jitclass(spec)
class Structures:
    """
    Object that Contains all Option Trade Structures
    """

    def __init__(self):
        self.straddle = np.zeros(2)
        self.strangle = np.zeros(2)
        self.callbackspread = np.zeros(3)
        self.putbackspread = np.zeros(3)
        self.ironcondor = np.zeros(4)
        self.ironbutterfly = np.zeros(4)

spec = [
    ('moving_average', float64[:]),
    ('volatility', float64[:]),
    ('volatility_cluster', float64[:]),
    ('vol_of_vol', float64[:]),
    ('vol_of_vol_cluster', float64[:]),
    ('long_cluster', int64),
    ('short_cluster', int64),
    ('implied_volatility', float64[:])
]

@jitclass(spec)
class OptionsIndicators:
    """
    Object that Contains all Option Trade Indicators
    """

    def __init__(self, moving_average, volatility, volatility_cluster, vol_vol, vol_vol_cluster, long_cluster, short_cluster, ivol):
        self.moving_average = moving_average
        self.volatility = volatility 
        self.volatility_cluster = volatility_cluster
        self.vol_of_vol = vol_vol
        self.vol_of_vol_cluster = vol_vol_cluster
        self.long_cluster = long_cluster
        self.short_cluster = short_cluster
        self.implied_volatility = ivol


