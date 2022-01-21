import numpy as np

"""
TODO:
- IRR
- FV
- MIRR
"""


class Financials:
    """Net Present Value calculator."""
    def __init__(self, drate:float, cashflow:float, outflow:float , years:int):
        self.drate = drate
        self.cashflow = cashflow
        self.years = years
        self.outflow = outflow

    def _get_DCF(self):
        """Helper method to calculate PV of cashflows."""
        years_array = np.arange(1, self.years+1)
        return np.round_(self.cashflow/(1+self.drate)**(years_array))

    def calc_NPV(self):
        dcf = self._get_DCF()
        return np.sum(dcf-self.outflow)

    def calc_PV(self):
        return np.sum(self._get_DCF())

if __name__ == '__main__':
    npv = Financials(0.1,10000.,8000.,10)
    print(npv._get_DCF())
    print(npv.calc_PV())
    print(npv.calc_NPV())
