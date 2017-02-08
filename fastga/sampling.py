from numpy import log1p
from numpy.random import rand

def sample(cdf):
    """
    Samples a random positive bounded integer according to the Cumulative Distribution Function
	given as input (under the form of an array 'cdf', with cdf[i + 1] >= cdf[i]
    and cdf[-1] = 1. Note that these verifications are not performed by the function).
    
    The resulting integer X has the property that
        Pr(X <= i + 1) = cdf[i], for i in [0, ..., n - 1] :
    
    Pr(X = 1) = cdf[0]
    Pr(X = 2) = cdf[1] - cdf[0]
    ...
    Pr(X = n) = cdf[n - 1] - cdf[n - 2] - ... - cdf[0]

    """
    n = len(cdf)
    x = rand()
    if x < cdf[0]:
        return 1
    low = 0
    high = n - 1
    while high - low > 1:
        mid = (low + high) >> 1  # same as (low + high) // 2, but hopefully (mildly) faster
        if x > cdf[mid]:
            low = mid
        else:
            high = mid
    return high + 1


def sample_waiting_time(p):
    """
    Samples the number of independent tries until a given random event happens.
    'p' should be the probability of the event happening in one try.
    """
    x = rand()
    # We use log1p(z) to compute precisely log(1 + z) :
    return 1 + int(log1p(- x) // log1p(- p))

