#!/usr/bin/env python
import os

class Directories:

    @staticmethod
    def __SubDirectory__( subdir ):
       return os.path.join( os.path.dirname(os.path.realpath(__file__)), subdir )

    @staticmethod
    def Data():
       return Directories.__SubDirectory__('data')

    @staticmethod
    def Code():
       return Directories.__SubDirectory__('code')

    @staticmethod
    def Stage():
       return Directories.__SubDirectory__('stage')
