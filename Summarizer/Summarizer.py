'author pol'
from PreProcessing import preprocessor
import math
#english NLG
from NLG.pynlg.realizer import Clause, ImperativeClause, PrepositionalPhrase, NounPhrase, SubjectPredicate, PredicateSubject, VerbPhrase
from NLG.pynlg.lexicon import Word, XMLLexicon, Noun, Determiner, Adjective,Verb
#english NLG
#Filipino NLG
from NLG.pynlg.fil_realizer import ImperativeClause as FImp, PrepositionalPhrase as FPrep, NounPhrase as FNP, SubjectPredicate as FSP, PredicateSubject as FPS, VerbPhrase as FVP
from NLG.pynlg.fil_lexicon import Word as Fword, XMLLexicon as Flex, Noun as Fnoun, Determiner as Fd, Adjective as Fad,Verb as Fverb
#Filipino NLG

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
global sumTh
global ActualSum

sumTh = 0
sentenceTh = 0
ActualSum = []


sentences = []
			# 0 sentence number, 
			#1 the sentence, 5
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
			if not preprocessor.enChunk(sents[2]):
				sents.append([])
			else:
				sents.append(preprocessor.enChunk(sents[2]))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			if not preprocessor.tlChunk(sents[2]):
				sents.append([])
			else:
				sents.append(preprocessor.tlChunk(sents[2]))
			sentences[sents[0]] = sents
		else:
			if not preprocessor.enChunk(sents[2]):
				sents.append([])
			else:
				sents.append(preprocessor.enChunk(sents[2]))
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
		for word in sent[2]:
			if word[1] in ["NNT","NNST","NNPT","NNPST","VBDT","VBZT","VBT", "VBNT","VBGT","VBPT",
							"JJT","JJRT","JJST","PRPT","PRP$T"]:
				sentScore = sentScore + 0.75
			elif word[1] in ["RBT""RBRT","RBST","RPT",".","INT"]:
				sentScore  = sentScore + 0.25
			else:
				sentScore = sentScore + 0.50
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
	global CandidSVO 
	global terms
	global sentenceTh
	global sumTh
	global ActualSum

	ActualSum = []
	sumTh = 0
	sentenceTh = 0
	terms = []
	CandidSVO = []
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
		else:
			sents.append(preprocessor.getSVO(sents[0],sents[2],True))
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
		else:
			sents.append(preprocessor.getFreqs(sents[4],True))
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
		try:
			for tup in sents[6]:
				if tup[0][0] not in nWords:
					nWords.append(tup[0][0])
		except:
			continue
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
	#print("got here entrance")
	for sents in sentences:
	#	print("got here first loop")
		for svo in sents[5]:
	#		print("got here second loop")
	#		print(sentences[svo.sNum][7])
			if svo.sNum in getAcSents():
	#			print("got here")
				for term in  terms[start:end]:
					if svo.subj[0] == term[0] and svo.obj[0]==term[0]:
						continue
					elif svo.subj[0]==term[0]:
	#					print("got appended")
						CandidSVO.append(svo)
					elif svo.obj[0] == term[0]:
	#					print("got appended")
						CandidSVO.append(svo)
	clnCandSubjs(start,end)

def clnCandSubjs(start,end):

	global CandidSVO
	global terms
	dltMe = False
	for svo in CandidSVO:
		for term in terms[start:end]:
			if(svo.subj[0]==term[0]):
				dltMe = False
				continue
			else:
				dltMe = True
		if dltMe:
	#		print("they're gonna remove me D:"+ " "+svo.subj[0] + " " +svo.obj[0] + " "+svo.verb[0])
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
	global summary
	global opha
	opha = []
	summary = []
	dis = []
	lex = XMLLexicon()
	flex = Flex()
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
						elif svo.obj[0] in npnoun:
							lobj.append(subs)
					elif subs.label() =="PP":
						continue
					elif subs.label() =="VP":
						vpverb = []
						for v in subs.leaves():
							vpverb.append(v[0])
						if svo.verb[0] in vpverb:
							lverb.append(subs)
#reminder try getting all them pos tags
#and try getting the object part too
		if sentences[svo.sNum][3] == "en" or  sentences[svo.sNum][3] not in ["tl"]:
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
				vebs = []
				for vp in lverb:
					vps = []
					redundant = []
					for v in vp.leaves():
						if v[1] in ["VBD","VBZ","VB", "VBN","VBG","VBP","MD"]:
							if v[0] not in redundant:
								if v[1] not in ["MD"]:
									phrase = VerbPhrase(lex.getWordFromVariant(v[0],"VERB"))
								elif v[1] in ["MD"]:
									phrase = VerbPhrase(lex.getWordFromVariant(v[0],"MODAL"))
								if phrase.verb != None:
									if v[1] in ["VB"]:
										phrase.set_tense("present")
									elif v[1] in ["VBZ","VBP"]:
										phrase.set_tense("infinitive")
									elif v[1] in ["VBD"]:
										phrase.set_tense("past")
									elif v[1] in ["VBN"]:
										phrase.set_tense("past_participle")
									elif v[1] in ["VBG"]:
										phrase.set_tense("present_participle")
									elif v[1] in ["MD"]:
										if lex.getWordFromVariant(v[0],"MODAL").base == v[0]:
											phrase.set_tense("present")
										else:
											phrase.set_tense("past")
									vps.append(phrase)
								redundant.append(v[0])
					vebs.append(vps)
				
				for op in lobj:
					ops = []
					nn =""
					redundant = []
					for o in op.leaves():
						adjs = []
						print(o)
						if o[1] in ["NN","NNS","NNP","NNPS"]:
							if o[0] not in redundant:
								nn+=o[0]+" "
								redundant.append(n[0])
						elif o[1] in ["DT"]:
							Det = o[0]
						elif o[1] in ["JJR","JJ","JJS"]:
							adjs.append(o[0])
							nn+=o[0]+" "
						else:
							if o[0] not in redundant:
								nn+=o[0]+" "
								redundant.append(o[0])
						Ophrase = NounPhrase(nn,Det,adjs)
						ops.append(Ophrase)
					opha.append([ops,svo.sNum])
					#printing function
					# not sedis.append((Nphrase,vps)) not used
					gen = ""
					for vps in vebs:
						gen+= Nphrase.realize()+" "
						for vph in vps:
							if vph.verb != None:
								if vps.index(vph) == (len(vps)-1):
									for op in ops:
										print(op.realize())
										vph.add_object(op)
									gen+=vph.realize()+" "
								else:
									gen+=vph.realize()+" "
						summary.append([svo.sNum,gen])
						print(gen)
		else:
			for np in lsubj:
				gen = ""
				nn =""
				redundant = []
				Det = None
				for n in np.leaves():
					adjs = []
					if n[1] in ["NNT","NNST","NNPT","NNPST"]:
						if n[0] not in redundant:
							nn+=n[0]+" "
							redundant.append(n[0])
					elif n[1] in ["DTT"]:
						Det = n[0]
					elif n[1] in ["JJRT","JJT","JJST"]:
						adjs.append(n[0])
					else:
						if n[0] not in redundant:
							nn+=n[0]+" "
							redundant.append(n[0])
				Nphrase = FNP(nn,Det,adjs)
				vebs = []
				for vp in lverb:
					vps = []
					redundant = []
					for v in vp.leaves():
						if v[1] in ["VBDT","VBZT","VBT", "VBNT","VBGT","VBPT"]:
							if v[0] not in redundant:
								phrase = FVP(flex.getWordFromVariant(v[0],"VERB"))
								
								if v[1] in ["VBT"]:
									phrase.set_tense("present")
								elif v[1] in ["VBZT","VBPT"]:
									phrase.set_tense("infinitive")
								elif v[1] in ["VBDT"]:
									phrase.set_tense("past")
								elif v[1] in ["VBNT"]:
									phrase.set_tense("past_participle")
								elif v[1] in ["VBGT"]:
									phrase.set_tense("present_participle")
								vps.append(phrase)
								redundant.append(v[0])
					vebs.append(vps)
				
				for op in lobj:
					ops = []
					nn =""
					redundant = []
					for o in op.leaves():
						adjs = []
						print(o)
						if o[1] in ["NNT","NNST","NNPT","NNPST"]:
							if o[0] not in redundant:
								nn+=o[0]+" "
								redundant.append(n[0])
						elif o[1] in ["DTT"]:
							Det = o[0]
						elif o[1] in ["JJRT","JJT","JJST"]:
							adjs.append(o[0])
							nn+=o[0]+" "
						else:
							if o[0] not in redundant:
								nn+=o[0]+" "
								redundant.append(o[0])
						Ophrase = FNP(nn,Det,adjs)
						ops.append(Ophrase)
					opha.append([ops,svo.sNum])
					#printing function
					# not sedis.append((Nphrase,vps)) not used
					gen = ""
					for vps in vebs:
						gen+= Nphrase.realize()+" "
						for vph in vps:
							if vph.verb != None:
								if vps.index(vph) == (len(vps)-1):
									for op in ops:
										print(op.realize())
										vph.add_object(op)
									gen+=vph.realize()+" "
								else:
									gen+=vph.realize()+" "
						summary.append([svo.sNum,gen])
						print(gen)

				#printing function
		
							#gen+=" "+Ophrase.realize()
						
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

def gvActSum():

	global summary
	global ActualSum

	senNum = []
	for sent in summary:
		if sent[0] in senNum:
			continue
		else:
			senNum.append(sent[0])
	for rapi in senNum:
		if getIdealSent(rapi) != ".":
			ActualSum.append(getIdealSent(rapi))
	for test in ActualSum:
		print(test)

#def gvActSums():
#	global summary
#	global sentences
#	global sumTh
#	global ActualStuff
#	process = []
#	ActualStuff = []
#	senNum = []
#	lsidea = []
#	senens = []
#	for sent in summary:
#		if sent[0] in senNum:
#			continue
#		else:
#			senNum.append(sent[0])#

#	for num in sentNum:
#		for sent in summary:
#			if num == sent[0]:
#				process.append(sent)
#		for sents in process:
#			if sentences[sents[0]][3] =="en":
#				sents.append(getSumScore(True,sents[1]))
#			else:
#				sents.append(getSumScore(False,sents[1]))
#		getSumTh(sent)
#		for sents in process:
#			if sents[2] >= sumTh:
#				if sents[1] not in lsidea:
#					lsidea.append(sents[1])
#					senens.append(sents)
#			ActualStuff.append(senens)
#	for d in senens:
#		print("Summary:\n")
#		for s in d:







def getIdealSent(num):
	global summary
	global sentences
	global sumTh
	sent = []
	sent2 = []
	ideal = ""
	lsidea = []
	for sents in summary:
		if num == sents[0]:
			sent.append(sents)
	for sents in sent:
		if sentences[sents[0]][3] =="en":
			sents.append(getSumScore(True,sents[1]))
		elif sentences[sents[0]][3] =="tl":
			sents.append(getSumScore(False,sents[1]))
	getSumTh(sent)
	for sents in sent:
		if sents[2] >= sumTh:
			if sents[1] not in lsidea:
				lsidea.append(sents)
				#print(sents[2])
	ideal = None
	for ideas in lsidea:
		if ideal ==None:
			ideal = ideas
		elif ideal[2] < ideas[2]:
			ideal = ideas
		elif ideal[2] == ideas[2]:
			if sentences[ideal[0]][3] =="en":
				if len(getPOS(ideal[1])) < len(getPOS(ideas[1])):
					ideal = ideas
			elif sentences[ideal[0]][3] =="tl":
					print("roadblock bitches")
#				sents.append(getSumScore(False,sents[1]))

	if ideal == None:
		return "."
	else:
		return ideal[1] + "."




def getSumFreq():
	pass
def getSumIDF():
	pass
def getSumTh(lst):
	global sumTh
	for sent in lst:
		sumTh = sumTh + sent[2]
	sumTh = sumTh/len(lst)
	return sumTh
def getSumScore(isEnglish, sent):
	sentScore = 0
	lent = 0
	if isEnglish:
		lent = len(getPOS(sent))

		for word in getPOS(sent):
			if word[1] in ["NN","NNS","NNP","NNPS","VBD","VBZ","VB", "VBN","VBG","VBP","MD",
							"JJ","JJR","JJS"]:
				sentScore = sentScore + 0.75
			elif word[1] in ["RBR","RBS","RP","."]:
				sentScore  = sentScore + 0.25
			else:
				sentScore = sentScore + 0.50
	else:
		lent = preprocessor.tokenizer(sent)
		for word in getFilPOS(preprocessor.tokenizer(sent)):
			if word[1] in ["NNT","NNST","NNPT","NNPST","VBDT","VBZT","VBT", "VBNT","VBGT","VBPT",
							"JJT","JJRT","JJST"]:
				sentScore = sentScore + 0.75
			elif word[1] in ["RBRT","RBST","RPT","."]:
				sentScore  = sentScore + 0.25
			else:
				sentScore = sentScore + 0.50
	sentScore = sentScore/lent#len(sent[2])
	return sentScore



#if svo.verb[0] in subs:
def gvSumme():
	for sent in sentences:
		senens= ""
		for item in summary:
			if item[0] == sent[0]:
				senens+=item[1]	
		print(senens+".")
			
class Docs:
	
	def __init__(self, words,show):
		self.words = words
		self.show = show
