#!/usr/bin/python

import os,sys
import re
import pprint

import Utils
import Conditioners

delimiter = re.compile( "\"" )

class Predicate:

    def __init__(self):
        pass
    
    def query(self, x):
        pass

class ZeroPredicate(Predicate):

    def __init__(self):
        super(ZeroPredicate).__init__(self)

class Question:

    def __init__(self, number ):
       
        self._question_number = number

        self._data = open( '../data/individual_questions/question_%d' % number, 'r' ).read()

        components =  delimiter.split( self._data ) 

        components = filter( lambda x: (x != ",") and (not len(x) == 0) and ( not x == "\r\n"), components ) 
        
        assert( int(components[0]) == self._question_number )
   
        # Attributes
        self._title = components[1]
        try: 
            self._text = Utils.strip_tags( ' '.join( components[2:-1] ) )
        except:
            self._text = ""

        self._tags = components[-1].split()

    def __repr__(self):
        return 'Question: %d' % self._question_number + '\n' + 'Title:\t' + self._title + '\n' + 'Text:\t' + self._text + '\n' + 'Tags:\t' + ','.join( self._tags) 

if __name__=="__main__":

    print Question(83)
