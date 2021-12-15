#!/usr/bin/python
# -*- coding: latin-1 -*-

from common.actions import  Action
from pandas_datareader import data as web
import numpy as np
import pandas as pd
import datetime
from functools import reduce
import json

# Opening JSON file


# returns JSON object as
# a dictionary

class ScrapeStock(Action):
    """
    this action read stock to analyze and  get data from yahoo finance
    """

    def __init__(self,job):
        super().__init__(job)
        self.stocks = job.dataParm['symbols']
        self.job = job

    def processing(self):
        ## 2 - We will look at stock prices over the past years, starting at ## January 1, 2015
        tickers = list(self.stocks.keys())
        start = datetime.datetime(2015,1,1)
        end = datetime.datetime(2020,4,16)
        for stock in self.stocks :
            print(stock)
        ## 3 - Let's get instruments data based on the tickers.
        instruments_data = {}
        for ticker, instrument in self.stocks.items():
            instruments_data[ticker] = web.DataReader(ticker, data_source = 'yahoo', start = start, end = end)["Adj Close"]

        data = list(instruments_data.values())
        data_df = reduce(lambda x, y: pd.merge(x, y, left_index=True, right_index=True, how='outer'), data).dropna()
        data_df.columns = tickers
        data_df = data_df.melt( var_name = "symbol", ignore_index= False)
        print(" config :"+str(self.job.config))
        data_df.to_csv(self.job.config["STORAGE"]["localoutput"], encoding='utf-8')
