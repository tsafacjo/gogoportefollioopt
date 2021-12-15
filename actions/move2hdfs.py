#!/usr/bin/python
# -*- coding: latin-1 -*-

from common.actions import  Action

class ScrapeStock(Action):
    """
    this action move stock data from local file system to hdfs
    """

    def __init__(self,context):
        super().__init__(context)

    def processing(self):
        print("ok dans ")
