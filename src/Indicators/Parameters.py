from numba import int64
from numba.experimental import jitclass

spec = [
    ('period', int64),
    ('projection', int64)
]

@jitclass(spec)
class Parameters:

  def __init__(self, period, projection):
    self.period = period
    self.projection = projection

