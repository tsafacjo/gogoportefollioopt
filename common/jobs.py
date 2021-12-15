#!/usr/bin/python
# -*- coding: latin-1 -*-

from abc import ABC,abstractmethod
import configparser
import json


class Job(ABC):

    def __init__(self,args):

         #self.config = config
         #self.parm = parm
         self.actions = []
         print("config "+str(args.config))
         self.config = self.initConfig(args.config)
         self.dataParm =  json.load(open(args.data))
         self.context = {}

    def initConfig(self, confPath):
        """
        initialisation de la configuration

        """
        config = configparser.ConfigParser()
        config.read(confPath)
        return config

    @abstractmethod
    def workflow(self):
        """
            define the way the action will run
        """
        pass
    @abstractmethod
    def run(self):
        """
        ru
        """
        self.workflow()
        for action in self.actions:
            action.processing()

        pass

    def addAction(self,action):
        """ Add new action in the current job
        """
        self.actions.append(action)
