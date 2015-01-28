'author pol'
from PreProcessing import preprocessor

#should contain these:
#a list containing:
	#sentence number,
	#sentence itself
	#words(this would be a dict)
		#word
		#POS tag
article =  [] #is this shit even needed

global sentences
sentences = [] # 1sentence number, 2the sentence, 3the tuples of words 0 = word 1 = pos 
			#and their corresponding POS tags, and the 4language id
			#5when chunkSents is invoked chunks of the sentence is appended
			#6when getTriple() is invoked svos of the sentence is appended
			#7when getTriple() is invoked frequencies of the sentences is also appended


def chunkSents():
	global sentences
	for sents in sentences:
		if sents[3] =="en":
			sents.append(preprocessor.enChunk(sents[2]))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			sents.append(preprocessor.tlChunk(sents[2]))
			sentences[sents[0]] = sents
	return sentences

def clearMem():
	global sentences 
	sentences = []
	return sentences

def getTriple():
	global sentences
	for sents in sentences:
		if sents[3] =="en":
			sents.extend(preprocessor.getSVO(sents[4],True))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			sents.extend(preprocessor.getSVO(sents[4],False))
			sentences[sents[0]] = sents
	return sentences



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
		
	return sentences
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
	compare = sentences
	nDocs = []
	ideff = []
	for sents in sentences:
		for terms in sents[7]:
			for com in compare:
				for chk in com[7]:
					if terms[0] in chk[0]:
						for n in nDocs:
							if terms[0]==n[0]:
								nDocs.insert(nDocs.index(n),(n[0],n[1]+1))
							else:
								nDocs.append((terms,1))
						break;
					else: continue;
	for n in nDocs:
		idf = math.log10(len(sentences)/n[1])
		print(idf)
		ideff.append((n[0],idf))
