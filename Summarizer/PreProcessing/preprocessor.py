from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from nltk.tokenize import wordpunct_tokenize
#from nltk.tag import pos_tag
import nltk
punkt_param  = PunktParameters() #creates an opening for tokenizer parameters.
punkt_param.abbrev_types = set(['gng']) #abbreviations further accepted goes here

sentence_splitter = PunktSentenceTokenizer(punkt_param)
tokenized = ""



def tokenizer(str):
    
    #print(wordpunct_tokenize(str))
    return wordpunct_tokenize(str)


def sentence_tokenizer(str):

	#splits input string into sentences, and returns a list of sentences.
    #for debugging purposes, remove the comment on the statement/s below.
    #print(sentence_splitter.tokenize(str.strip()))
    #print('\n-----\n'.join(sentence_splitter.tokenize(str.strip())))
	return sentence_splitter.tokenize(str.strip())

def posTagger(sents):
	return nltk.pos_tag(wordpunct_tokenize(sents))

def nerTagger(sents):
	#todo: ner tagging
	pass