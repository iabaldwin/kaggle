import Question
import Conditioners
import Dictionary

import sklearn.feature_extraction.text

class Document(object):

    def __init__(self, question_number ):
        
        self._question_number = question_number
        self._question = Question.Question( self._question_number )

        text = Conditioners.PunctuationConditioner( self._question._text ).Condition() 
        text = Conditioners.CaseConditioner( text ).Condition() 
        text = Conditioners.StopWordsConditioner( text ).Condition()

        self._text = text
        self._tags = self._question._tags

if __name__=="__main__":

    vocabulary = Dictionary.Dictionary().Build()

    f = Document( 1 )

    print f._tags
