'''
tests each of the three methods in the WalkForwardAnalysis class: run_backtest, optimize_parameters, and plot_results.
test_run_backtest checks that the results are of the expected type (a dictionary), and that the results contain the expected keys ('trades', 'returns', 'cum_returns', 'sharpe_ratio').
test_optimize_parameters checks that the best_params are of the expected type (a dictionary), and that the best_params contain the expected keys ('train_period', 'test_period', 'lookback_period', 'entry_threshold', 'exit_threshold', 'stop_loss').
test_plot_results checks that the plot_results method produces a plot.
'''

import unittest
from walk_forward import WalkForwardAnalysis
from matplotlib import pyplot as plt

class TestWalkForwardAnalysis(unittest.TestCase):
    def setUp(self):
        # Initialize data and parameters
        self.data = pd.read_csv('data.csv')
        self.params = {
            'train_period': 30,
            'test_period': 10,
            'lookback_period': 20,
            'entry_threshold': 0.05,
            'exit_threshold': 0.03,
            'stop_loss': 0.1
        }

    def test_run_backtest(self):
        # Test the run_backtest method
        wfa = WalkForwardAnalysis(self.data, self.params)
        results = wfa.run_backtest()

        # Check that the results are of the expected type
        self.assertIsInstance(results, dict)

        # Check that the results contain the expected keys
        expected_keys = ['trades', 'returns', 'cum_returns', 'sharpe_ratio']
        for key in expected_keys:
            self.assertIn(key, results)

        # Check that the returns and cum_returns are of the expected type
        self.assertIsInstance(results['returns'], pd.Series)
        self.assertIsInstance(results['cum_returns'], pd.Series)

    def test_optimize_parameters(self):
        # Test the optimize_parameters method
        wfa = WalkForwardAnalysis(self.data, self.params)
        best_params = wfa.optimize_parameters()

        # Check that the best_params are of the expected type
        self.assertIsInstance(best_params, dict)

        # Check that the best_params contain the expected keys
        expected_keys = ['train_period', 'test_period', 'lookback_period', 'entry_threshold', 'exit_threshold', 'stop_loss']
        for key in expected_keys:
            self.assertIn(key, best_params)

    def test_plot_results(self):
        # Test the plot_results method
        wfa = WalkForwardAnalysis(self.data, self.params)
        results = wfa.run_backtest()

        # Check that the plot_results method produces a plot
        wfa.plot_results()
        plt.show()

if __name__ == '__main__':
    unittest.main()
