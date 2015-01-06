#from pynlg.realizer import Clause, ImperativeClause, PrepositionalPhrase, NounPhrase, SubjectPredicate, PredicateSubject, VerbPhrase
from pynlg.lexicon import Word, XMLLexicon, Noun, Determiner, Adjective
import pynlg.fil_lexicon as filex
from pynlg.fil_realizer import ImperativeClause, PrepositionalPhrase, NounPhrase, SubjectPredicate, PredicateSubject, VerbPhrase


class Sample():

        def setUp1():

                lex = XMLLexicon()

                #the girl is playing the guitar        
                s1 = Clause()
                
                np_sub = s1.add_subject(lex.getWord("girl"))
                np_sub.add_determiner(lex.getWord("the"))
                vp_play = s1.add_verb(lex.getWord("play", "VERB"))
        
                np_guitar = vp_play.add_object(lex.getWord("guitar"))
                np_guitar.add_determiner(lex.getWord("the"))
        
                s1.set_verb_tense("present_progressive")

                print(s1.realize())


        def setUp2():

                lex = XMLLexicon()

                #my dog's my best friend        
                s1 = Clause()
                a = "my best friend"

                s1 = NounPhrase(a)
                np_own = s1.add_owner(lex.getWord("dog"))
                np_own.add_determiner(lex.getWord("my"))
                
                print(s1.realize())


        def setUp3():

                lex = XMLLexicon()

                #put the beans in the old machine
                s1 = ImperativeClause()

                vp_put = s1.add_verb(lex.getWord("put", "VERB"))
                np_the_machine = NounPhrase(lex.getWord("machine", "NOUN"), determiner=lex.getWord("the"), adjectives=[lex.getWord("old")])
                pp_in_the_machine = PrepositionalPhrase(lex.getWord("in", "PREPOSITION"), [np_the_machine])
        
                vp_put.add_prepositional_phrase(pp_in_the_machine)
        
        
                np_the_beans = s1.add_subject(lex.getWord("bean"))
                np_the_beans.add_determiner(lex.getWord("the"))
                np_the_beans.set_number("plural")

                print(s1.realize())

        def setUp4():

                lex = XMLLexicon()
        
                #the woman kissed the man behind the curtain
                s1 = Clause()

                np_woman = s1.add_subject(lex.getWord("woman"))
                np_woman.add_determiner(lex.getWord("the"))
                                
                vp_kiss = s1.add_verb(lex.getWord("kiss", "VERB"))
                np_the_curtain = NounPhrase(lex.getWord("curtain", "NOUN"), determiner=lex.getWord("the"))
                pp_the_curtain = PrepositionalPhrase(lex.getWord("behind", "PREPOSITION"), [np_the_curtain])
        
                vp_kiss.add_prepositional_phrase(pp_the_curtain)
        
                np_man = vp_kiss.add_object(lex.getWord("man"))
                np_man.add_determiner(lex.getWord("the"))
                
        
                s1.set_verb_tense("past")

                print(s1.realize())

        def setUp5():
		
                lex = filex.XMLLexicon()

                #Nagluluto ang Kusinero
                s1 = PredicateSubject()

                #vp_nagluluto = s1.add_verb(lex.getWord("luto", "VERB"))
                #np_ang_kusinero = NounPhrase(lex.getWord("kusinero", "NOUN"))
                #pp_ng_kusinero = PrepositionalPhrase(lex.getWord("ng", "PREPOSITION"), [np_ang_kusinero])
                s1.add_subject(lex.getWord("baba","NOUN"))
                s1.add_verb(lex.getWord("luto","VERB"))
                #vp_nagluluto.add_prepositional_phrase(pp_ng_kusinero)
        
        
                #np_ang_babae = s1.add_subject(lex.getWord("babae","NOUN"))
                #np_ang_babae.add_determiner(lex.getWord("ang"))


                print(s1.realize())
#Sample.setUp1()
#Sample.setUp2()
#Sample.setUp3()
#Sample.setUp4()
Sample.setUp5()
