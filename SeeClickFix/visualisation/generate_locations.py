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

            splits = element.split(",")


            self._positions.append( (splits[1].replace( "\"", "" ) , splits[2].replace( "\"", "" )) )

        with open( target, 'w' ) as t:

            json.dump( self._positions, t )


if __name__=="__main__":

    if len(sys.argv) < 2:
        LatLongExtractor( open('../data/train.csv', 'r') ).Build( 'locations.json' )
    else:
        sys.exit( "err" )

