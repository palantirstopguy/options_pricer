# Options Pricer

A Python implementation of two classical options pricing models: **Black-Scholes** and **Monte Carlo Simulation**. Built as a quantitative finance learning project.

## What this project does

Given a set of market parameters, this pricer calculates the fair price of a **European Call Option** using two independent methods and compares the results.

A European Call Option gives the buyer the right — but not the obligation — to purchase a stock at a fixed price (Strike Price) at a specific point in the future.

## Models

### Black-Scholes
An analytical formula that calculates the exact theoretical price of a European Call Option. Based on the assumption that stock prices follow a Geometric Brownian Motion.

### Monte Carlo Simulation
A numerical method that simulates thousands of random stock price paths until the option's expiry date. The fair price is approximated as the discounted average payoff across all simulations.

Both methods should converge to a similar price — the closer they are, the more simulations were run.

## Project Structure

```
options_pricer/
├── black_scholes.py    # Black-Scholes analytical formula
├── monte_carlo.py      # Monte Carlo simulation
└── main.py             # Runs both models and compares results
```

## Parameters

| Parameter | Description | Example |
|---|---|---|
| `S` | Current stock price in USD | 150 |
| `K` | Strike Price — the price you have the right to buy at | 155 |
| `r` | Risk-free interest rate | 0.05 (= 5%) |
| `sigma` | Volatility of the stock | 0.2 (= 20%) |
| `T` | Time to expiry in years | 1 |

## Usage

```python
from black_scholes import Black_Scholes
from monte_carlo import Monte_Carlo
import numpy as np

# Black-Scholes
price_bs = Black_Scholes(S=150, K=155, r=0.05, sigma=0.2, T=1)

# Monte Carlo (10,000 simulations)
payoffs = [Monte_Carlo(S0=150, K=155, r=0.05, sigma=0.2, T=252, dt=1/252) for _ in range(10000)]
price_mc = np.mean(payoffs) * np.exp(-0.05 * 1)

print(f"Black-Scholes Price: {price_bs:.4f}")
print(f"Monte Carlo Price:   {price_mc:.4f}")
```

## Example Output

```
Black-Scholes Price: 13.1698
Monte Carlo Price:   13.3821
```

## Dependencies

```
numpy
scipy
```

Install with:
```bash
pip install numpy scipy
```

## Concepts covered

- Geometric Brownian Motion
- Stochastic Differential Equations (SDEs)
- Log-normal distribution of returns
- Risk-neutral pricing
- Time value of money (discounting)
- Law of Large Numbers (Monte Carlo convergence)
