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

if __name__ == '__main__':

    paths = 100
    initial_price = 100
    drift = .08
    volatility = .7
    dt = 0.1/365
    T = 1
    price_paths = []

    for i in range(0, paths):
        price_paths.append(BrownianMotion(initial_price, drift, volatility, dt, T).prices)

    for price_path in price_paths:
        plt.plot(price_path)

    plt.show()
