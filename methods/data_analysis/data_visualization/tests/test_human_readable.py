import unittest
from methods.data_analysis.data_visualization.human_readable import HumanVisualization
from pathlib import Path
import datetime as dt

project_dir = Path(__file__).resolve().parents[3]
human_vis = HumanVisualization(f'{project_dir}/data_collection/output/SP500/yahoo_sp500_stocks_{dt.date.today()}.csv')

class TestHumanReadable(unittest.TestCase):
    def test_determine_trend(self):
        # self.assertEqual(human_vis.determine_trend(), 'positive trend:1.0')
        human_vis.determine_annual_trend()
    
    def test_determine_spread(self):
        # self.assertEqual(human_vis.determine_spread(), 'positive spread:1.0')
        human_vis.determine_annual_spread()
    
    def test_determine_liquidity(self):
        # self.assertEqual(human_vis.determine_liquidity(), 'liquid')
        human_vis.determine_annual_liquidity()

    
    def test_determine_volatility(self):
        # self.assertEqual(human_vis.determine_volatility(), 'volatility: 1.0%')
        human_vis.determine_annual_volatility()
    
    def test_determine_momentum(self):
    #     # self.assertEqual(human_vis.determine_momentum(), 'momentum: 1.0%')
        human_vis.determine_annual_momentum()
        
if __name__ == '__main__':
    unittest.main()
