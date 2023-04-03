import pandas as pd
import locale

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
        return trend
    
    def determine_annual_spread(self):
        print('🔮 Determining annual spread...')
        
        locale.setlocale(locale.LC_NUMERIC, '')
        
        bid_ask = self.data[['Bid', 'Ask']].apply(lambda x: x.str.split(' x ').str[0].astype(float))
        spread = pd.Series(index=self.data.index)
        for i in range(len(self.data)):
            if bid_ask.iloc[i][0] > bid_ask.iloc[i][1]:
                spread.iloc[i] = 'positive spread: +' + str(round(bid_ask.iloc[i][0] - bid_ask.iloc[i][1], 2)) + ' points. This is a good time to buy.'
            elif bid_ask.iloc[i][0] < bid_ask.iloc[i][1]:
                spread.iloc[i] = 'negative spread: -' + str(round(bid_ask.iloc[i][1] - bid_ask.iloc[i][0], 2)) + ' points. This is a good time to sell.'
            else:
                spread.iloc[i] = 'neutral spread: ' + str(round(bid_ask.iloc[i][1] - bid_ask.iloc[i][0], 2)) + ' points.'
        
        print(spread)
        return spread
    
    def determine_annual_liquidity(self):
        print('🔮 Determining annual liquidity...')
        
        volume = self.data['Volume'].str.replace(',', '').astype(float)
        avg_volume = self.data['Avg. Volume'].str.replace(',', '').astype(float)
        liquidity = pd.Series(index=self.data.index)
        for i in range(len(self.data)):
            if volume.iloc[i] > avg_volume.iloc[i]:
                liquidity.iloc[i] = 'liquid. The volume is ' + str(round(volume.iloc[i] / avg_volume.iloc[i], 2)) + ' times the average volume.'
            elif volume.iloc[i] < avg_volume.iloc[i]:
                liquidity.iloc[i] = 'illiquid. The volume is ' + str(round(avg_volume.iloc[i] / volume.iloc[i], 2)) + ' times the average volume.'
            else:
                liquidity.iloc[i] = 'neither liquid nor illiquid'
                
        print(liquidity)
        return liquidity
    
    def determine_annual_volatility(self):
        print('🔮 Determining annual volatility...')

        locale.setlocale(locale.LC_NUMERIC, '') # set locale to allow for string to float conversion
        
        prev_close = self.data['Previous Close'].astype(float)
        open_price = self.data['Open'].astype(float)
        volatility = pd.Series(index=self.data.index)

        for i in range(len(self.data)):
            if prev_close.iloc[i] > 0:
                if prev_close.iloc[i] > open_price.iloc[i]:
                    volatility.iloc[i] = 'volatility: -' + str(round((prev_close.iloc[i] - open_price.iloc[i]) / prev_close.iloc[i] * 100, 2)) + '%... This is a good time to sell.'
                elif prev_close.iloc[i] < open_price.iloc[i]:
                    volatility.iloc[i] = 'volatility: +' + str(round((open_price.iloc[i] - prev_close.iloc[i]) / prev_close.iloc[i] * 100, 2)) + '%... This is a good time to buy.'
                else:
                    volatility.iloc[i] = 'no volatility: ' + str(round((open_price.iloc[i] - prev_close.iloc[i]) / prev_close.iloc[i] * 100, 2)) + '%'
            
        print(volatility)
        return volatility
      
    def determine_annual_momentum(self):
        print('🔮 Determining annual momentum...')

        locale.setlocale(locale.LC_NUMERIC, '')
        
        prev_close = self.data['Previous Close'].astype(float)
        open_price = self.data['Open'].astype(float)
        day_range = self.data['Day\'s Range'].str.split(' - ')
        momentum = pd.Series(index=self.data.index)

        for i in range(len(self.data)):
            if prev_close.iloc[i] > 0:
                if locale.atof(day_range.iloc[i][1]) > prev_close.iloc[i]:
                    momentum.iloc[i] = 'momentum: +' + str(round((locale.atof(day_range.iloc[i][1]) - prev_close.iloc[i]) / prev_close.iloc[i] * 100, 2)) + '%... This is a good time to buy.'
                elif locale.atof(day_range.iloc[i][1]) < prev_close.iloc[i]:
                    momentum.iloc[i] = 'momentum: -' + str(round((prev_close.iloc[i] - locale.atof(day_range.iloc[i][1])) / prev_close.iloc[i] * 100, 2)) + '%... This is a good time to sell.'
                else:
                    momentum.iloc[i] = 'no momentum: ' + str(round((prev_close.iloc[i] - locale.atof(day_range.iloc[i][1])) / prev_close.iloc[i] * 100, 2)) + '%'
                  
        print(momentum)
        return momentum
      