import numpy as np
import scipy.stats as scs

def Black_Scholes(S,K,r,T,sigma):
    d1 = (np.log(S/K) + (r+(sigma**2/2))*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    C = S * scs.norm.cdf(d1) - K*np.exp(-r*T) * scs.norm.cdf(d2)
    return C

