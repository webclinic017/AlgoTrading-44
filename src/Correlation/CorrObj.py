import numpy as np
from numba import jit, float64 
from numba.experimental import jitclass

spec = [
    # Volatility
    ('ocorr', float64[:]),
    ('hcorr', float64[:]),
    ('lcorr', float64[:]),
    ('ccorr', float64[:]),
    ('ocorr_clusters', float64[:]),
    ('hcorr_clusters', float64[:]),
    ('lcorr_clusters', float64[:]),
    ('ccorr_clusters', float64[:]),

    # Volatility of Correlation
    ('ocorr_vol', float64[:]),
    ('hcorr_vol', float64[:]),
    ('lcorr_vol', float64[:]),
    ('ccorr_vol', float64[:]),
    ('ocorr_vol_clusters', float64[:]),
    ('hcorr_vol_clusters', float64[:]),
    ('lcorr_vol_clusters', float64[:]),
    ('ccorr_vol_clusters', float64[:]),

]

@jitclass(spec)
class CorrStats:
    """
    
    """

    def __init__(self):

        # Temp Length
        N = 100

        # Volatility
        self.ocorr = np.zeros(N)
        self.hcorr = np.zeros(N)
        self.lcorr = np.zeros(N)
        self.ccorr = np.zeros(N)
        self.ocorr_clusters = np.zeros(N)
        self.hcorr_clusters = np.zeros(N)
        self.lcorr_clusters = np.zeros(N)
        self.ccorr_clusters = np.zeros(N)

        # Volatility of Volatility
        self.ocorr_vol = np.zeros(N)
        self.hcorr_vol = np.zeros(N)
        self.lcorr_vol = np.zeros(N)
        self.ccorr_vol = np.zeros(N)
        self.ocorr_vol_clusters = np.zeros(N)
        self.hcorr_vol_clusters = np.zeros(N)
        self.lcorr_vol_clusters = np.zeros(N)
        self.ccorr_vol_clusters = np.zeros(N)


