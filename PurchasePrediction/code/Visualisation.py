#!/usr/bin/env python

import os, json
import pprint
import numpy

from collections import defaultdict
from Project import Directories

from matplotlib import cm
from matplotlib.colors import rgb2hex

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
        states_data = {}

        for index, line in enumerate( input_data ):
            state = line.split(',')[ self.keys['state'] ]
            
            if state in states_data:
                states_data[ state ]['count'] += 1
            else:
                states_data[ state ] = {}
                states_data[ state ]['count'] = 0

        # Compute scaling
        scaling = numpy.max( [ value[1]['count'] for value in states_data.iteritems() ] )

        # Assign colors
        jet_colormap = cm.get_cmap('Blues')

        fills = {}

        for key, value in states_data.iteritems():
            fills[ key ] = rgb2hex( jet_colormap(float(value['count'])/scaling) )

        fills['defaultFill'] = rgb2hex( jet_colormap(0) )

        # Assign fill keys
        for key, value in states_data.iteritems():
            states_data[ key ][ 'fillKey' ] = key
       
        states['states_data'] = states_data
        states['fill_keys'] = fills

        with open( os.path.join( Directories.Stage(), 'states.json' ), 'w' ) as handle:
            json.dump( states, handle )

if __name__=="__main__":
    StateVisualiser()
