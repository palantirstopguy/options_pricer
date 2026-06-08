from monte_carlo import Monte_Carlo
import numpy as np
from black_scholes import Black_Scholes
import greeks as gk

payoffs = []
for i in range(100000):
    payoff = Monte_Carlo(150, 155, 0.05, 0.2, 252, 1/252) #type in the values for: S0, K, r, sigma, T, dt
    payoffs.append(payoff)
avg = np.mean(payoffs)
C = avg *np.exp(-0.05*1)
print("Monte Carlo Preis: ",C)

blsc = Black_Scholes(150, 155, 0.05, 0.2, 1) #type in the values for S, K, R, sigma, T

print("Black-Scholes Preis: ",blsc)

delta_call = gk.calculate_delta_call(150,155, 0.05, 0.2, 1)
print("Delta Call: ",delta_call)

delta_put = gk.calculate_delta_put(150, 155, 0.05, 0.2, 1)
print("Delta Put: ",delta_put)

gamma = gk.calculate_gamma(150, 155, 0.05, 0.2, 1)
print("Gamma: ",gamma)