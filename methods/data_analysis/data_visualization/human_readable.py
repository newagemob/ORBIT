import pandas as pd

class HumanVisualization:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file, index_col='Symbol')

    def determine_trend(self):
        day_range = self.data['Day\'s Range'].str.split(' - ')
        year_range = self.data['52 Week Range'].str.split(' - ')
        trend = pd.Series(index=self.data.index)
        for i in range(len(self.data)):
            if float(day_range.iloc[i][0]) > float(year_range.iloc[i][0]) and float(day_range.iloc[i][1]) > float(year_range.iloc[i][1]):
                trend.iloc[i] =  'trending upward ' + str(round(float(day_range.iloc[i][1]) - float(year_range.iloc[i][1]), 2)) + ' points. This is a good time to buy.'
            elif float(day_range.iloc[i][0]) < float(year_range.iloc[i][0]) and float(day_range.iloc[i][1]) < float(year_range.iloc[i][1]):
                trend.iloc[i] = 'trending downward ' + str(round(float(year_range.iloc[i][0]) - float(day_range.iloc[i][0]), 2)) + ' points. This is a good time to sell.'
            else:
                trend.iloc[i] = 'no trend'
                
        print(trend)
        return trend
    
    def determine_spread(self):
        bid_ask = self.data[['Bid', 'Ask']].apply(lambda x: x.str.split(' x ').str[0].astype(float))
        spread = pd.Series(index=self.data.index)
        for i in range(len(self.data)):
            if bid_ask.iloc[i][0] > bid_ask.iloc[i][1]:
                spread.iloc[i] = 'negative spread: ' + str(round(bid_ask.iloc[i][0] - bid_ask.iloc[i][1], 2)) + '. This is a good time to buy.'
            elif bid_ask.iloc[i][0] < bid_ask.iloc[i][1]:
                spread.iloc[i] = 'positive spread: ' + str(round(bid_ask.iloc[i][1] - bid_ask.iloc[i][0], 2)) + '. This is a good time to sell.'
            else:
                spread.iloc[i] = 'no spread'
        print(spread)
        return spread
    
    def determine_liquidity(self):
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
    
    def determine_volatility(self):
        prev_close = self.data['Previous Close'].astype(float)
        open_price = self.data['Open'].astype(float)
        volatility = pd.Series(index=self.data.index)
        for i in range(len(self.data)):
            if prev_close.iloc[i] > 0:
                if prev_close.iloc[i] > open_price.iloc[i]:
                    volatility.iloc[i] = 'volatility: -' + str(round((prev_close.iloc[i] - open_price.iloc[i]) / prev_close.iloc[i] * 100, 2)) + '%. This indicates a bearish trend.'
                elif prev_close.iloc[i] < open_price.iloc[i]:
                    volatility.iloc[i] = 'volatility: +' + str(round((open_price.iloc[i] - prev_close.iloc[i]) / prev_close.iloc[i] * 100, 2)) + '%. This indicates a bullish trend.'
                else:
                    volatility.iloc[i] = 'no volatility'
                  
        print(volatility)
        return volatility
      
    def determine_momentum(self):
        prev_close = self.data['Previous Close'].astype(float)
        day_range = self.data['Day\'s Range'].str.split(' - ').apply(lambda x: x.str.replace(',', '').astype(float))
        momentum = pd.Series(index=self.data.index)
        for i in range(len(self.data)):
            if prev_close.iloc[i] > 0:
                if prev_close.iloc[i] > day_range.iloc[i][0]:
                    momentum.iloc[i] = 'momentum: -' + str(round((prev_close.iloc[i] - day_range.iloc[i][0]) / prev_close.iloc[i] * 100, 2)) + '%'
                elif prev_close.iloc[i] < day_range.iloc[i][0]:
                    momentum.iloc[i] = 'momentum: +' + str(round((day_range.iloc[i][0] - prev_close.iloc[i]) / prev_close.iloc[i] * 100, 2)) + '%'
                else:
                    momentum.iloc[i] = 'no momentum'
                  
        print(momentum)
        return momentum
      