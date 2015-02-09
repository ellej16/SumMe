'author pol'
from PreProcessing import preprocessor
import math
from NLG.pynlg.realizer import Clause, ImperativeClause, PrepositionalPhrase, NounPhrase, SubjectPredicate, PredicateSubject, VerbPhrase
from NLG.pynlg.lexicon import Word, XMLLexicon, Noun, Determiner, Adjective,Verb
import NLG.Sample3 as nlg
from nltk.tree import Tree
#should contain these:
#a list containing:
	#sentence number,
	#sentence itself
	#words(this would be a dict)
		#word
		#POS tag
article =  [] #is this shit even needed

global sentences
global terms
global sentenceTh
global CandidSVO

sentenceTh = 0



sentences = []
			# 0 sentence number, 
			#1 the sentence, 
			#2 the tuples of words 0 = word 1 = pos 
			#  their corresponding POS tags, and 
			# the 3 language id
			#4when chunkSents is invoked chunks of the sentence is appended
			#5when getTriple() is invoked svos of the sentence is appended
			#6when getFreq() is invoked frequencies of the sentences is also appended(subjects only)
			#7 when getSentScore is inovked
terms = []
CandidSVO = []
#class Sentence:
#	self.SentNum
#	self.langId
#	self.Sent
#	self.SentenceScore
#	self.Words
#	self.Chunks


def chunkSents():
	global sentences
	for sents in sentences:
		if sents[3] =="en":
			sents.append(preprocessor.enChunk(sents[2]))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			sents.append(preprocessor.tlChunk(sents[2]))
			sentences[sents[0]] = sents
	#return sentences

def getSenScore(sent, isEnglish):
	sentScore = 0
	if isEnglish:
		for word in sent[2]:
			if word[1] in ["NN","NNS","NNP","NNPS","VBD","VBZ","VB", "VBN","VBG","VBP","MD",
							"JJ","JJR","JJS"]:
				sentScore = sentScore + 0.75
			elif word[1] in ["RBR","RBS","RP","."]:
				sentScore  = sentScore + 0.25
			else:
				sentScore = sentScore + 0.50
	else:
		pass
	sentScore = sentScore/len(sent[2])
	return sentScore

def getSenThreshold():
	global sentenceTh
	for sent in sentences:
		sentenceTh = sentenceTh + sent[7]
	sentenceTh = sentenceTh/len(sentences)
	return sentenceTh



def clearMem():
	global sentences 
	sentences = []
	#return sentences

def getTriple():
	global sentences
	for sents in sentences:
		if sents[3] =="en":
			sents.append(preprocessor.getSVO(sents[0],sents[2],True))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			sents.append(preprocessor.getSVO(sents[0],sents[2],False))
			sentences[sents[0]] = sents
	#return sentences



def getSentences(str):
	
	sents  = preprocessor.sentence_tokenizer(str)
	sentNum = 0
	sentence = [] 
	global sentences
	sentences = []
	for sent in sents:
		sentence.append(sentNum)
		sentence.append(sent)
		ID = preprocessor.LangDetect(sent)
		if ID == "en":
			sentence.append(getPOS(sent))
			sentence.append(ID)
			print(ID+" "+sent)
		elif ID =="tl":
			sentence.append(getFilPOS(preprocessor.tokenizer(sent)))
			sentence.append(ID)
			print(ID+" "+sent)
		else :
			sentence.append(getPOS(sent))
			sentence.append(ID)
			print(ID+" "+sent)
		sentNum+=1
		sentences.append(sentence)
		sentence = []
		
	#return sentences
	#article.append(sentences)
	
	#article = [] #clears the article altogether
	#for sent in article:
	#	print(sent)
	#	print("\n")
	
def getPOS(sent):
	words = []
	POS = preprocessor.posTagger(sent)
	for item in POS:
		word = (item[0],item[1])
		words.append(word)
	return words



def getFilPOS(sent):
	words = []
	return preprocessor.filposTagger(sent)

def getFreq():
	global sentences
	for sents in sentences:
		if sents[3] =="en":
			sents.append(preprocessor.getFreqs(sents[4],True))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			sents.append(preprocessor.getFreqs(sents[4],False))
			sentences[sents[0]] = sents
	#return sentences
	#	idf = math.log10(len(sentences)/n[1])
	#	print(idf)
	#	ideff.append((n[0],idf))
def getIDF():
	#currently gets idfs of subjects/nouns only
	global sentences
	global terms
	nWords = []
	
	for sents in sentences:
		for tup in sents[6]:
			if tup[0][0] not in nWords:
				nWords.append(tup[0][0])
	nDocs = Docs(nWords,[0]*len(nWords))
	for sents in sentences:
		for tup in sents[6]:
			if tup[0][0] in nWords :
				nDocs.show[nDocs.words.index(tup[0][0])] +=1
	for n in nDocs.words:
		idf = math.log10(len(sentences)/nDocs.show[nDocs.words.index(n)])
		terms.append((n,nDocs.show[nDocs.words.index(n)]*idf))

def sortTerms():
	global terms
	terms = sorted(terms,key= lambda t : t[1] , reverse = True)


def getCandidSubjs(start, end):
	global sentences
	global terms
	global CandidSVO
	for sents in sentences:
		for svo in sents[5]:
			if svo.sNum in getAcSents():
				for term in  terms[start:end]:
					if svo.subj[0] == term[0] and svo.obj[0]==term[0]:
						continue
					elif svo.subj[0]==term[0]:
						CandidSVO.append(svo)
					elif svo.obj[0] == term[0]:
						CandidSVO.append(svo)
	clnCandSubjs(start,end)

def clnCandSubjs(start,end):

	global CandidSVO
	global terms
	dltMe = False
	for svo in CandidSVO:
		for term in terms[start:end]:
			if(svo.subj[0]==term[0]):
				continue
			else:
				dltMe = True
		if dltMe:
			CandidSVO.remove(svo)
			dltMe = False



def getAcSents():
	global sentences
	acc = []
	for sent in sentences:
		if sent[7] >= sentenceTh:
			acc.append(sent[0])
	return acc


def doGet():

	global sentenceTh
	chunkSents()
	getTriple()
	getFreq()
	getIDF()
	sortTerms()
	for sent in sentences:
		sent.append(getSenScore(sent, True))
		sentences[sent[0]] = sent
	getSenThreshold()
	print(sentenceTh)

def doGetAll():
	doGet()
	getCandidSubjs(None,10)
	genSents()

def genSents():

	

	global CandidSVO
	global sentences
	global dis
	dis = []
	lex = XMLLexicon()
	lsubj = []
	lobj = []
	lverb = []
	for svo in CandidSVO:
		print(str(svo.sNum),svo.subj[0]+" "+svo.verb[0]+" "+svo.obj[0])
		for trees in sentences[svo.sNum][4]:
			if isinstance(trees,Tree):
				for subs in trees.subtrees():
					if subs.label()=="NP":
						npnoun = []
						for n in subs.leaves():
							npnoun.append(n[0])
						if svo.subj[0] in npnoun:
							lsubj.append(subs)
						#elif svo.obj[0] in npnoun:
						#	lobj.append(subs)
					elif subs.label() =="PP":
						continue
					elif subs.label() =="VP":
						vpverb = []
						for v in subs.leaves():
							vpverb.append(v[0])
						if svo.verb[0] in vpverb:
							lverb.append(subs)

		for np in lsubj:
			gen = ""
			nn =""
			redundant = []
			Det = None
			for n in np.leaves():
				adjs = []
				if n[1] in ["NN","NNS","NNP","NNPS"]:
					if n[0] not in redundant:
						nn+=n[0]+" "
						redundant.append(n[0])
				elif n[1] in ["DT"]:
					Det = n[0]
				elif n[1] in ["JJR","JJ","JJS"]:
					adjs.append(n[0])
				else:
					if n[0] not in redundant:
						nn+=n[0]+" "
						redundant.append(n[0])
			Nphrase = NounPhrase(nn,Det,adjs)
			for vp in lverb:
				vps = []
				redundant = []
				for v in vp.leaves():
					if v[1] in ["VBD","VBZ","VB", "VBN","VBG","VBP"]:
						if v[0] not in redundant:
							phrase = VerbPhrase(lex.getWordFromVariant(v[0],"VERB"))
							if v[1] in ["VB","VBZ","VBP"]:
								phrase.set_tense("present")
							elif v[1] in ["VBD"]:
								phrase.set_tense("past")
							elif v[1] in ["VBN"]:
								phrase.set_tense("past_participle")
							elif v[1] in ["VBG"]:
								phrase.set_tense("present_participle")
							vps.append(phrase)
							redundant.append(v[0])
#				for op in lobj:
#					nn =""
#					redundant = []
#					for o in op.leaves():
#						adjs = []
#						if n[1] in ["NN","NNS","NNP","NNPS"]:
#							if n[0] not in redundant:
#								nn+=n[0]+" "
#								redundant.append(n[0])
#						elif n[1] in ["DT"]:
#							Det = n[0]
#						elif n[1] in ["JJR","JJ","JJS"]:
#							adjs.append(n[0])
#						else:
#							if n[0] not in redundant:
#								nn+=n[0]+" "
#								redundant.append(n[0])
#						Ophrase = NounPhrase(nn,Det,adjs)
						dis.append((Nphrase,vps))
						gen+= Nphrase.realize()+" "
						for vph in vps:
							if vps.index(vph) == (len(vps)-1):
								vph.add_object(Noun(svo.obj[0]))
								gen+=vph.realize()
							else:
								gen+=vph.realize()
						#gen+=" "+Ophrase.realize()
						print("\n"+gen)
		lsubj=[]
		lobj=[]
		lverb=[]
#	if svo.verb[1] in ["VB","VBZ","VBP"]:
#		nlg.setUp1(svo.subj[0],svo.verb[0],svo.obj[0],"present")
#	elif svo.verb[1] in ["VBD"]:
#		nlg.setUp1(svo.subj[0],svo.verb[0],svo.obj[0],"past")
#	elif svo.verb[1] in ["VBN"]:
#		nlg.setUp1(svo.subj[0],svo.verb[0],svo.obj[0],"past_participle")
#	elif svo.verb[1] in ["VBG"]:
#		nlg.setUp1(svo.subj[0],svo.verb[0],svo.obj[0],"present_participle")


#if svo.verb[0] in subs:

			
class Docs:
	def __init__(self, words,show):
		self.words = words
		self.show = show
