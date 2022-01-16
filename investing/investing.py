import numpy as np

"""
TODO:
- IRR
- FV
- PV
- MIRR
"""


class NPV:
    """Net Present Value calculator."""
    def __init__(self, drate:float, cashflow:float, outflow:float , years:int):
        self.drate = drate
        self.cashflow = cashflow
        self.years = years
        self.outflow = outflow

    def _get_PV(self):
        """Helper method to calculate PV of cashflows."""
        discount_factor = np.array([])
        for year in range(self.years):
            year_discount_factor = np.array((1+self.drate)**(1+year))
            discount_factor = np.append(discount_factor, year_discount_factor)
        return np.round_(self.cashflow/discount_factor)

    def calculate(self):

        pv = self._get_PV()
        return np.sum(pv-self.outflow)

if __name__ == '__main__':
    npv = NPV(0.1,10000.,6000.,10)
    print(npv._get_PV())
    print(npv.calculate())
