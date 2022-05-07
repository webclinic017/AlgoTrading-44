import numpy as np 
from numba import jit 
from sklearn.cluster import kmeans_plusplus

from Volatility.VolMetrics import compute_vol_of_vol

def get_correlation_coeff(ohlcA, ohlcB, period):
    """
    Compute Correlation of OHLC
    """

    open_corr, high_corr, low_corr, close_corr = get_correlations(ohlcA, ohlcB, period)

    ocluster, _ = kmeans_plusplus(open_corr.reshape(-1, 1), n_clusters = 3, random_state = 0)
    hcluster, _ = kmeans_plusplus(high_corr.reshape(-1, 1), n_clusters = 3, random_state = 0)
    lcluster, _ = kmeans_plusplus(low_corr.reshape(-1, 1), n_clusters = 3, random_state = 0)
    ccluster, _ = kmeans_plusplus(close_corr.reshape(-1, 1), n_clusters = 3, random_state = 0)

    return open_corr, high_corr, low_corr, close_corr, ocluster, hcluster, lcluster, ccluster

@jit(nopython = True)
def get_correlations(ohlcA, ohlcB, period):

    index = 0
    open_corr = np.zeros(len(ohlcA.close))
    high_corr = np.zeros(len(ohlcA.close))
    low_corr = np.zeros(len(ohlcA.close))
    close_corr = np.zeros(len(ohlcA.close))

    for i in range(period, len(ohlcA.close)):

        TA_open = np.zeros(period)
        TB_open = np.zeros(period)
        TA_high = np.zeros(period)
        TB_high = np.zeros(period)
        TA_low = np.zeros(period)
        TB_low = np.zeros(period)
        TA_close = np.zeros(period)
        TB_close = np.zeros(period)

        count = 0
        for j in range(i, i - period, -1):

            TA_open[count] = ohlcA.open[j]
            TA_high[count] = ohlcA.high[j]
            TA_low[count] = ohlcA.low[j]
            TA_close[count] = ohlcA.close[j]

            TB_open[count] = ohlcB.open[j]
            TB_high[count] = ohlcB.high[j]
            TB_low[count] = ohlcB.low[j]
            TB_close[count] = ohlcB.close[j]

            count+=1

        open_corr[index] = np.corrcoef(TA_open, TB_open, rowvar = False)[0][1]
        high_corr[index] = np.corrcoef(TA_high, TB_high, rowvar = False)[0][1]
        low_corr[index] = np.corrcoef(TA_low, TB_low, rowvar = False)[0][1]
        close_corr[index] = np.corrcoef(TA_close, TB_close, rowvar = False)[0][1]

        index+=1

    return open_corr, high_corr, low_corr, close_corr

def get_vol_of_corr_methods(ocorr, hcorr, lcorr, ccorr, period):
    """
    Compute all Volatility of Volatility Metrics
    """

    ocorr_vol = compute_vol_of_vol(ocorr, period)
    hcorr_vol = compute_vol_of_vol(hcorr, period)
    lcorr_vol = compute_vol_of_vol(lcorr, period)
    ccorr_vol = compute_vol_of_vol(ccorr, period)

    ocorr_clusters, _ = kmeans_plusplus(ocorr_vol.reshape(-1, 1), n_clusters = 3, random_state = 0)
    hcorr_clusters, _ = kmeans_plusplus(hcorr_vol.reshape(-1, 1), n_clusters = 3, random_state = 0)
    lcorr_clusters, _ = kmeans_plusplus(lcorr_vol.reshape(-1, 1), n_clusters = 3, random_state = 0)
    ccorr_clusters, _ = kmeans_plusplus(ccorr_vol.reshape(-1, 1), n_clusters = 3, random_state = 0)

    return ocorr_vol, hcorr_vol, lcorr_vol, ccorr_vol, ocorr_clusters, hcorr_clusters, lcorr_clusters, ccorr_clusters