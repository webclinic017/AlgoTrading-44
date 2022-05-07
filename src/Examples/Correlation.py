from Correlation.Correlation import get_correlation_coeff
from Correlation.PairsMetrics import get_correlations
from Volatility.VolMetrics import get_correlation_vol, get_vol_of_vol

import numpy as np
import matplotlib.pyplot as plt

def plot_corr_metrics(ohlcA, ohlcB, par):

    open, high, low, close, _, _, _, _ = get_correlation_coeff(ohlcA, ohlcB, par.period)
    ovol, hvol, ivol, cvol = get_correlation_vol(open, high, low, close, par.period)

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(open, label = "Open")
    ax1.plot(high, label = "High")
    ax1.plot(low, label = "Low")
    ax1.plot(close, label = "Close")
    ax1.set_title("Correlation Metrics")
    ax1.legend(loc = 'best')

    ax2.plot(ovol, label = "Open Volatility")
    ax2.plot(hvol, label = "High Volatility")
    ax2.plot(ivol, label = "Low Volatility")
    ax2.plot(cvol, label = "Close Volatility")   
    ax2.set_title("Vol of Vol Metrics")
    ax2.legend(loc = "best")

    return 0

def plot_pairs_testing(ohlcA, ohlcB):

    a, b, reg = get_correlations(ohlcA, ohlcB)

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.scatter(a, b)
    ax1.plot(a, reg)
    ax1.set_title("Regression Prediction")

    return 0