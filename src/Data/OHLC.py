import numpy as np
from numba import int64, float64
from numba.experimental import jitclass

spec = [
    ('length', int64),
    ('open', float64[:]),
    ('high', float64[:]),
    ('low', float64[:]),
    ('close', float64[:])
]

@jitclass(spec)
class Prices:

  def __init__(self, length):
    self.open = np.zeros(length)
    self.high = np.zeros(length)
    self.low = np.zeros(length)
    self.close = np.zeros(length)


