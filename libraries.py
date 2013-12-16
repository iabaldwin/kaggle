#!/usr/bin/python

import os, json
import string
import subprocess

required = [
        {'name': 'jquery', 'lang': 'js' },
        {'name': 'underscore', 'lang': 'js' },
        {'name': 'topojson', 'lang': 'js' },
        {'name': 'd3', 'lang': 'js' },
        {'name': 'datamaps', 
            'targets': [ 
                { 'url': 'http://datamaps.github.io/scripts/datamaps.usa.min.js' },
                { 'url': 'http://datamaps.github.io/scripts/datamaps.world.min.js' }
                ],
            'lang': 'js'
            },
       
        {'name': 'geopy', 'lang': 'py'}
        ]

class ResourceManager(object):

    def __init__(self):
        pass

class URLResourceManager(ResourceManager):

    def __init__(self, targets, destination ):
        
        super( URLResourceManager, self ).__init__()
        self._destination   = destination
        self._targets       = targets

    def Get(self):
       
        for target in self._targets:
            args = ['wget', '--quiet', '--no-clobber', '--directory-prefix', self._destination , target['url'] ]
            subprocess.call( args )

class LanguageManager(object):

    def __init__( self ):
        pass

class JSLanguageManager(LanguageManager):

    def __init__(self):
        super( JSLanguageManager, self ).__init__()

        if not os.path.exists( 'libraries/js/node_modules' ):
            os.makedirs( 'libraries/js/node_modules' )

    def Manage(self, requirement ):

        if 'targets' in requirement.keys():
            URLResourceManager( requirement['targets'], 'libraries/js/%s' % requirement['name']).Get()
        else:
            if not os.path.exists( 'libraries/js/node_modules/%s' % requirement['name'] ):

                print 'Installing: %s' % requirement['name']

                args = ['npm', 'install',  '--prefix', 'libraries/js/', requirement['name'] ]

                subprocess.call( args )
                
            else: 
                    
                print string.rjust( '[%s]' % requirement['name'], 20 ), string.rjust( 'already installed', 20  )

class PYLanguageManager(LanguageManager):

    def __init__(self):
        super( PYLanguageManager, self ).__init__()

    def Manage(self, requirement ):

        if 'targets' in requirement.keys():
            URLResourceManager( requirement['targets'], 'libraries/py/%s' % requirement['name']).Get()

        else:
            destination = os.path.join( os.getcwd(), 'libraries/py/' )

            if not os.path.exists( 'libraries/py/lib/python2.7/site-packages/%s' % requirement['name' ] ):
                
                args = ['pip', 'install', '--install-option=--prefix=%s' % destination, requirement['name'] ]

                subprocess.call( args )

            else:

                print string.rjust( '[%s]' % requirement['name'], 20 ), string.rjust( 'already installed', 20  )


if __name__=="__main__":

    # Save
    with open( 'libraries.json', 'w' ) as handle:
        json.dump( required, handle )

    managers = { 'js': JSLanguageManager, 'py': PYLanguageManager }

    for requirement in required:
        # Manage with respective package managers
        managers[requirement['lang']]().Manage( requirement )
