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
def get_pairs_backtest(stats, pricesA, pricesB, indicatorObj, contrarian):
    """
    Returns the Profit / Loss of a Selected Indicator and Correlated Pairs

    Long Strategy
    *Contrarian = True does Opposite*
    1. Enters Long Position when Selected Price Dips Below Indicator
    2. Closes Long Position when Selected Price Rips Above Indicator

    Short Strategy
    *Contrarian = True does Opposite*
    1. Enters Short Position when Selected Price Rips Above Indicator
    2. Closes Short Position when Selected Price Dips Below Indicator
    """

    longA = False
    shortA = False
    longB = False
    shortB = False

    long_entry = 0
    long_exit = 0
    short_entry = 0
    short_exit = 0
    stats.pnl[0] = 10000
    stats.benchmark[0] = stats.pnl[0]

    # Case One
    if contrarian == True:

        for i in range(1, len(stats.pnl)):

            trade_result = 0
            stats.benchmark[i] = stats.benchmark[i - 1] + (pricesA[i] - pricesA[i - 1]) * stats.lot_size * 2

            # Enter Long Position A, Short B
            priceA = pricesA[i] > indicatorObj.moving_averageA[i]
            volA = indicatorObj.volatilityA[i] < indicatorObj.volatility_clusterA[indicatorObj.long_cluster]
            vol_volA = indicatorObj.vol_of_volA[i] < indicatorObj.vol_of_vol_clusterA[indicatorObj.long_cluster]

            priceB = pricesB[i] < indicatorObj.moving_averageB[i]
            volB = indicatorObj.volatilityA[i] > indicatorObj.volatility_clusterB[indicatorObj.short_cluster]
            vol_volB = indicatorObj.vol_of_volA[i] > indicatorObj.vol_of_vol_clusterB[indicatorObj.short_cluster]

            corr = indicatorObj.corr[i] < indicatorObj.corr_cluster[indicatorObj.long_cluster]

            if (priceA and (volA or vol_volA) and priceB and (volB or vol_volB) and corr) and (longA == False and shortA == False) and (longB == False and shortB == False):
                long_entry = pricesA[i]
                short_entry = pricesB[i]
                longA = True
                shortB = True
                stats.trade_count+=1

            # Exit Long Position A, Short B
            priceA = pricesA[i] < indicatorObj.moving_averageA[i]
            priceB = pricesB[i] > indicatorObj.moving_averageB[i]

            if (priceA and priceB) and (longA == True and shortA == False) and (longB == False and shortB == True):
                long_exit = pricesA[i]
                short_exit = pricesB[i]
                longA = False
                shortB = False

                # Log Trade Results
                trade_result = get_long_pnl(long_entry, long_exit) + get_short_pnl(short_entry, short_exit)
                if trade_result > 0:
                    stats.win_rate+=1

            # Enter Short Position A, Long B
            priceA = pricesA[i] < indicatorObj.moving_averageA[i]
            volA = indicatorObj.volatilityA[i] > indicatorObj.volatility_clusterA[indicatorObj.short_cluster]
            vol_volA = indicatorObj.vol_of_volA[i] > indicatorObj.vol_of_vol_clusterA[indicatorObj.short_cluster]

            priceB = pricesB[i] > indicatorObj.moving_averageB[i]
            volB = indicatorObj.volatilityA[i] < indicatorObj.volatility_clusterB[indicatorObj.long_cluster]
            vol_volB = indicatorObj.vol_of_volA[i] < indicatorObj.vol_of_vol_clusterB[indicatorObj.long_cluster]

            corr = indicatorObj.corr[i] < indicatorObj.corr_cluster[indicatorObj.long_cluster]

            if (priceA and (volA or vol_volA) and priceB and (volB or vol_volB) and corr) and (longA == False and shortA == False) and (longB == False and shortB == False):
                long_entry = pricesB[i]
                short_entry = pricesA[i]
                longB = True
                shortA = True
                stats.trade_count+=1

            # Exit Short Position A, Long B
            priceA = pricesA[i] > indicatorObj.moving_averageA[i]
            priceB = pricesB[i] < indicatorObj.moving_averageB[i]

            if (priceA and priceB) and (longA == False and shortA == True) and (longB == True and shortA == False):
                long_exit = pricesB[i]
                short_exit = pricesA[i]
                longB = False
                shortA = False

                trade_result = get_long_pnl(long_entry, long_exit) + get_short_pnl(short_entry, short_exit)
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
            stats.benchmark[i] = stats.benchmark[i - 1] + (pricesA[i] - pricesA[i - 1]) * stats.lot_size * 2

            # Enter Long Position A, Short B
            priceA = pricesA[i] < indicatorObj.moving_averageA[i]
            volA = indicatorObj.volatilityA[i] < indicatorObj.volatility_clusterA[indicatorObj.long_cluster]
            vol_volA = indicatorObj.vol_of_volA[i] < indicatorObj.vol_of_vol_clusterA[indicatorObj.long_cluster]

            priceB = pricesB[i] > indicatorObj.moving_averageB[i]
            volB = indicatorObj.volatilityA[i] > indicatorObj.volatility_clusterB[indicatorObj.short_cluster]
            vol_volB = indicatorObj.vol_of_volA[i] > indicatorObj.vol_of_vol_clusterB[indicatorObj.short_cluster]

            corr = indicatorObj.corr[i] < indicatorObj.corr_cluster[indicatorObj.long_cluster]

            if ((priceA or (volA or vol_volA)) or (priceB or (volB or vol_volB)) and corr) and (longA == False and shortA == False) and (longB == False and shortB == False):
                long_entry = pricesA[i]
                short_entry = pricesB[i]
                longA = True
                shortB = True
                stats.trade_count+=1

            # Exit Long Position A, Short B
            priceA = pricesA[i] > indicatorObj.moving_averageA[i]
            priceB = pricesB[i] < indicatorObj.moving_averageB[i]

            if (priceA and priceB) and (longA == True and shortA == False) and (longB == False and shortB == True):
                long_exit = pricesA[i]
                short_exit = pricesB[i]
                longA = False
                shortB = False

                trade_result = get_long_pnl(long_entry, long_exit) + get_short_pnl(short_entry, short_exit)
                if trade_result > 0:
                    stats.win_rate+=1

            # Enter Short Position A, Long B
            priceA = pricesA[i] > indicatorObj.moving_averageA[i]
            volA = indicatorObj.volatilityA[i] > indicatorObj.volatility_clusterA[indicatorObj.short_cluster]
            vol_volA = indicatorObj.vol_of_volA[i] > indicatorObj.vol_of_vol_clusterA[indicatorObj.short_cluster]

            priceB = pricesB[i] < indicatorObj.moving_averageB[i]
            volB = indicatorObj.volatilityA[i] < indicatorObj.volatility_clusterB[indicatorObj.long_cluster]
            vol_volB = indicatorObj.vol_of_volA[i] < indicatorObj.vol_of_vol_clusterB[indicatorObj.long_cluster]

            corr = indicatorObj.corr[i] < indicatorObj.corr_cluster[indicatorObj.long_cluster]

            if ((priceA or (volA or vol_volA)) or (priceB or (volB or vol_volB)) and corr) and (longA == False and shortA == False) and (longB == False and shortB == False):
                long_entry = pricesB[i]
                short_entry = pricesA[i]
                longB = True
                shortA = True
                stats.trade_count+=1

            # Exit Short Position A, Long B
            priceA = pricesA[i] < indicatorObj.moving_averageA[i]
            priceB = pricesB[i] > indicatorObj.moving_averageB[i]

            if (priceA and priceB) and (longA == False and shortA == True) and (longB == True and shortB == False):
                long_exit = pricesB[i]
                short_exit = pricesA[i]
                longB = False
                shortA = False

                trade_result = get_long_pnl(long_entry, long_exit) + get_short_pnl(short_entry, short_exit)
                if trade_result > 0:
                    stats.win_rate+=1

            if trade_result != 0:
                stats.pnl[i] = stats.pnl[i - 1] + trade_result * stats.lot_size
                stats.trade_results.append(trade_result * stats.lot_size)

            else:
                stats.pnl[i] = stats.pnl[i - 1]

    return stats




