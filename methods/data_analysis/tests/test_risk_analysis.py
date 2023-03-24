from risk_analysis import risk_management

# list of stock price dataframes
stock_data_list = [stock_data1, stock_data2, stock_data3]

# list of analyses
analyses = [{'stock_data': stock_data_list[0], 'alpha': 95, 'stop_loss_percent': 0.1},
            {'stock_data': stock_data_list[1], 'alpha': 99, 'stop_loss_percent': 0.15},
            {'stock_data': stock_data_list[2], 'alpha': 90, 'stop_loss_percent': 0.05}]

# perform risk management on each stock
for i, analysis in enumerate(analyses):
    stock_data = analysis['stock_data']
    alpha = analysis['alpha']
    stop_loss_percent = analysis['stop_loss_percent']
    risk_managed_data = risk_management(stock_data, alpha, stop_loss_percent)
    # output report
    print(f"Stock {i+1} VaR: {risk_managed_data['VaR'].iloc[-1]}")
    print(f"Stop Loss Percentage: {stop_loss_percent}")
    print(f"Total Losses Due to Stop Loss: {((stock_data['Adj Close'] - risk_managed_data['Adj Close']) < 0).sum()}")
