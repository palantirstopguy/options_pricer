from monte_carlo import Monte_Carlo
import numpy as np
from black_scholes import Black_Scholes

payoffs = []
for i in range(10000):
    payoff = Monte_Carlo(150, 155, 0.05, 0.2, 252, 1/252) #type in the values for: S0, K, r, sigma, T, dt
    payoffs.append(payoff)
avg = np.mean(payoffs)
C = avg *np.exp(-0.05*1)
print("Monte Carlo Preis: ",C)

blsc = Black_Scholes(150, 155, 0.05, 0.2, 1) #type in the values for S, K, R, sigma, T
print("Black-Scholes Preis: ",blsc)