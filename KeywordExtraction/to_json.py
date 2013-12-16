#!/usr/bin/python

import json
import pprint

data = open( 'data.tsv' ).read().split( '\n' )

json_data = {}

for d in data:
   
    datum = d.split( '\t' )
 
    if len(datum) == 1:
        break

    json_data[datum[0]] = datum[1]

pprint.pprint( json_data )

with open( 'data.json', 'w' ) as handle:

    json.dump( json_data, handle )

