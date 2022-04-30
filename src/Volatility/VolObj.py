import numpy as np
from numba import jit, float64 
from numba.experimental import jitclass

spec = [
    # Volatility
    ('cvol', float64[:]),
    ('ovol', float64[:]),
    ('ivol', float64[:]),
    ('cvol_clusters', float64[:]),
    ('ovol_clusters', float64[:]),
    ('ivol_clusters', float64[:]),

    # Volatility of Volatility
    ('cvol_vol', float64[:]),
    ('ovol_vol', float64[:]),
    ('ivol_vol', float64[:]),
    ('cvol_vol_clusters', float64[:]),
    ('ovol_vol_clusters', float64[:]),
    ('ivol_vol_clusters', float64[:]),

]

@jitclass(spec)
class VolStats:

    def __init__(self):

        # Temp Length
        N = 100

        # Volatility
        self.cvol = np.zeros(N)
        self.ovol = np.zeros(N)
        self.ivol = np.zeros(N)
        self.cvol_clusters = np.zeros(N)
        self.cvol_clusters = np.zeros(N)
        self.cvol_clusters = np.zeros(N)

        # Volatility of Volatility
        self.cvol_vol = np.zeros(N)
        self.ovol_vol = np.zeros(N)
        self.ivol_vol = np.zeros(N)
        self.cvol_vol_clusters = np.zeros(N)
        self.cvol_vol_clusters = np.zeros(N)
        self.cvol_vol_clusters = np.zeros(N)