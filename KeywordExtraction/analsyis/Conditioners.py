import string

class Conditioner(object):
    """
    Condition a string of text.
    """
    def __init__(self, text):
        self._text = text

class CaseConditioner(Conditioner):
    
    def __init__(self, text) :
        """
        Condition the case of a string of text.
        """
        super(CaseConditioner,self).__init__( text )

    def Condition(self):
        return self._text.lower()

class PunctuationConditioner(Conditioner):

    def __init__(self, text) :
        """
        Condition a string of text, removing all punctuation.
        """
        super(PunctuationConditioner,self).__init__( text )

    def Condition(self):
        replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))

        return self._text.translate( replace_punctuation )

class StopWordsConditioner(Conditioner):

    def __init__(self, text) :
        super(StopWordsConditioner,self).__init__( text )

    def Condition(self):
        self._stop_words = set( filter( lambda x: x, open( '../data/stop_words' ).read().split() ) )

        text_set = set( self._text.split() )

        return ' '.join( text_set.difference( self._stop_words ) )
