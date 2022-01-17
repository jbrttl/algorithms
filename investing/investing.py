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
        years_array = np.arange(1, self.years+1)
        discount_factor = (1+self.drate)**(years_array)
        return np.round_(self.cashflow/discount_factor)

    def calc_NPV(self):
        pv = self._get_PV()
        return np.sum(pv-self.outflow)

if __name__ == '__main__':
    npv = NPV(0.1,10000.,0.,10)
    print(npv._get_PV())
    print(npv.calc_NPV())
