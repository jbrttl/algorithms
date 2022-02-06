"""
Before we can model the price of derivative securities whose value depends on an
underlying equity — we need to model the underlying equity. Geometric Brownian motion
is a stochastic process that can be used to generate sample paths that the underlying
equity may follow. In other words, we can use geometric Brownian motion to simulate stock
prices.
"""

import matplotlib.pyplot as plt
import numpy as np
import math

class BrownianMotion:

    def __init__(self,initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.normal(0,math.sqrt(self.dt)) # Brownian motion
            dYt = self.drift*self.dt + self.volatility*dWt # Change in price
            self.current_price *= (1+dYt) # Add change to the current price
            self.prices.append(self.current_price)
            self.T -= self.dt # Account for the step in time

class EuropeanCallPayoff:

    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self,stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 0


if __name__ == '__main__':

    paths = 100
    initial_price = 100
    drift = .08
    volatility = .3
    dt = 1/365
    T = 1
    price_paths = []

    for i in range(0, paths):
        price_paths.append(BrownianMotion(initial_price, drift, volatility, dt, T).prices)


    # European call
    call_payoffs = []
    ec = EuropeanCallPayoff(100)
    risk_free_rate = .01

    for price_path in price_paths:
        call_payoffs.append(ec.get_payoff(price_path[-1])/(1+risk_free_rate))

    for price_path in price_paths:
        plt.plot(price_path)

    plt.show()

    print(np.average(call_payoffs)*100)
