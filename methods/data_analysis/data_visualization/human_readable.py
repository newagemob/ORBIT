import pandas as pd
import locale
from pathlib import Path
import datetime as dt

project_dir = Path(__file__).resolve().parents[3]

class HumanVisualization:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file, index_col='Symbol')

    def determine_annual_trend(self):
        print('🔮 Determining annual trend...')
        day_range = self.data['Day\'s Range'].str.split(' - ')
        year_range = self.data['52 Week Range'].str.split(' - ')
        trend = pd.Series(index=self.data.index) # create a series of the same length as the dataframe

        locale.setlocale(locale.LC_NUMERIC, '') # set locale to allow for string to float conversion

        for i in range(len(self.data)):
            if locale.atof(day_range.iloc[i][1]) > locale.atof(year_range.iloc[i][1]):
                trend.iloc[i] =  'trending upward over the year: +' + str(round(locale.atof(day_range.iloc[i][1]) - locale.atof(year_range.iloc[i][1]), 2)) + ' points. This is a good time to buy.'
            elif locale.atof(day_range.iloc[i][1]) < locale.atof(year_range.iloc[i][1]):
                trend.iloc[i] = 'trending downward over the year: -' + str(round(locale.atof(year_range.iloc[i][1]) - locale.atof(day_range.iloc[i][1]), 2)) + ' points. This is a good time to sell.'
            else:
                trend.iloc[i] = 'trending neutral over the year: ' + str(round(locale.atof(day_range.iloc[i][1]) - locale.atof(year_range.iloc[i][1]), 2)) + ' points.'
                
        print(trend)
        
        self.export_data_to_csv(data=trend, filename='annual_trend')
        
        return trend
    
    def determine_annual_spread(self):
        print('🔮 Determining annual spread...')
        
        locale.setlocale(locale.LC_NUMERIC, '')
        
        bid_ask = self.data[['Bid', 'Ask']].apply(lambda x: x.str.split(' x ').str[0])
        spread = pd.Series(index=self.data.index)

        for i in range(len(self.data)):
            if locale.atof(bid_ask.iloc[i][0]) > locale.atof(bid_ask.iloc[i][1]):
                spread.iloc[i] = 'positive spread: +' + str(round(locale.atof(bid_ask.iloc[i][0]) - locale.atof(bid_ask.iloc[i][1]), 2)) + ' points. This is a good time to buy.'
            elif locale.atof(bid_ask.iloc[i][0]) < locale.atof(bid_ask.iloc[i][1]):
                spread.iloc[i] = 'negative spread: -' + str(round(locale.atof(bid_ask.iloc[i][1]) - locale.atof(bid_ask.iloc[i][0]), 2)) + ' points. This is a good time to sell.'
            else:
                spread.iloc[i] = 'neutral spread: ' + str(round(locale.atof(bid_ask.iloc[i][0]) - locale.atof(bid_ask.iloc[i][1]), 2)) + ' points.'
        
        print(spread)
        
        self.export_data_to_csv(data=spread, filename='annual_spread')
        
        return spread
    
    def determine_annual_liquidity(self):
        print('🔮 Determining annual liquidity...')
        
        locale.setlocale(locale.LC_NUMERIC, '')
        
        volume = self.data['Volume']
        avg_volume = self.data['Avg. Volume']
        liquidity = pd.Series(index=self.data.index)
        for i in range(len(self.data)):
            if volume.iloc[i] > avg_volume.iloc[i]:
                liquidity.iloc[i] = 'liquid. The volume is ' + str(round(locale.atof(volume.iloc[i]) / locale.atof(avg_volume.iloc[i]), 2)) + ' times the average volume.'
            elif locale.atof(volume.iloc[i]) < locale.atof(avg_volume.iloc[i]):
                liquidity.iloc[i] = 'illiquid. The volume is ' + str(round(locale.atof(avg_volume.iloc[i]) / locale.atof(volume.iloc[i]), 2)) + ' times the average volume.'
            else:
                liquidity.iloc[i] = 'neither liquid nor illiquid'
                
        print(liquidity)
        
        self.export_data_to_csv(data=liquidity, filename='annual_liquidity')
        
        return liquidity
    
    def determine_annual_volatility(self):
        print('🔮 Determining annual volatility...')

        locale.setlocale(locale.LC_NUMERIC, '') # set locale to allow for string to float conversion
        
        prev_close = self.data['Previous Close']
        open_price = self.data['Open']
        volatility = pd.Series(index=self.data.index)

        for i in range(len(self.data)):
            if locale.atof(prev_close.iloc[i]) > 0:
                if locale.atof(prev_close.iloc[i]) > locale.atof(open_price.iloc[i]):
                    volatility.iloc[i] = 'volatility: -' + str(round((locale.atof(prev_close.iloc[i]) - locale.atof(open_price.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)) + '%... This is a good time to sell.'
                elif prev_close.iloc[i] < open_price.iloc[i]:
                    volatility.iloc[i] = 'volatility: +' + str(round((locale.atof(open_price.iloc[i]) - locale.atof(prev_close.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)) + '%... This is a good time to buy.'
                else:
                    volatility.iloc[i] = 'no volatility: ' + str(round((locale.atof(open_price.iloc[i]) - locale.atof(prev_close.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)) + '%'
            
        print(volatility)
        
        self.export_data_to_csv(data=volatility, filename='annual_volatility')
        
        return volatility
      
    def determine_annual_momentum(self):
        print('🔮 Determining annual momentum...')

        locale.setlocale(locale.LC_NUMERIC, '')
        
        prev_close = self.data['Previous Close']
        open_price = self.data['Open']
        day_range = self.data['Day\'s Range'].str.split(' - ')
        momentum = pd.Series(index=self.data.index)

        for i in range(len(self.data)):
            if locale.atof(prev_close.iloc[i]) > 0:
                if locale.atof(day_range.iloc[i][1]) > locale.atof(day_range.iloc[i][0]):
                    momentum.iloc[i] = 'momentum: +' + str(round((locale.atof(day_range.iloc[i][1]) - locale.atof(prev_close.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)) + '%... This is a good time to buy.'
                elif locale.atof(day_range.iloc[i][1]) < locale.atof(prev_close.iloc[i]):
                    momentum.iloc[i] = 'momentum: -' + str(round((locale.atof(prev_close.iloc[i]) - locale.atof(day_range.iloc[i][1])) / locale.atof(prev_close.iloc[i]) * 100, 2)) + '%... This is a good time to sell.'
                else:
                    momentum.iloc[i] = 'no momentum' + str(round((locale.atof(day_range.iloc[i][1]) - locale.atof(prev_close.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)) + '%'
                  
        print(momentum)
        
        self.export_data_to_csv(data=momentum, filename='annual_momentum')
        
        return momentum
    
    def export_data_to_csv(self, data, filename):
        print('🔮 Exporting data to CSV...')
        
        data.to_csv(f"{project_dir}/methods/data_analysis/data_visualization/output/SP500/human_readable/{filename}_{dt.date.today()}.csv")
        
        print('✅ Data successfully exported to CSV!')
        
    def export_data_to_json(self):
        print('🔮 Exporting data to JSON...')
        
        self.data.to_json(f"{project_dir}/methods/data_analysis/data_visualization/output/SP500/human_readable/annual_data_{dt.date.today()}.json")
        
        print('✅ Data successfully exported to JSON!')
        