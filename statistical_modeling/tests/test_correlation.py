import unittest
import pandas as pd
from correlation import calculate_correlation

class TestCorrelationAnalysis(unittest.TestCase):
    def test_calculate_correlation(self):
        # Create test DataFrame
        data = {'feature1': [1, 2, 3, 4, 5],
                'feature2': [2, 4, 6, 8, 10]}
        df = pd.DataFrame(data)

        # Test Pearson correlation coefficient calculation
        corr_coef = calculate_correlation(df, 'feature1', 'feature2')
        self.assertAlmostEqual(corr_coef, 1.0, places=2)

if __name__ == '__main__':
    unittest.main()
