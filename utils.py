import numpy as np
import scipy.stats as scs

def calculate_d1_d2(S,K,r,sigma,T):
    d1 = (np.log(S/K) + (r+(sigma**2/2))*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1,d2