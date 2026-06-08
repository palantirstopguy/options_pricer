import numpy as np
import scipy.stats as scs
from utils import calculate_d1_d2


def calculate_delta_call(S,K,r,sigma,T):
    d1,d2 = calculate_d1_d2(S,K,r,sigma,T)
    delta_call = scs.norm.cdf(d1)
    return delta_call

def calculate_delta_put(S,K,r,sigma,T):
    d1,d2 = calculate_d1_d2(S,K,r,sigma,T)
    delta_put = scs.norm.cdf(d1) - 1
    return delta_put

def calculate_gamma(S,K,r,sigma,T):
    d1,d2 = calculate_d1_d2(S,K,r,sigma,T)
    gamma = (scs.norm.pdf(d1)) / (S*sigma*np.sqrt(T))
    return gamma