import pprint

import Question
import Conditioners

class Dictionary:

    def __init__(self):
        self._dict = set()

    def Build(self):
           
        for i in range(1,100):
            q = Question.Question(i)
   
            text = q._text 
         
            text = Conditioners.PunctuationConditioner( text ).Condition()
            text = Conditioners.StopWordsConditioner( text ).Condition()

            self._dict |= set( text.split() )

        return self

if __name__=="__main__":

    Dictionary().Build()
