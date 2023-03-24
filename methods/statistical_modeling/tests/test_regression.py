import pandas as pd
import unittest
from regression import RegressionAnalysis

class TestRegressionAnalysis(unittest.TestCase):

    def setUp(self):
        self.ra = RegressionAnalysis('cleaned_stock_data.csv', 'price', ['feature1', 'feature2'])

    def test_add_constant_term(self):
        self.ra.add_constant_term()
        self.assertEqual(self.ra.X.columns[0], 'const')

    def test_fit_linear_regression(self):
        self.ra.add_constant_term()
        self.ra.fit_linear_regression()
        self.assertAlmostEqual(self.ra.model.params[0], -3.921309e+01, delta=1e-5)
        self.assertAlmostEqual(self.ra.model.params[1], 1.252154e+00, delta=1e-5)
        self.assertAlmostEqual(self.ra.model.params[2], 7.965201e-03, delta=1e-5)

if __name__ == '__main__':
    unittest.main()
