import os
import json
import string
import subprocess


required = [
        {'name': 'jquery'},
        {'name': 'underscore'},
        {'name': 'topojson'},
        {'name': 'd3'},
        {'name': 'datamaps', 
            'targets': ['http://datamaps.github.io/scripts/datamaps.usa.min.js',
                        'http://datamaps.github.io/scripts/datamaps.world.min.js'
                ]
            }
        ]

# Save
with open( 'libraries.json', 'w' ) as handle:
    json.dump( required, handle )

for requirement in required:

    if not 'targets' in requirement.keys():

        if not os.path.exists( 'node_modules/%s' % requirement['name'] ):

            print 'Installing: %s' % requirement['name']

            args = ['npm', 'install', requirement['name'] ]

            subprocess.call( args )
        
        else: 
            
            print string.rjust( '[%s]' % requirement['name'], 20 ), string.rjust( 'already installed', 20  )
   
    else :
        
        print 'Managed manually'

        try:
            os.mkdir( requirement['name'] )
        except:
            continue

        for target in requirement['targets']:

            print target


