import numpy as np
from numba import int64, float64, types, typed
from numba.experimental import jitclass

spec = [
    ('lot_size', int64),
    ('mean', float64),
    ('std', float64),
    ('pnl', float64[:]),
    ('win_rate', float64),
    ('trade_count', int64),
    ('trade_results', types.ListType(float64)),
    ('benchmark', float64[:])
]

@jitclass(spec)
class Statistics:

  def __init__(self, lot_size, length):
      self.lot_size = lot_size * 100
      self.mean = 0
      self.std = 0
      self.pnl = np.zeros(length)
      self.win_rate = 0
      self.trade_count = 0
      self.trade_results = typed.List.empty_list(float64)
      self.benchmark = np.zeros(length)