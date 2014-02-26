#!/usr/bin/env python

import os, json
from collections import defaultdict

from Project import Directories

class Visualiser(object):
    pass

class StateVisualiser(Visualiser):

    keys = None

    def __init__(self):

        input_data = open( os.path.join( Directories.Data() , 'train.csv' ), 'r' )

        self.keys = {}
       
        for index, key in enumerate( input_data.readline().split(',') ):
            self.keys[ key ] = index
      
        states = {} 

        states_data = defaultdict(int)

        for index, line in enumerate( input_data ):
            state = line.split(',')[ self.keys['state'] ]
            states_data[ state ] += 1

        states['fill_keys'] = [ '#FFFFFF', '#000000' ] 
        states['states_data'] = states_data

        with open( os.path.join( Directories.Stage(), 'states.json' ), 'w' ) as handle:
            json.dump( states, handle )

if __name__=="__main__":
    StateVisualiser()
