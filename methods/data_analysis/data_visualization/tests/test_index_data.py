import unittest
from data_visualization.index_data import get_index_data
import sys


class TestIndexData(unittest.TestCase):
    def test_get_index_data(self):
        index_data = get_index_data(filename='~/Developer/openliquid-capital/orbit/data_collection/output/sp500_stocks.csv', duration='1w')
        self.assertEqual(len(index_data), 10)
        
        
if __name__ == '__main__':
    unittest.main()
