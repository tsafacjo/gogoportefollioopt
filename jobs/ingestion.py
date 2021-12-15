#!/usr/bin/python
# -*- coding: latin-1 -*-

from common.jobs import  Job
from actions.scrapestock import ScrapeStock
from actions.local2datalake import Local2Datalake


class Ingestion(Job):

    def __init__(self,context):
        super().__init__(context)


    def workflow(self):
        scrapeStock = ScrapeStock(self)
        self.addAction(scrapeStock)
        local2Datalake = Local2Datalake(self)
        self.addAction(local2Datalake)

    def addAction(self,action):
        """ Add new action in the current job
        """
        self.actions.append(action)
    def run(self):
        super().run()
