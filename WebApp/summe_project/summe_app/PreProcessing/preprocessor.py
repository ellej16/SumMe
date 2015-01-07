from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from nltk.tokenize import wordpunct_tokenize , sent_tokenize
import nltk
import os.path
from py4j.java_gateway import JavaGateway

#edit this when changind dirs
LangPaths =os.path.realpath("C:/users/rihanna/Documents/Pol/ThesisIt/SumMe/Summarizer/langdetector/profiles/")
tltagger = nltk.data.load("taggers/fil-tagged_aubt.pickle") #filipino pos tagger

#tlChunker = nltk.data.load("chunkers/tagal")#filipino chunker here
enChunker = nltk.data.load("chunkers/treebank_chunk_ub.pickle") #enChunkerhere


punkt_param  = PunktParameters() #creates an opening for tokenizer parameters.
punkt_param.abbrev_types = set(['gng','mr','mrs','dr']) #abbreviations further accepted goes here

sentence_splitter = PunktSentenceTokenizer(punkt_param)
tokenized = ""
gateway = JavaGateway()
detector = gateway.entry_point
detector.init(LangPaths)

def LangDetect(str):
	return detector.detect(str)

def tokenizer(str):
    
    #print(wordpunct_tokenize(str))
    return wordpunct_tokenize(str)


def sentence_tokenizer(str):

    #splits input string into sentences, and returns a list of sentences.
    #for debugging purposes, remove the comment on the statement/s below.
    #print(sentence_splitter.tokenize(str.strip()))
    #print('\n-----\n'.join(sentence_splitter.tokenize(str.strip())))
	#print(sent_tokenize(str))
	return sentence_splitter.tokenize(str.strip())

def posTagger(sents):
	return nltk.pos_tag(wordpunct_tokenize(sents))

def filposTagger(sents):
	return tltagger.tag(sents)

#def tlChunk(sents):
#	return tlChunker.parse(sents)

def enChunk(sents):
	return enChunker.parse(sents)


def nerTagger(sents):
	#todo: ner tagging
	pass
