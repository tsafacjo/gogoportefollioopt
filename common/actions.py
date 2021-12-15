#!/usr/bin/python
# -*- coding: latin-1 -*-

from abc import ABC, abstractmethod

class Action (ABC):

    def __init__(self,job):

        self.job = job

    @abstractmethod
    def processing(self):
        """
        traitements liés aux actions
        """
        pass

