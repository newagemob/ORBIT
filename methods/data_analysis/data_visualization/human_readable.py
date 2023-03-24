import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file

class HumanVisualization:
    def __init__(self, df):
        self.df = df

# Function to display top 10 companies by market cap
    def top_10(self):
        top_10 = self.df.sort_values(by='Market Cap', ascending=False).head(10)
        plt.barh(top_10['Company'], top_10['Market Cap'])
        plt.xlabel('Market Cap (in billions)')
        plt.title('Top 10 Companies by Market Cap')
        plt.show()


    # Function to display bottom 10 companies by market cap
    def bottom_10(self):
        bottom_10 = self.df.sort_values(by='Market Cap').head(10)
        plt.barh(bottom_10['Company'], bottom_10['Market Cap'])
        plt.xlabel('Market Cap (in billions)')
        plt.title('Bottom 10 Companies by Market Cap')
        plt.show()


    # Function to display top 10 companies by volume
    def top_10_by_volume(self):
        self.df['Volume'] = self.df['Volume'].str.replace(',', '').astype(float)
        top_10 = self.df.sort_values(by='Volume', ascending=False).head(10)
        plt.barh(top_10['Company'], top_10['Volume'])
        plt.xlabel('Volume')
        plt.title('Top 10 Companies by Volume')
        plt.show()


    # Function to display bottom 10 companies by volume
    def bottom_10_by_volume(self):
        self.df['Volume'] = self.df['Volume'].str.replace(',', '').astype(float)
        bottom_10 = self.df.sort_values(by='Volume').head(10)
        plt.barh(bottom_10['Company'], bottom_10['Volume'])
        plt.xlabel('Volume')
        plt.title('Bottom 10 Companies by Volume')
        plt.show()


    def top_10_chg(self):
        self.df['% Chg'] = self.df['% Chg'].str.replace('(', '-').str.replace(')', '').str.replace('%', '').astype(float)
        top_10_pos = self.df.nlargest(10, '% Chg')
        top_10_neg = self.df.nsmallest(10, '% Chg')
        top_10 = pd.concat([top_10_pos, top_10_neg]).sort_values(by='% Chg', ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(top_10['Symbol'], top_10['% Chg'], color=top_10['% Chg'] > 0, height=0.6)
        ax.set_title('Top 10 Stocks by Percentage Change')
        ax.set_xlabel('% Change')
        ax.set_ylabel('Symbol')
        ax.axvline(0, color='black', linewidth=0.5)
        plt.show()
