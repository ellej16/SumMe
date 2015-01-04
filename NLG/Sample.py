from pynlg.realizer import Clause, ImperativeClause, PrepositionalPhrase, NounPhrase
from pynlg.lexicon import Word, XMLLexicon, Noun




def setUp():
<<<<<<< HEAD
        lex = XMLLexicon()
        
        #the woman kissed the man behind the curtain
        s1 = Clause()
        np_woman = s1.add_subject(lex.getWord("woman"))
        np_woman.add_determiner(lex.getWord("the"))
        vp_kiss = s1.add_verb(lex.getWord("kiss", "VERB"))
		np_the_curtain = NounPhrase(lex.getWord("curtain", "NOUN"), determiner=lex.getWord("the"))
		pp_the_curtain = PrepositionalPhrase(lex.getWord("behind", "PREPOSITION"), [np_the_curtain])
        
        np_man = vp_kiss.add_object(lex.getWord("man"))
        np_man.add_determiner(lex.getWord("the"))
        
        s1.set_verb_tense("past")       
        print(s1.realize())
=======
	lex = XMLLexicon()    
	#the woman kissed the man behind the curtain
	s1 = Clause()
	np_woman = s1.add_subject(lex.getWord("woman"))
	np_woman.add_determiner(lex.getWord("the"))
	vp_kiss = s1.add_verb(lex.getWord("abandon", "VERB"))
	np_the_curtain = NounPhrase(lex.getWord("curtain", "NOUN"), determiner=lex.getWord("the"))
	pp_the_curtain = PrepositionalPhrase(lex.getWord("behind", "PREPOSITION"), [np_the_curtain])    
	vp_kiss.add_prepositional_phrase(pp_the_curtain)
	np_man = vp_kiss.add_object(lex.getWord("man"))
	np_man.add_determiner(lex.getWord("the"))    
	s1.set_verb_tense("past")
	print(s1.realize())
>>>>>>> 5a9d9c55583b036fb12d9bf6522af720b36dd6aa

