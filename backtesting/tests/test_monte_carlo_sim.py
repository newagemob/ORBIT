'''
the sim test first loads the input data from a CSV file generated earlier by the pipeline, then runs a series of tests to ensure that the simulation runs without errors, the output shape matches the input shape, the output columns are correct, and the output values are within expected ranges.
'''

import unittest
import pandas as pd
from monte_carlo_sim import MonteCarloSimulation

class TestMonteCarloSimulation(unittest.TestCase):

    def setUp(self):
        # Load input data from CSV file
        self.input_data = pd.read_csv('test_input_data.csv')

    def test_simulation_runs(self):
        # Test that the simulation runs without errors
        simulation = MonteCarloSimulation(self.input_data)
        simulation.run_simulation()

    def test_output_shape(self):
        # Test that the output shape matches the input shape
        simulation = MonteCarloSimulation(self.input_data)
        simulation.run_simulation()
        output_data = simulation.get_output()
        self.assertEqual(self.input_data.shape, output_data.shape)

    def test_output_columns(self):
        # Test that the output columns are correct
        simulation = MonteCarloSimulation(self.input_data)
        simulation.run_simulation()
        output_data = simulation.get_output()
        expected_columns = ['date', 'portfolio_value', 'portfolio_returns']
        self.assertEqual(list(output_data.columns), expected_columns)

    def test_output_values(self):
        # Test that the output values are within expected ranges
        simulation = MonteCarloSimulation(self.input_data)
        simulation.run_simulation()
        output_data = simulation.get_output()
        # Check that portfolio value is non-negative
        self.assertGreaterEqual(output_data['portfolio_value'].min(), 0)
        # Check that returns are within a reasonable range
        self.assertLess(output_data['portfolio_returns'].max(), 10)
        self.assertGreater(output_data['portfolio_returns'].min(), -10)

if __name__ == '__main__':
    unittest.main()
