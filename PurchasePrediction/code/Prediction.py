import os
import csv
import numpy
import sklearn
import cPickle

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

from sklearn import cross_validation

from Project import Directories

class Predictor(object):
  
    def _load_(self,target):

        binary_target = os.path.join( Directories.Stage(), target + '.bin' )
        
        if os.path.exists( binary_target ):
            with open( binary_target, 'rb' ) as handle:
                return cPickle.load( handle )
        else: 
            with open( os.path.join( Directories.Data(), target ), 'r' ) as handle:

                header = [ element for element in handle.readline().split('\n')[0].split(',') if element ]

                keys = dict( zip( header, range(0,len(header))))

                parsed_data = numpy.array( list( csv.reader( handle ) ) )

                data = {'data': parsed_data, 'keys': keys }

                cPickle.dump( data, open( binary_target, 'wb' ), cPickle.HIGHEST_PROTOCOL )
    
                return data

class NaiveBayes(Predictor):

    def __init__(self, target ):

        record = self._load_( target )

        keys = record['keys']
        data = record['data']

        #clf = MultinomialNB()
        clf = BernoulliNB()

        X = numpy.array(data[:,[keys['cost'],0]])
        y = numpy.array(data[:,keys['record_type']])
    
        X = numpy.reshape( X, (X.shape[0], -1 ) )
    
        X_train, X_test, y_train, y_test = cross_validation.train_test_split( X, y, test_size=0.4, random_state=0)

        clf.fit( X_train, y_train )
    
if __name__=="__main__":
    
    NaiveBayes( 'train.csv' )
