import numpy as np

"""
    Parameter:
        S0    : Starting price of the stock in USD
        K     : Strike Price
        r     : riskfree interest (e.g. 0.05 = 5%)
        sigma : Volatility of the stock (e.g. 0.2 = 20%)
        T     : Number of time steps (e.g. 252 trading days = one year)
        dt    : size of a single time step in years (e.g. 1/252 for one trading day)

    Returns : 
        C     : fair price of the call option in USD    
"""


def Monte_Carlo(S0,K,r,sigma,T,dt):
    prices = np.zeros(T)
    prices[0] = S0

    for t in range(0, T-1):
        Z = np.random.randn()
        prices[t+1] = prices[t] *np.exp((r- sigma**2/2)*dt+sigma*np.sqrt(dt)*Z)
    Payoff = max(prices[T-1]-K,0)
    return Payoff