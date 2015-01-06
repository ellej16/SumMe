from pynlg.realizer import Clause, ImperativeClause, PrepositionalPhrase, NounPhrase, SubjectPredicate, PredicateSubject, VerbPhrase
from pynlg.lexicon import Word, XMLLexicon, Noun, Determiner, Adjective

class Sample():

        def setUp1():

                lex = XMLLexicon()

                #the girl is playing the guitar        
                s1 = SubjectPredicate()
                
                np_sub = s1.add_subject(lex.getWord("lalaki"))
                np_sub.add_determiner(lex.getWord("ang"))
                vp_bumayo = s1.add_verb(lex.getWord("bumayo", "VERB"))
        
                np_aso = vp_play.add_object(lex.getWord("aso"))
 
                np_ng_aso = PrepositionalPhrase(lex.getWord("ng", "PREPOSITION"), [np_aso])

                print(s1.realize())

Sample.setUp1()