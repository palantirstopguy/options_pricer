import numpy as np
import scipy.stats as scs
from utils import calculate_d1_d2

"""
    Parameter:
        S     : current stock price in USD
        K     : Strike Price
        r     : riskfree interest (e.g. 0.05 = 5%)
        sigma : Volatility of the stock (e.g. 0.2 = 20%)
        T     : Time until maturity in years (e.g. 1 = one year)

    Returns : 
        C     : fair price of the call option in USD    
"""

def Black_Scholes(S,K,r,sigma,T):

    d1,d2 = calculate_d1_d2(S, K, r, sigma, T)

    C = S * scs.norm.cdf(d1) - K*np.exp(-r*T) * scs.norm.cdf(d2)
    return C

def Black_Scholes_Put(S,K,r,sigma,T):
    d1,d2 = calculate_d1_d2(S,K,r,sigma,T)

    C = K*np.exp(-r*T) * scs.norm.cdf(-d2) - S*scs.norm(-d1)
    return C