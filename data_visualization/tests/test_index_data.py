import unittest
from data_visualization.index_data import get_index_data
# use pwd to find the path to the file
import sys


class TestIndexData(unittest.TestCase):
    # use sys to access and print the file in ../../data_collection/output/sp500_stocks.csv
    print(sys.path)

    def test_get_index_data(self):
        index_data = get_index_data(filename='~/Developer/openliquid-capital/orbit/data_collection/output/sp500_stocks.csv', duration='1m')
        self.assertEqual(index_data.shape[0], 505)
        self.assertEqual(index_data.shape[1], 4)
        self.assertEqual(index_data['Symbol'].tolist()[0], 'MMM')
        
        
if __name__ == '__main__':
    unittest.main()
