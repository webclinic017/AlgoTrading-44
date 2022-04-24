from numba import int64, char
from numba.experimental import jitclass

spec = [
    ('endpoint', char[:]),
    ('api_key', char[:]),
    ('accountid', char[:]),
    ('ticker', char[:]),
    ('months', int64)
]

# @jitclass(spec)
class Client:

  def __init__(self, endpoint, api_key, accountid, ticker, months):
    self.endpoint = endpoint
    self.api_key = api_key
    self.accountid = accountid
    self.ticker = ticker
    self.months = months


