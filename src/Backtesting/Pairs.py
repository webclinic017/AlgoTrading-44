import numpy as np
from numba import jit 

@jit(nopython = True)
def get_long_pnl(entry, exit):
    """
    Return Profit / Loss from Long Trade
    """

    return (exit - entry)

@jit(nopython = True)
def get_short_pnl(entry, exit):
    """
    Return Profit / Loss from Short Trade
    """

    return (entry - exit)

@jit(nopython = True)
def get_pairs_backtest(stats, pricesA, indicatorA, pricesB, indicatorB):
    """
    Returns the Profit / Loss of a Selected Indicator and Correlated Pairs

    Long Strategy
    1. Enters Long Position when Selected Price Dips Below Indicator
    2. Closes Long Position when Selected Price Rips Above Indicator

    Short Strategy
    1. Enters Short Position when Selected Price Rips Above Indicator
    2. Closes Short Position when Selected Price Dips Below Indicator
    """

    position = False
    long_entry = 0
    long_exit = 0
    short_entry = 0
    short_exit = 0
    stats.pnl[0] = 10000
    stats.benchmark[0] = stats.pnl[0]

    for i in range(1, len(stats.pnl)):

        trade_result = 0
        stats.benchmark[i] = stats.benchmark[i - 1] + (pricesA[i] - pricesA[i - 1]) * stats.lot_size * 2

        # Enter Long Position A, Short B
        if pricesA[i] < indicatorA[i] and pricesB[i] > indicatorB[i] and position == False:
            long_entry = pricesA[i]
            short_entry = pricesB[i]
            position = True
            stats.trade_count+=1

        # Exit Long Position A, Short B
        if pricesA[i] > indicatorA[i] and pricesB[i] < indicatorB[i] and position == True:
            long_exit = pricesA[i]
            short_exit = pricesB[i]
            position = False

            trade_result = get_long_pnl(long_entry, long_exit) + get_short_pnl(short_entry, short_exit)
            if trade_result > 0:
                stats.win_rate+=1

        # Enter Short Position A, Long B
        if pricesA[i] > indicatorA[i] and pricesB[i] < indicatorB[i] and position == False:
            long_entry = pricesB[i]
            short_entry = pricesA[i]
            position = True
            stats.trade_count+=1

        # Exit Short Position A, Long B
        if pricesA[i] < indicatorA[i] and pricesB[i] > indicatorB[i] and position == True:
            long_exit = pricesB[i]
            short_exit = pricesA[i]
            position = False

            trade_result = get_long_pnl(long_entry, long_exit) + get_short_pnl(short_entry, short_exit)
            if trade_result > 0:
                stats.win_rate+=1

        if trade_result != 0:
            stats.pnl[i] = stats.pnl[i - 1] + trade_result * stats.lot_size
            stats.trade_results.append(trade_result * stats.lot_size)

        else:
            stats.pnl[i] = stats.pnl[i - 1]

    return stats