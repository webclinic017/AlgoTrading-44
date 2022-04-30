import numpy as np
from .VolObj import VolStats
from Volatility.VolMetrics import get_vol_of_vol_methods, get_volatilty_methods

def get_vol_clusters(ohlc, period):
    """
    Returns an Object that Wraps All Volatility Methods
    """

    # Fetch Volatility Data
    cvol, ovol, ivol, cvol_clusters, ovol_clusters, ivol_clusters = get_volatilty_methods(ohlc, period)
    cvol_vol, ovol_vol, ivol_vol, cvol_vol_clusters, ovol_vol_clusters, ivol_vol_clusters = get_vol_of_vol_methods(cvol, ovol, ivol, period)

    # Initialize Object
    VS = VolStats()

    # Volatility Methods
    VS.cvol = cvol 
    VS.ovol = ovol 
    VS.ivol = ivol 
    VS.cvol_clusters = np.sort(np.array([cvol_clusters[0][0], cvol_clusters[1][0], cvol_clusters[2][0]]))
    VS.ovol_clusters = np.sort(np.array([ovol_clusters[0][0], ovol_clusters[1][0], ovol_clusters[2][0]]))
    VS.ivol_clusters = np.sort(np.array([ivol_clusters[0][0], ivol_clusters[1][0], ivol_clusters[2][0]]))

    # Volatility of Volatility Methods
    VS.cvol_vol = cvol_vol
    VS.ovol_vol = ovol_vol 
    VS.ivol_vol = ivol_vol 
    VS.cvol_vol_clusters = np.sort(np.array([cvol_vol_clusters[0][0], cvol_vol_clusters[1][0], cvol_vol_clusters[2][0]]))
    VS.ovol_vol_clusters = np.sort(np.array([ovol_vol_clusters[0][0], ovol_vol_clusters[1][0], ovol_vol_clusters[2][0]]))
    VS.ivol_vol_clusters = np.sort(np.array([ivol_vol_clusters[0][0], ivol_vol_clusters[1][0], ivol_vol_clusters[2][0]]))

    return VS