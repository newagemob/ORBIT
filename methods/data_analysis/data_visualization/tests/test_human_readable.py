import unittest
from methods.data_analysis.data_visualization import human_readable
from pathlib import Path

project_dir = Path(__file__).resolve().parents[3]
human_vis = human_readable.HumanVisualization(f'{project_dir}/data_collection/output/SP500/yahoo_sp500_stocks_2023-03-24.csv')

class TestHumanReadable(unittest.TestCase):
    def test_determine_trend(self):
        # self.assertEqual(human_vis.determine_trend(), 'positive trend:1.0')
        human_vis.determine_trend()
    
    def test_determine_spread(self):
        # self.assertEqual(human_vis.determine_spread(), 'positive spread:1.0')
        human_vis.determine_spread()
    
    def test_determine_liquidity(self):
        # self.assertEqual(human_vis.determine_liquidity(), 'liquid')
        human_vis.determine_liquidity()

    
    def test_determine_volatility(self):
        # self.assertEqual(human_vis.determine_volatility(), 'volatility: 1.0%')
        human_vis.determine_volatility()
    
    # def test_determine_momentum(self):
    #     # self.assertEqual(human_vis.determine_momentum(), 'momentum: 1.0%')
    #     human_vis.determine_momentum()
        
if __name__ == '__main__':
    unittest.main()
