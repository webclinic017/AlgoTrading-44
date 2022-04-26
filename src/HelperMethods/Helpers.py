import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def print_results(stats, names):
    """
    Prints Backtest Statistics to Terminal
    """

    myTable = PrettyTable(["OHLC", "Mean", "Standard Deviation", "Win Rate", "Trade Count"])

    for i in range(len(stats)):

        if len(stats[i].trade_results) > 0:

            stats[i].mean = np.mean(stats[i].trade_results)
            stats[i].std = np.std(stats[i].trade_results)

            myTable.add_row([
                names[i], 
                round(stats[i].mean, 2), 
                round(stats[i].std, 2), 
                round(stats[i].win_rate / stats[i].trade_count, 2), 
                stats[i].trade_count
                ])

        else: 

            myTable.add_row([names[i], 0, 0, 0, 0])

    print(myTable)

    return 0

def plot_backtest_pnl(stats):
    """
    Displays Backtest Results in Grid Format
    """

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle("Backtesting Engine")

    ax1.plot(stats[0].benchmark, label = "Benchmark")
    ax1.plot(stats[0].pnl, label = "Open")
    ax1.set_title("Daily Open")
    ax1.legend(loc = 'best')

    ax2.plot(stats[1].benchmark, label = "Benchmark")
    ax2.plot(stats[1].pnl, label = "High")
    ax2.set_title("Daily High")
    ax2.legend(loc = 'best')

    ax3.plot(stats[2].benchmark, label = "Benchmark")
    ax3.plot(stats[2].pnl, label = "Low")
    ax3.set_title("Daily Low")
    ax3.legend(loc = 'best')

    ax4.plot(stats[3].benchmark, label = "Benchmark")
    ax4.plot(stats[3].pnl, label = "Close")
    ax4.set_title("Daily Close")
    ax4.legend(loc = 'best')

    return 0

def plot_backtest_distribution(stats):
    """
    Displays Backtest Distribution in Grid Format
    """

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle("Backtesting Engine")

    ax1.hist(stats[0].trade_results, bins = 100)
    ax1.set_title("Daily Open Backtest")

    ax2.hist(stats[1].trade_results, bins = 100)
    ax2.set_title("Daily High Backtest")

    ax3.hist(stats[2].trade_results, bins = 100)
    ax3.set_title("Daily Low Backtest")

    ax4.hist(stats[3].trade_results, bins = 100)
    ax4.set_title("Daily Close Backtest")

    return 0

def plot_optimized_backtest_results(open, high, low, close, interval):
    """
    Displays Optimized Backtest Results
    """

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle("Backtesting Engine")

    ax1.plot(interval, open)
    ax1.set_title("Daily Open")

    ax2.plot(interval, high)
    ax2.set_title("Daily High")

    ax3.plot(interval, low)
    ax3.set_title("Daily Low")

    ax4.plot(interval, close)
    ax4.set_title("Daily Close")

    return 0