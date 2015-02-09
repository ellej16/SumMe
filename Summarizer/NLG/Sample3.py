from NLG.pynlg.realizer import Clause, ImperativeClause, PrepositionalPhrase, NounPhrase, SubjectPredicate, PredicateSubject, VerbPhrase
from NLG.pynlg.lexicon import Word, XMLLexicon, Noun, Determiner, Adjective,Verb


def setUp1(noun, verb, obj, tense):
	lex = XMLLexicon()  
	#the girl is playing the guitar        
	s1 = Clause()
	try:
		np_sub = s1.add_subject(lex.getWord(noun,"NOUN"))
		np_sub.add_determiner(lex.getWord("the")) vp_play = s1.add_verb(lex.getWordFromVariant(verb, "VERB"))

		#if none
		np_guitar = vp_play.add_object(lex.getWord(obj,"NOUN"))
		np_guitar.add_determiner(lex.getWord("the"))
		s1.set_verb_tense(tense)
		print(s1.realize())

	except :
		try:
			np_sub = s1.add_subject(Noun(noun))
			np_sub.add_determiner(lex.getWord("the"))
			vp_play = s1.add_verb(lex.getWordFromVariant(verb,"VERB"))

			#if none
			np_guitar = vp_play.add_object(Noun(obj))
			np_guitar.add_determiner(lex.getWord("the"))
			s1.set_verb_tense(tense)
			print(s1.realize())
		except Exception as inst:
			print(type(inst))
			print(inst.args)
			pass
def CreateSent(NP, VP, OBJ):
	#args: noun = NP chunk
	# 
	lex = XMLLexicon()  
	#the girl is playing the guitar        
	s1 = Clause()
	try:
		np_sub = s1.add_subject(lex.getWord(noun,"NOUN"))
		np_sub.add_determiner(lex.getWord("the"))
		vp_play = s1.add_verb(lex.getWordFromVariant(verb, "VERB"))

		#if none
		np_guitar = vp_play.add_object(lex.getWord(obj,"NOUN"))
		np_guitar.add_determiner(lex.getWord("the"))
		s1.set_verb_tense(tense)
		print(s1.realize())

	except :
		try:
			np_sub = s1.add_subject(Noun(noun))
			np_sub.add_determiner(lex.getWord("the"))
			vp_play = s1.add_verb(lex.getWordFromVariant(verb,"VERB"))

			#if none
			np_guitar = vp_play.add_object(Noun(obj))
			np_guitar.add_determiner(lex.getWord("the"))
			s1.set_verb_tense(tense)
			print(s1.realize())
		except Exception as inst:
			print(type(inst))
			print(inst.args)
			pass