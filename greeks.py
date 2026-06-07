import numpy as np
import scipy.stats as scs
from utils import calculate_d1_d2


def delta_call(S,K,r,sigma,T):
    d1,d2 = calculate_d1_d2(S,K,r,sigma,T)
    d_call = scs.norm.cdf(d1)
    return d_call

def delta_put(S,K,r,sigma,T):
    d1,d2 = calculate_d1_d2(S,K,r,sigma,T)
    d_put = scs.norm.cdf(d1) - 1
    return d_put

def gamma(S,K,r,sigma,T):
    d1,d2 = calculate_d1_d2(S,K,r,sigma,T)
    g = (scs.norm.pdf(d1)) / (S*sigma*np.sqrt(T))
    return g