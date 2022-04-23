from numba import int64, char
from numba.experimental import jitclass

spec = [
    ('api_key', char[:]),
    ('ticker', char[:]),
    ('months', int64)
]

# @jitclass(spec)
class Client:

  def __init__(self, api_key, ticker, months):
    self.api_key = api_key
    self.ticker = ticker
    self.months = months


