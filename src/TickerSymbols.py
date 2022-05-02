import pandas as pd
import numpy as np

def get_ticker_symbols():
    """
    Read Tickers Symbols CSV and convert to Numpy Array
    """

    df = pd.read_csv('QQQTickers.csv')
    ticker_array = df.to_numpy()

    return ticker_array


    