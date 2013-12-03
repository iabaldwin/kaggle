import pprint

import Question
import Document

from numpy import ndarray

class WordCooccurence:

    def __init__(self):
        self.coocurrences = {}

    def build(self):

        for i in range(1,1000):

            q = Document.Document(i)

            words = q._text.split()

            for index, word in enumerate(words):

                if word[0].isdigit():
                    continue

                # Word pair
                next_index = index + 1
                if (next_index > len(words)-1):
                    break
    

                next_word = words[next_index]
                
                self.increment_word_pair( (word, next_word ) )
   
                next_word, word = word, next_word
                
                self.increment_word_pair( (word, next_word ) )

        pprint.pprint( self.coocurrences )

    def increment_word_pair( self, word_pair  ):

        if word_pair[0] in self.coocurrences:
            if word_pair[1] in self.coocurrences[word_pair[0]]:
                self.coocurrences[word_pair[0]][word_pair[1]] = self.coocurrences[word_pair[0]][word_pair[1]] + 1
            else:
                self.coocurrences[word_pair[0]][word_pair[1]] = 0

        else:
            self.coocurrences[word_pair[0]] = {}
            self.coocurrences[word_pair[0]][word_pair[1]] = 0

if __name__=="__main__":

    WordCooccurence().build()

