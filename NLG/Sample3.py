from pynlg.realizer import Clause, ImperativeClause, PrepositionalPhrase, NounPhrase, SubjectPredicate, PredicateSubject, VerbPhrase
from pynlg.lexicon import Word, XMLLexicon, Noun, Determiner, Adjective


def setUp1(noun, verb, obj):


	lex = XMLLexicon()  
	#the girl is playing the guitar        
	s1 = Clause()

	np_sub = s1.add_subject(lex.getWord("girl"))
	np_sub = s1.add_subject(lex.getWord(noun,"NOUN"))
	np_sub.add_determiner(lex.getWord("the"))
	vp_play = s1.add_verb(lex.getWord(verb, "VERB"))

	np_guitar = vp_play.add_object(lex.getWord(obj))
	np_guitar.add_determiner(lex.getWord("the"))

	s1.set_verb_tense("present_progressive")

	print(s1.realize())

