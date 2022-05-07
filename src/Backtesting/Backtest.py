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
def get_vanilla_backtest(stats, prices, indicatorObj, period, isContrarian):
    """
    Returns the Profit / Loss of a Selected Indicator

    Long Strategy 
    *Contrarian = True does Opposite*
    1. Enters Long Position when:
        - Selected Price Dips Below Indicator
        - Selected Volatility Dips Below Cluster

    2. Closes Long Position when:
        - Selected Price Rips Above Indicator

    Short Strategy
    *Contrarian = True does Opposite*
    1. Enters Short Position when:
        - Selected Price Rips Above Indicator
        - Selected Price Rips Above Cluster
        
    2. Closes Short Position when:
        - Selected Price Dips Below Indicator
    """

    long_position = False
    short_position = False
    entry = 0
    exit = 0
    stats.pnl[0] = 10000
    stats.benchmark[0] = stats.pnl[0]

    # Case One 
    if isContrarian == True:

        for i in range(1, len(stats.pnl)):

            trade_result = 0
            stats.benchmark[i] = stats.benchmark[i - 1] + (prices[i] - prices[i - 1]) * stats.lot_size

            # Enter Long Position
            price = prices[i] > indicatorObj.moving_average[i]
            vol = indicatorObj.volatility[i] > indicatorObj.volatility_cluster[indicatorObj.long_cluster]
            vol_vol = indicatorObj.vol_of_vol[i] > indicatorObj.vol_of_vol_cluster[indicatorObj.long_cluster]

            # Evaluate Long Entry Logic
            if (price and vol and vol_vol) and (long_position == False and short_position == False):

                entry = prices[i]
                long_position = True
                stats.trade_count+=1

            # Exit Long Position
            price = prices[i] < indicatorObj.moving_average[i]

            # Evaluate Long Exit Logic
            if (price) and (long_position == True and short_position == False):

                exit = prices[i]
                long_position = False

                # Log Results
                trade_result = get_long_pnl(entry, exit)
                if trade_result > 0:
                    stats.win_rate+=1

            # Enter Short Position
            price = prices[i] < indicatorObj.moving_average[i]
            vol = indicatorObj.volatility[i] < indicatorObj.volatility_cluster[indicatorObj.short_cluster]
            vol_vol = indicatorObj.vol_of_vol[i] < indicatorObj.vol_of_vol_cluster[indicatorObj.short_cluster]

            # Evaluate Short Entry Logic
            if (price and vol and vol_vol) and (long_position == False and short_position == False):

                entry = prices[i]
                short_position = True
                stats.trade_count+=1

            # Exit Short Exit Position
            price = prices[i] > indicatorObj.moving_average[i]

            # Evaluate Short Logic
            if (price) and (long_position == False and short_position == True):

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
    if isContrarian == False:

        for i in range(1, len(stats.pnl)):

            trade_result = 0
            stats.benchmark[i] = stats.benchmark[i - 1] + (prices[i] - prices[i - 1]) * stats.lot_size

            # Enter Long Position
            price = prices[i] < indicatorObj.moving_average[i]
            vol = indicatorObj.volatility[i] < indicatorObj.volatility_cluster[indicatorObj.long_cluster]
            vol_vol = indicatorObj.vol_of_vol[i] < indicatorObj.vol_of_vol_cluster[indicatorObj.long_cluster]

            # Evaluate Long Entry Logic
            if (price and vol and vol_vol) and (long_position == False and short_position == False):

                entry = prices[i]
                long_position = True
                stats.trade_count+=1

            # Exit Long Position
            price = prices[i] > indicatorObj.moving_average[i]

            # Evaluate Long Exit Logic
            if (price) and (long_position == True and short_position == False):
                exit = prices[i]
                long_position = False

                # Log Results
                trade_result = get_long_pnl(entry, exit)
                if trade_result > 0:
                    stats.win_rate+=1

            # Enter Short Position
            price = prices[i] > indicatorObj.moving_average[i]
            vol = indicatorObj.volatility[i] > indicatorObj.volatility_cluster[indicatorObj.short_cluster]
            vol_vol = indicatorObj.vol_of_vol[i] > indicatorObj.vol_of_vol_cluster[indicatorObj.short_cluster]

            # Evaluate Short Entry Logic
            if (price and vol and vol_vol) and (long_position == False and short_position == False):

                entry = prices[i]
                short_position = True
                stats.trade_count+=1

            # Exit Short Exit Position
            price = prices[i] < indicatorObj.moving_average[i]

            # Evaluate Short Logic
            if (price) and (long_position == False and short_position == True):
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



