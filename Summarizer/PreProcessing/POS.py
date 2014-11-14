#POS tagger
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.tag import pos_tag
def POS(str):
   
    
    return nltk.pos_tag(wordpunct_tokenize(str))
