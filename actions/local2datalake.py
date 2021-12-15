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

class Local2Datalake(Action):
    """
    this action read data from local and put it on the datalake
    """

    def __init__(self,job):
        super().__init__(job)

        self.job = job

    def processing(self):
        ## 2 - We will look at stock prices over the past years, starting at ## January 1, 2015
        # check the output
        if len(self.job.config["STORAGE"]["hdfspath"]) != 0 :
            command = "hdfs dfs -put {0}  {1}".format(self.job.config["STORAGE"]["localoutput"],datetime.now().strftime("%Y-%m-%d")+self.job.config["STORAGE"]["hdfspath"])
            subprocess.run(command, shell=True, check=True)

        if len(self.job.config["STORAGE"]["s3path"]) != 0 :

            command = "aws s3 cp {0}  {1}".format(self.job.config["STORAGE"]["localoutput"],self.job.config["STORAGE"]["s3path"])
