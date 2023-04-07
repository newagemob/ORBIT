import pandas as pd
import locale
from pathlib import Path
import datetime as dt

project_dir = Path(__file__).resolve().parents[3]


class MachineLearningData:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file, index_col='Symbol')

    def determine_annual_trend(self):
        day_range = self.data['Day\'s Range'].str.split(' - ')
        year_range = self.data['52 Week Range'].str.split(' - ')
        trend = pd.Series(index=self.data.index)

        locale.setlocale(locale.LC_NUMERIC, '')

        for i in range(len(self.data)):
            if locale.atof(day_range.iloc[i][1]) > locale.atof(year_range.iloc[i][1]):
                trend.iloc[i] = round(locale.atof(
                    day_range.iloc[i][1]) - locale.atof(year_range.iloc[i][1]), 2)
            elif locale.atof(day_range.iloc[i][1]) < locale.atof(year_range.iloc[i][1]):
                trend.iloc[i] = -round(locale.atof(year_range.iloc[i]
                                       [1]) - locale.atof(day_range.iloc[i][1]), 2)
            else:
                trend.iloc[i] = 0

        df = pd.DataFrame(trend).rename(columns={0: "Annual Trend"})
        print(df.head())
        self.export_data_to_csv(
            data=df, filename='machine_readable_annual_trend')

        return df

    def determine_annual_spread(self):

        locale.setlocale(locale.LC_NUMERIC, '')

        bid_ask = self.data[['Bid', 'Ask']].apply(
            lambda x: x.str.split(' x ').str[0])
        spread = pd.Series(index=self.data.index)

        for i in range(len(self.data)):
            if locale.atof(bid_ask.iloc[i][0]) > locale.atof(bid_ask.iloc[i][1]):
                spread.iloc[i] = round(locale.atof(
                    bid_ask.iloc[i][0]) - locale.atof(bid_ask.iloc[i][1]), 2)
            elif locale.atof(bid_ask.iloc[i][0]) < locale.atof(bid_ask.iloc[i][1]):
                spread.iloc[i] = round(locale.atof(
                    bid_ask.iloc[i][1]) - locale.atof(bid_ask.iloc[i][0]), 2)
            else:
                spread.iloc[i] = round(locale.atof(
                    bid_ask.iloc[i][0]) - locale.atof(bid_ask.iloc[i][1]), 2)

        df = pd.DataFrame(spread).rename(columns={0: "Annual Spread"})
        self.export_data_to_csv(
            data=df, filename='machine_readable_annual_spread')

        return df

    def determine_annual_liquidity(self):

        volume = self.data['Volume']
        avg_volume = self.data['Avg. Volume']
        liquidity = pd.Series(index=self.data.index)

        locale.setlocale(locale.LC_NUMERIC, '')

        for i in range(len(self.data)):
            if locale.atof(volume.iloc[i]) > locale.atof(avg_volume.iloc[i]):
                liquidity.iloc[i] = round(locale.atof(
                    volume.iloc[i]) / locale.atof(avg_volume.iloc[i]), 2)
            elif locale.atof(volume.iloc[i]) < locale.atof(avg_volume.iloc[i]):
                liquidity.iloc[i] = -round(locale.atof(avg_volume.iloc[i]
                                                       ) / locale.atof(volume.iloc[i]), 2)
            else:
                liquidity.iloc[i] = 0

        df = pd.DataFrame(liquidity).rename(columns={0: "Annual Liquidity"})
        self.export_data_to_csv(
            data=df, filename='machine_readable_annual_liquidity')

        return df

    def determine_annual_volatility(self):

        prev_close = self.data['Previous Close']
        open_price = self.data['Open']
        volatility = pd.Series(index=self.data.index)

        locale.setlocale(locale.LC_NUMERIC, '')

        for i in range(len(self.data)):
            if locale.atof(prev_close.iloc[i]) > 0:
                if locale.atof(prev_close.iloc[i]) > locale.atof(open_price.iloc[i]):
                    volatility.iloc[i] = -round((locale.atof(prev_close.iloc[i]) - locale.atof(
                        open_price.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)
                elif locale.atof(prev_close.iloc[i]) < locale.atof(open_price.iloc[i]):
                    volatility.iloc[i] = round((locale.atof(open_price.iloc[i]) - locale.atof(
                        prev_close.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)
                else:
                    volatility.iloc[i] = 0
            else:
                volatility.iloc[i] = 0

        df = pd.DataFrame(volatility).rename(columns={0: "Annual Volatility"})
        self.export_data_to_csv(
            data=df, filename='machine_readable_annual_volatility')

        return df

    def determine_annual_momentum(self):

        prev_close = self.data['Previous Close']
        open_price = self.data['Open']
        momentum = pd.Series(index=self.data.index)

        locale.setlocale(locale.LC_NUMERIC, '')

        for i in range(len(self.data)):
            if locale.atof(prev_close.iloc[i]) > 0:
                if locale.atof(prev_close.iloc[i]) > locale.atof(open_price.iloc[i]):
                    momentum.iloc[i] = -round((locale.atof(prev_close.iloc[i]) - locale.atof(
                        open_price.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)
                elif prev_close.iloc[i] < open_price.iloc[i]:
                    momentum.iloc[i] = round((locale.atof(open_price.iloc[i]) - locale.atof(
                        prev_close.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)
                else:
                    momentum.iloc[i] = 0
            else:
                momentum.iloc[i] = 0

        df = pd.DataFrame(momentum).rename(columns={0: "Annual Momentum"})
        self.export_data_to_csv(
            data=df, filename='machine_readable_annual_momentum')

        return df

    def determine_annual_return(self):
        prev_close = self.data['Previous Close']
        open_price = self.data['Open']
        ret = pd.Series(index=self.data.index)

        locale.setlocale(locale.LC_NUMERIC, '')

        for i in range(len(self.data)):
            if locale.atof(prev_close.iloc[i]) > 0:
                if locale.atof(prev_close.iloc[i]) > locale.atof(open_price.iloc[i]):
                    ret.iloc[i] = -round((locale.atof(prev_close.iloc[i]) - locale.atof(
                        open_price.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)
                elif locale.atof(prev_close.iloc[i]) < locale.atof(open_price.iloc[i]):
                    ret.iloc[i] = round((locale.atof(open_price.iloc[i]) - locale.atof(
                        prev_close.iloc[i])) / locale.atof(prev_close.iloc[i]) * 100, 2)
                else:
                    ret.iloc[i] = 0
            else:
                ret.iloc[i] = 0

        df = pd.DataFrame(ret).rename(columns={0: "Annual Return"})
        self.export_data_to_csv(
            data=df, filename='machine_readable_annual_return')

        return df

    def export_data_to_csv(self, data, filename):
        print('🔮 Exporting data to CSV...')

        data.to_csv(
            f"{project_dir}/methods/data_analysis/data_visualization/output/SP500/machine_readable/{filename}_{dt.date.today()}.csv")

        print('✅ Machine Readable Data successfully exported to CSV!')

    def export_data_to_json(self, data, filename):
        print('🔮 Exporting data to JSON...')

        data.to_json(
            f"{project_dir}/methods/data_analysis/data_visualization/output/SP500/machine_readable/{filename}_{dt.date.today()}.json")

        print('✅ Data successfully exported to JSON!')
