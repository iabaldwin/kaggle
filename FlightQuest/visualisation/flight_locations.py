#!/usr/bin/python

import os,sys
import json
import pprint


class LatLongExtractor:

    def __init__(self,target):

        self._target = target

    def Build(self, target):

        self._positions = []

        for element in self._target:

            element.replace( "\"", "" ) 

            splits = element.split(",")

            self._positions.append( { 'lat': splits[4], 'long': splits[5], 'airport': splits[2] })

        with open( target, 'w' ) as t:

            json.dump( self._positions, t )


if __name__=="__main__":


    if len(sys.argv) < 2:
        LatLongExtractor( open('../data/TestFlights.csv', 'r') ).Build( 'flight_locations.json' )
    else:
        sys.exit( "err" )

