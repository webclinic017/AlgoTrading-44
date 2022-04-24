from matplotlib import ticker
from numba import int64, char, float64
from numba.experimental import jitclass

spec = [
    ('accountid', char[:]),
    ('ticker', char[:]),
    ('side', char[:]),
    ('quantity', int64),
    ('type', char[:]),
    ('duration', char[:]),
    ('price', float64)

]

# @jitclass(spec)
class Order:

  def __init__(self, accountid, ticker, side, quantity, type, duration, price):
    self.accountid = accountid
    self.ticker = ticker
    self.side = side 
    self.quantity = quantity
    self.type = type 
    self.duration = duration 
    self.price = price 



