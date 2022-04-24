from .OHLC import Prices
import requests
from numba import jit
from datetime import datetime
from dateutil.relativedelta import relativedelta

# @jit(nopython = True)
def get_ohlc(Dict, length):

    OHLC = Prices(length)

    for i in range(length):
        OHLC.open[i] = Dict[i]["open"]
        OHLC.high[i] = Dict[i]["high"]
        OHLC.low[i] = Dict[i]["low"]
        OHLC.close[i] = Dict[i]["close"]

    return OHLC

def get_historical_data(client):
    """
    Fetch Historical Data

    Inputs:
    1. Api Key
    2. Ticker Symbol
    3. Numbers of Months 
    """

    current_date = datetime.today()
    past_date = current_date - relativedelta(months = client.months)

    current_date = current_date.strftime('%Y-%m-%d')
    past_date = past_date.strftime('%Y-%m-%d')

    response = requests.get(
        
        'https://' + client.endpoint + '/v1/markets/history',

        params = {
            'symbol': client.ticker, 
            'interval': 'daily', 
            'start': past_date, 
            'end': current_date,
            },

        headers = {
            'Authorization': 'Bearer ' + client.api_key, 
            'Accept': 'application/json'
            })

    json_response = response.json()
    length = len(json_response["history"]["day"])
    ohlc = get_ohlc(json_response["history"]["day"], length)

    return ohlc