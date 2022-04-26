import numpy as np
from numba import jit

@jit(nopython = True)
def get_long_pnl(entry, exit):
    """
    Return Profit / Loss from Long Trade
    """

    pnl = exit - entry

    return pnl

@jit(nopython = True)
def get_short_pnl(entry, exit):
    """
    Return Profit / Loss from Short Trade
    """

    pnl = entry - exit

    return pnl

@jit(nopython = True)
def get_vanilla_backtest(stats, prices, indicator, contrarian = True):
    """
    Returns the Profit / Loss of a Selected Indicator

    Long Strategy 
    *Contrarian = True does Opposite*
    1. Enters Long Position when Selected Price Dips Below Indicator
    2. Closes Long Position when Selected Price Rips Above Indicator

    Short Strategy
    *Contrarian = True does Opposite*
    1. Enters Short Position when Selected Price Rips Above Indicator
    2. Closes Short Position when Selected Price Dips Below Indicator
    """

    long_position = False
    short_position = False
    entry = 0
    exit = 0
    stats.pnl[0] = 10000
    stats.benchmark[0] = stats.pnl[0]

    # Case One 
    if contrarian == True:

        for i in range(1, len(stats.pnl)):

            trade_result = 0
            stats.benchmark[i] = stats.benchmark[i - 1] + (prices[i] - prices[i - 1]) * stats.lot_size

            # Enter Long Position
            if (prices[i] > indicator[i]) and (long_position == False and short_position == False):
                entry = prices[i]
                long_position = True
                stats.trade_count+=1

            # Exit Long Position
            if (prices[i] < indicator[i]) and (long_position == True and short_position == False):
                exit = prices[i]
                long_position = False

                # Log Results
                trade_result = get_long_pnl(entry, exit)
                if trade_result > 0:
                    stats.win_rate+=1

            # Enter Short Position
            if (prices[i] < indicator[i]) and (long_position == False and short_position == False):
                entry = prices[i]
                short_position = True
                stats.trade_count+=1

            # Exit Short Position
            if prices[i] > indicator[i] and (long_position == False and short_position == True):
                exit = prices[i]
                short_position = False

                # Log Results
                trade_result = get_short_pnl(entry, exit)
                if trade_result > 0:
                    stats.win_rate+=1

            if trade_result != 0:
                stats.pnl[i] = stats.pnl[i - 1] + trade_result * stats.lot_size
                stats.trade_results.append(trade_result * stats.lot_size)

            else:
                stats.pnl[i] = stats.pnl[i - 1]

    # Case Two
    if contrarian == False:

        for i in range(1, len(stats.pnl)):

            trade_result = 0
            stats.benchmark[i] = stats.benchmark[i - 1] + (prices[i] - prices[i - 1]) * stats.lot_size

            # Enter Long Position
            if (prices[i] < indicator[i]) and (long_position == False and short_position == False):
                entry = prices[i]
                long_position = True
                stats.trade_count+=1

            # Exit Long Position
            if (prices[i] > indicator[i]) and (long_position == True and short_position == False):
                exit = prices[i]
                long_position = False

                # Log Results
                trade_result = get_long_pnl(entry, exit)
                if trade_result > 0:
                    stats.win_rate+=1

            # Enter Short Position
            if (prices[i] > indicator[i]) and (long_position == False and short_position == False):
                entry = prices[i]
                short_position = True
                stats.trade_count+=1

            # Exit Short Position
            if (prices[i] < indicator[i]) and (long_position == False and short_position == True):
                exit = prices[i]
                short_position = False

                # Log Results
                trade_result = get_short_pnl(entry, exit)
                if trade_result > 0:
                    stats.win_rate+=1

            if trade_result != 0:
                stats.pnl[i] = stats.pnl[i - 1] + trade_result * stats.lot_size
                stats.trade_results.append(trade_result * stats.lot_size)

            else:
                stats.pnl[i] = stats.pnl[i - 1]

    return stats

@jit(nopython = True)
def get_bands_backtest(stats, prices, indicator, upper_bands, lower_bands):
    """
    Returns the Profit / Loss of a Selected Indicator with Bollinger Bands

    Long Strategy
    1. Enters Long Position when Selected Price Dips Below Lower Band
    2. Closes Long Position when Selected Price Rips Above Indicator

    Short Strategy
    1. Enters Short Position when Selected Price Rips Above Upper Band
    2. Closes Short Position when Selected Price Dips Below Indicator
    """

    position = False
    entry = 0
    exit = 0
    stats.pnl[0] = 10000
    stats.benchmark[0] = stats.pnl[0]

    for i in range(1, len(stats.pnl)):

        trade_result = 0
        stats.benchmark[i] = stats.benchmark[i - 1] + (prices[i] - prices[i - 1]) * stats.lot_size

        # Enter Long Position
        if prices[i] < lower_bands[i] and position == False:
            entry = prices[i]
            position = True
            stats.trade_count+=1

        # Exit Long Position
        if prices[i] > indicator[i] and position == True:
            exit = prices[i]
            position = False

            trade_result = get_long_pnl(entry, exit)
            if trade_result > 0:
                stats.win_rate+=1

        # Enter Short Position
        if prices[i] > upper_bands[i] and position == False:
            entry = prices[i]
            position = True
            stats.trade_count+=1

        # Exit Short Position
        if prices[i] < indicator[i] and position == True:
            exit = prices[i]
            position = False

            trade_result = get_short_pnl(entry, exit)
            if trade_result > 0:
                stats.win_rate+=1

        if trade_result != 0:
            stats.pnl[i] = stats.pnl[i - 1] + trade_result * stats.lot_size
            stats.trade_results.append(trade_result * stats.lot_size)

        else:
            stats.pnl[i] = stats.pnl[i - 1]

    return stats