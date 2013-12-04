#!/usr/bin/python

import sys
import json
import utils
import pprint
import itertools

class Airport:

    def __init__(self,airport_string):

        keys = airport_string.split( ':' )
        
        self._icode     = keys[0]
        self._code      = keys[1]
        self._name      = keys[2]
        self._province  = keys[3]
        self._country   = keys[4]
        self._northing  = keys[5:9]
        self._easting   = keys[9:13]

        try:
            self._lat  = utils.Geo.NorthingEastingToDecimal( *self._northing )
            self._long = utils.Geo.NorthingEastingToDecimal( *self._easting )
        
        except:
            self._lat = self._long = float('NaN')

    #def __repr__(self):
        #return '[%s, %s] <%s,%s> @ [%s, %s][%f, %f]' % (self._icode, self._code, self._name, self._country, ' '.join(self._northing), ' '.join( self._easting), self._lat, self._long )

class Airports:

    def __init__(self, airports_file ):

        with open( airports_file, 'r' ) as handle:
        
            airports = filter( lambda x: x, handle.read().split( '\n' ) )
 
            self._airports = map( lambda x: Airport(x), airports )
    
    def __getitem__(self,_str):
       
        return [item for item in self._airports if (item._code == _str )]

    def __repr__(self):

        return self._airports.__repr__() 

    def ToJson(self):

        #locations = []
        #[ locations.append( airport_tuple )  for airport_tuple in map( lambda airport: (airport._lat, airport._long), self._airports ) ]
   
        valid_locations = []
        for airport in self._airports:
            if ( airport._country == "USA" and airport._lat > 10.0  ):

                valid_locations.append( { 'designator': airport._icode, 'lat':airport._lat, 'long':airport._long } )

        with open( 'airport_locations.json', 'w' ) as handle:
            json.dump(valid_locations, handle )

if __name__=="__main__":

    A = Airports( '../data/USAirports.txt' )

    A.ToJson()

