from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from nltk.tokenize import wordpunct_tokenize , sent_tokenize
from py4j.java_gateway import JavaGateway

import nltk
from nltk.tree import Tree
import os.path
from PreProcessing import parsers



#edit this when changind dirs
LangPaths =os.path.realpath("C:/users/rihanna/Documents/Pol/ThesisIt/SumMe/Summarizer/langdetector/profiles/")
tltagger = nltk.data.load("taggers/fil-tagged_aubt.pickle") #filipino pos tagger

tlChunker = nltk.data.load("chunkers/fili_ub.pickle")#filipino chunker here
enChunker = nltk.data.load("chunkers/conll2000_ub.pickle") #enChunkerhere


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

def tlChunk(sents):
	return tlChunker.parse(sents)

def enChunk(sents):
	return enChunker.parse(sents)
	#pos = []
	#for word in sents:
	#	pos.append(word[1])
	#for tree in parsers.srParseEng(pos):
	#	chunkd = tree
		#remember if this doesnt return anything ur grammar sux
	#pos = []
	#for a in chunkd.subtrees():
	#	pos.append(a)
	#pos = clnChunk(sents,pos)
	#return pos

def clnChunk(sents,cln):
	words = []
	for word in sents:
		words.append(word[0])
	#	if libs.label==libs[0]
	#		libs[0] = words[0]
	#		words.remove(0)
	for pos in cln[0].treepositions('Leaves'):
		cln[0][pos] = cln[0][pos] = words[0]
		words.remove(words[0])
	return cln[0]

def getSVO(sent,isEnglish):
	subjs = []
	vbs = []
	objs = []
	if(isEnglish):
		for trees in sent:
			if isinstance(trees,Tree):
				for subs in trees.subtrees():
					if subs.label() == "NP":
						for node in subs:
							if node[1] in ["NN","NNS","NNP","NNPS"]:
								subjs.append(node)
								objs.append(node)
					elif subs.label() == "VP":
						for node in subs:
							if node[1] in ["VBD","VBZ","VB", "VBN","VBG","VBP"]:
								vbs.append(node)
	else:
		for trees in sent:
			if isinstance(trees,Tree):
				for subs in trees.subtrees():
					if subs.label() == "NP":
						for node in subs:
							if node[1] in ["NNT","NNST","NNPT","NNPST"]:
								subjs.append(node)
								objs.append(node)
					elif subs.label() == "VP":
						for node in subs:
							if node[1] in ["VBDT","VBZT","VBT", "VBNT","VBGT","VBPT"]:
								vbs.append(node)
	triples = []
	for subj in subjs:
		for vb in vbs:
			for obj in objs:
				triples.append(SVO(subj,vb,obj))

	return triples


def getFreqs(sent,isEnglish):
	subjs =[]
	vbs = []
	if(isEnglish):
		for trees in sent:
			if isinstance(trees,Tree):
				for subs in trees.subtrees():
					if subs.label() == "NP":
						for node in subs:
							if node[1] in ["NN","NNS","NNP","NNPS","PRP","PRP$"]:
								subjs.append(node)
					elif subs.label() == "VP":
						for node in subs:
							if node[1] in ["VBD","VBZ","VB", "VBN","VBG","VBP"]:
								vbs.append(node)
	else:
		for trees in sent:
			if isinstance(trees,Tree):
				for subs in trees.subtrees():
					if subs.label() == "NP":
						for node in subs:
							if node[1] in ["NNT","NNST","NNPT","NNPST","PRPT","PRP$T"]:
								subjs.append(node)
					elif subs.label() == "VP":
						for node in subs:
							if node[1] in ["VBDT","VBZT","VBT", "VBNT","VBGT","VBPT"]:
								vbs.append(node)
	frq = []
	tf = []
	for subj in subjs:
		if subj not in frq:
			frq.append(subj)
			tf.append((subj, 1))
		else:
			for terms in tf:
				if(terms[0]==subj):
					tf.remove(terms)
					tf.append((terms[0],terms[1]+1))
	return tf

class SVO:
	def __init__(self, subj,verb,obj):
		self.subj = subj
		self.verb = verb
		self.obj = obj
class stats:
	def __init__(self,word, tf=0, idf=0.0,augtf=None):
		self.word = word
		self.tf = tf
		self.idf = idf
		self.augtf = augtf
	def incTf():
		self.tf+=1
