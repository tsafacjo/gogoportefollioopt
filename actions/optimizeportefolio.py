#!/usr/bin/python
# -*- coding: latin-1 -*-

from common.actions import  Action
from pandas_datareader import data as web
import numpy as np
import pandas as pd
import datetime
from functools import reduce
import subprocess
from datetime import datetime

# Opening JSON file


# returns JSON object as
# a dictionary

class OptimizedPortefolio(Action):
    """
    this action process data  datalake
    """

    def __init__(self,job):
        super().__init__(job)

        self.job = job

    def processing(self):
        ## 2 - We will look at stock prices over the past years, starting at ## January 1, 2015
        # check the output

    def generateWeights(self,n):
        """
        generate weights

        parameter :
                    n : int number of stocks
        """
        weights = np.array(np.random.random(n))
        weights /= np.sum(weights)

    def computeReturn(self, data, weights):
        """
        this function computes a return on a given portefolio

        parameter:
        input :
        data: DataFrame stocks historic
        weighst: DataFrame weight of each stocks

        output : risk
        daily return = rt+1/rt -1 

        """
        pass
    def computeRisk(self ,data ,weights):
        """
        this function computes a risk on a given portefolio

        parameter:
        input :
        data: DataFrame stocks historic
        weighst: DataFrame weight of each stocks

        output : risk
        """

        pass
    def sharpe_ratio(self):
        """

        """
        pass
