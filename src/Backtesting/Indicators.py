from numba import int64, float64
from numba.experimental import jitclass

#######################
#                     #
# INDIVIDUAL BACKTEST #
#                     #
#######################

spec = [
    ('moving_average', float64[:]),
    ('volatility', float64[:]),
    ('volatility_cluster', float64[:]),
    ('vol_of_vol', float64[:]),
    ('vol_of_vol_cluster', float64[:]),
    ('long_cluster', int64),
    ('short_cluster', int64)
]

@jitclass(spec)
class Indicators:
    """
    Object that wraps all backtesting indicators

    Inputs: 
    1. Statistical Indicator
    2. Volatility Metric
    3. Volatility Metric Clustered
    4. Volatility of Volatility Metric
    5. Volatility of Volatility Clustered
    6. Long Cluster Index
    7. Short Cluster Index

    Output: 
    1. Returns Initialied Object
    """

    def __init__(self, moving_average, volatility, volatility_cluster, vol_vol, vol_vol_cluster, long_cluster, short_cluster):
        self.moving_average = moving_average
        self.volatility = volatility 
        self.volatility_cluster = volatility_cluster
        self.vol_of_vol = vol_vol
        self.vol_of_vol_cluster = vol_vol_cluster
        self.long_cluster = long_cluster
        self.short_cluster = short_cluster

##################
#                #
# PAIRS BACKTEST #
#                #
##################

spec = [
    ('moving_averageA', float64[:]),
    ('moving_averageB', float64[:]),
    ('volatility', float64[:]),
    ('volatility_cluster', float64[:]),
    ('vol_of_vol', float64[:]),
    ('vol_of_vol_cluster', float64[:]),
    ('corr', float64[:]),
    ('corr_vol', float64[:]),
    ('corr_vol_cluster', float64[:]),
    ('long_cluster', int64),
    ('short_cluster', int64)
]

@jitclass(spec)
class PairsIndicators:
    """
    Object that wraps all backtesting indicators

    Inputs: 
    1. Statistical Indicator
    2. Volatility Metric
    3. Volatility Metric Clustered
    4. Volatility of Volatility Metric
    5. Volatility of Volatility Clustered
    6. Correlation Metric
    7. Volatility of Correlation
    8. Volatility of Correlation Clustered
    9. Long Cluster Index
    10. Short Cluster Index

    Output: 
    1. Returns Initialied Object
    """

    def __init__(self, moving_averageA, moving_averageB, volatility, volatility_cluster, vol_vol, vol_vol_cluster, corr, corr_vol, corr_vol_cluster, long_cluster, short_cluster):
        self.moving_averageA = moving_averageA
        self.moving_averageB = moving_averageB
        self.volatility = volatility 
        self.volatility_cluster = volatility_cluster
        self.vol_of_vol = vol_vol
        self.vol_of_vol_cluster = vol_vol_cluster
        self.corr = corr 
        self.corr_vol = corr_vol
        self.corr_vol_cluster = corr_vol_cluster
        self.long_cluster = long_cluster
        self.short_cluster = short_cluster



