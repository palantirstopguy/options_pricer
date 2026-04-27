import numpy as np

def Monte_Carlo(S0,T,r,sigma,dt,K):
    prices = np.zeros(T)
    prices[0] = S0

    for t in range(0, T-1):
        Z = np.random.randn()
        prices[t+1] = prices[t] *np.exp((r- sigma**2/2)*dt+sigma*np.sqrt(dt)*Z)
    Payoff = max(prices[T-1]-K,0)
    return Payoff