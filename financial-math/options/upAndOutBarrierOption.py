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


class UpandOutBarrierOption:
    def __init__(self,strike,barrier_level):
        self.strike = strike
        self.barrier_level = barrier_level
        self.barrier_trigger = False

    def check_barrier(self,stock_price):
        if stock_price>self.barrier_level:
            self.barrier_level = True

    def get_payoff(self,stock_price):
        if not self.barrier_trigger:
            if stock_price>self.strike:
                return stock_price - self.strike
            else:
                return 0
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

    # Up and Out barrier option

    barrier_payoff = list()
    risk_free_rate = 0.01
    for price_path in price_paths:
        bc = UpandOutBarrierOption(100,100.5)
        for price in price_path:
            bc.check_barrier(price)
        barrier_payoff.append(bc.get_payoff(price_path[-1])/(1+risk_free_rate))

    for price_path in price_paths:
        plt.plot(price_path)
    plt.show()
    print(np.average(barrier_payoff)*100)
