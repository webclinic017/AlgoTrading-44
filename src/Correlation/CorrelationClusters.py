import numpy as np

from Correlation.CorrObj import CorrStats
from Correlation.Correlation import get_correlation_coeff, get_vol_of_corr_methods

def get_corr_clusters(ohlcA, ohlcB, period):
    """
    Returns an Object that Wraps All Correlation Methods
    """

    # Fetch Volatility Data
    open_corr, high_corr, low_corr, close_corr, open_clusters, high_clusters, low_clusters, close_clusters = get_correlation_coeff(ohlcA, ohlcB, period)
    ocorr_vol, hcorr_vol, lcorr_vol, ccorr_vol, ocorr_vol_clusters, hcorr_vol_clusters, lcorr_vol_clusters, ccorr_vol_clusters = get_vol_of_corr_methods(open_corr, high_corr, low_corr, close_corr, period)

    # Initialize Object
    CS = CorrStats()

    # Volatility Methods
    CS.ocorr = open_corr 
    CS.hcorr = high_corr 
    CS.lcorr = low_corr 
    CS.ccorr = close_corr
    CS.ocorr_clusters = np.sort(np.array([open_clusters[0][0], open_clusters[1][0], open_clusters[2][0]]))
    CS.hcorr_clusters = np.sort(np.array([high_clusters[0][0], high_clusters[1][0], high_clusters[2][0]]))
    CS.lcorr_clusters = np.sort(np.array([low_clusters[0][0], low_clusters[1][0], low_clusters[2][0]]))
    CS.ccorr_clusters = np.sort(np.array([close_clusters[0][0], close_clusters[1][0], close_clusters[2][0]]))

    # Volatility of Volatility Methods
    CS.ocorr_vol = ocorr_vol
    CS.hcorr_vol = hcorr_vol 
    CS.lcorr_vol = lcorr_vol 
    CS.ccorr_vol = ccorr_vol 
    CS.ocorr_vol_clusters = np.sort(np.array([ocorr_vol_clusters[0][0], ocorr_vol_clusters[1][0], ocorr_vol_clusters[2][0]]))
    CS.hcorr_vol_clusters = np.sort(np.array([hcorr_vol_clusters[0][0], hcorr_vol_clusters[1][0], hcorr_vol_clusters[2][0]]))
    CS.lcorr_vol_clusters = np.sort(np.array([lcorr_vol_clusters[0][0], lcorr_vol_clusters[1][0], lcorr_vol_clusters[2][0]]))
    CS.ccorr_vol_clusters = np.sort(np.array([ccorr_vol_clusters[0][0], ccorr_vol_clusters[1][0], ccorr_vol_clusters[2][0]]))

    return CS