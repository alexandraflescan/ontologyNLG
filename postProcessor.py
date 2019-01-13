from nltk.corpus import words
import textwrap
from pprint import pprint
import nltk.data
import inflect

class PostProcessor():
    def __init__(self,text):
        self.text = text
    def capitalise_words(self):
         sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
         sentences = sent_tokenizer.tokenize(self.text)
         sentences = [sent.capitalize() for sent in sentences]
         self.text = ' '.join(sentences)
         return self
