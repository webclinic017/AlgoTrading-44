import numpy as np
from numba import jit

@jit(nopython = True)
def chandrupatla_method(lower, upper, prices, indicator, par, stats, function):
    """
    Returns a Local Maximum given a Moving Average Interval
    """

    # Initialization
    b = lower
    a = upper
    c = a 
    t = 0.5

    par.period = b
    fb = function(stats, prices, indicator)

    par.period = a 
    fa = function(stats, prices, indicator)
    fc = fa

    # Iteration
    itr_count = 0
    while a != b or a != c:

        xt = int(a + t * (b - a))

        par.period = xt
        ft = function(stats, prices, indicator)

        if np.sign(ft) == np.sign(fa):

            c = a 
            fc = fa 
            a = xt 
            fa = ft

        else: 

            c = b 
            b = a 
            a = xt 
            fc = fb 
            fb = fa 
            fa = ft

        xm = a 
        fm = fa

        if np.abs(fb) < np.abs(fa):

            xm = b 
            fm = fb

        

        itr_count+=1

    return xt