#!/usr/bin/python

import os,sys
import json
import pprint

import Utils
import Document

class Tags:

    def __init__(self): 
        self._tag_list = {}

        for i in range( 1, 1000 ):

            f = Document.Document( i )
   
            #self._tag_list |= set( f._tags )

            for tag in f._tags:

                if tag in self._tag_list:
                    self._tag_list[tag] = self._tag_list[tag]  + 1
                else:
                    self._tag_list[tag] = 1
    
    def __repr__(self):

        #print zip( self._tag_list.keys(), self._tag_list.values() ) 
        #return '\n'.join( map( lambda x: ' '.join(x), zip( self._tag_list.keys(), self._tag_list.values() ) )
        return ' '.join( self._tag_list.keys() )

    def write( self, destination ):
    
        with open( destination, 'w' ) as file_descriptor:

            json.dump( self._tag_list, file_descriptor )

if __name__=="__main__":

    tags = Tags()

    tags.write( 'data/tag_cloud.json' )

