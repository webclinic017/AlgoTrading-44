from matplotlib.pyplot import get
from Volatility.VolMetrics import get_vol_of_vol, get_volatilty_methods

import matplotlib.pyplot as plt

def plot_vol_metrics(ohlc, par):

    cvol, ovol, ivol = get_volatilty_methods(ohlc, par.period)
    cvol_vol, ovol_vol, ivol_vol = get_vol_of_vol(cvol, ovol, ivol, par.period)

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(cvol, label = "Close to Close")
    ax1.plot(ovol, label = "Overnight")
    ax1.plot(ivol, label = "Intraday")
    ax1.set_title("Volatility Metrics")
    ax1.legend(loc = 'best')

    ax2.plot(cvol_vol, label = "Close to Close Vol of Vol")
    ax2.plot(ovol_vol, label = "Overnight Vol of Vol")
    ax2.plot(ivol_vol, label = "Intraday Vol of Vol")
    ax2.set_title("Vol of Vol Metrics")
    ax2.legend(loc = "best")

    return 0