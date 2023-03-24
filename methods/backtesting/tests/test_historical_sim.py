'''
@ ** VaR is a measure of risk and should therefore always be negative. **

an example test script for the historical_simulation function.
test data is a csv file with a single column of returns.
test script creates a pandas series from the returns column and passes it to the historical_simulation function.
test script then checks that the function returns a float and that the float is negative.
'''

import unittest
import pandas as pd
from historical_simulation import historical_simulation

class TestHistoricalSimulation(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.read_csv("test_data.csv")
    
    def test_historical_simulation(self):
        returns = self.test_data["returns"]
        portfolio_value = 10000
        alpha = 0.05
        VaR = historical_simulation(returns, portfolio_value, alpha)
        self.assertIsInstance(VaR, float)
        self.assertLess(VaR, 0)
        
if __name__ == '__main__':
    unittest.main()
