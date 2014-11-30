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
		getPOS(sent)
		#sentence.append(getWords(sent))
	#appending per sentence[sentences.append(sent) for sent in sents]
	#for appending everything[article.append(sent) for sent in sentences]
	
def getPOS(sent):
        POS = preprocessor.posTagger(sent)
        print(POS)
