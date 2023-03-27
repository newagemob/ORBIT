import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout


class RNN_Model:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.training_set = None
        self.testing_set = None
        self.scaler = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.regressor = None
        self.predictions = None
        self.real_stock_price = None
        
    def get_data(self):
        # Importing the training set
        dataset_train = web.DataReader(self.ticker, 'yahoo', self.start_date, self.end_date)
        training_set = dataset_train.iloc[:, 1:2].values
        return training_set

    def scale_data(self):
        # Feature Scaling
        sc = MinMaxScaler(feature_range = (0, 1))
        training_set_scaled = sc.fit_transform(self.training_set)
        return training_set_scaled
      
    def create_data_structure(self):
        sc = MinMaxScaler(feature_range = (0, 1))
        training_set_scaled = sc.fit_transform(self.training_set)
        # Creating a data structure with 60 timesteps and 1 output
        X_train = []
        y_train = []
        for i in range(60, 1258):
            X_train.append(training_set_scaled[i-60:i, 0])
            y_train.append(training_set_scaled[i, 0])
        X_train, y_train = np.array(X_train), np.array(y_train)
        return X_train, y_train
    
    def reshape_data(self):
        # Reshaping
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        return X_train
      
    def build_model(self, X_train, y_train):
        # Building the RNN
        # Initialising the RNN
        regressor = Sequential()
        # Adding the first LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
        regressor.add(Dropout(0.2))
        # Adding a second LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))
        # Adding a third LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))
        # Adding a fourth LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = 50))
        regressor.add(Dropout(0.2))
        # Adding the output layer
        regressor.add(Dense(units = 1))
        # Compiling the RNN
        regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
        # Fitting the RNN to the Training set
        regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)
        return regressor

    def predict(self):
        # Getting the real stock price of 2017
        dataset_test = web.DataReader(self.ticker, 'yahoo', self.start_date, self.end_date)
        real_stock_price = dataset_test.iloc[:, 1:2].values
        # Getting the predicted stock price of 2017
        dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0)
        inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
        inputs = inputs.reshape(-1,1)
        inputs = sc.transform(inputs)
        X_test = []
        for i in range(60, 80):
            X_test.append(inputs[i-60:i, 0])
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        predicted_stock_price = regressor.predict(X_test)
        predicted_stock_price = sc.inverse_transform(predicted_stock_price)
        return predicted_stock_price, real_stock_price
