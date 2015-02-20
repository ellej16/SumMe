import nltk




enGrammar  = nltk.data.load('grammars/test.cfg')
enRdParser = nltk.RecursiveDescentParser(enGrammar)
enSRParser = nltk.ShiftReduceParser(enGrammar)
#enLCParser = nltk

#filGrammar = nltk.data.load("")
#filRdParser = nltk.RecursiveDescentParser(filGrammar)
#filSRParser = nltk.ShiftReduceParser(filGrammar)

def rdParseEng(sents):
	return enRdParser.parse(sents)


def srParseEng(sents):
	return enSRParser.parse(sents)

def lcParseEng(sents):
	return enLCParser.parse(sents)

#def srParseFil(sents):
#	return filSRParser.parse(sents)
