'author pol'
from PreProcessing import preprocessor

#should contain these:
#a list containing:
	#sentence number,
	#sentence itself
	#words(this would be a dict)
		#word
		#POS tag
article =  []
sentences = [] # sentence number, the sentence, the dictionary of words
def getSentences(str):
	
	sents  = preprocessor.sentence_tokenizer(str)
	sentNum = 0
	sentence = [] 
	for sent in sents:
		sentence.append(sentNum)
		sentence.append(sent)
		ID = preprocessor.LangDetect(sent)
		if ID == "en":
			sentence.append(getPOS(sent))
			print(ID+ " Huehue Bitches")
		elif ID =="tl":
			print(ID+" yay")
		else :
			print(ID + " wut")
		sentNum+=1
		sentences.append(sentence)
		sentence = []
	article.append(sentences)
	#article = [] #clears the article altogether
	for sent in article:
		print(sent)
		print("\n")
	
def getPOS(sent):

	words = []
	POS = preprocessor.posTagger(sent)
	for item in POS:
		word = (item[0],item[1])
		words.append(word)
	return words
