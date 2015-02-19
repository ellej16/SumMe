'''
Created on 2013-03-06

@author: Nich
'''
import unittest
from NLG.pynlg.realizer import Clause, ImperativeClause, PrepositionalPhrase, NounPhrase
from NLG.pynlg.lexicon import Word, XMLLexicon, Noun

class TestRealizer(unittest.TestCase):


    def setUp(self):
        lex = XMLLexicon()
        
        #the woman kissed the man behind the curtain
        self.s1 = Clause()
        np_woman = self.s1.add_subject(lex.getWord("woman"))
        np_woman.add_determiner(lex.getWord("the"))
        vp_kiss = self.s1.add_verb(lex.getWord("kiss", "VERB"))
        
        np_man = vp_kiss.add_object(lex.getWord("man"))
        np_man.add_determiner(lex.getWord("the"))
        
        self.s1.set_verb_tense("past")
        
        
        #there is the dog on the rock
        
        #the man gives the woman John's flower
        self.s2 = Clause()
        np_man = self.s2.add_subject(lex.getWord("man"))
        np_man.add_determiner(lex.getWord("the"))
        
        vp_give = self.s2.add_verb(lex.getWord("give"))
        vp_give.set_tense("present")
        
        np_flower = vp_give.add_object(lex.getWord("flower"))
        np_flower.add_owner(lex.getWord("john"))
        
        np_woman = vp_give.add_indirect_object(lex.getWord("woman"))
        np_woman.add_determiner(lex.getWord("the"))
        
        #Test imperative
        
        #Make the coffee
        
        self.s3 = ImperativeClause()
        vp_make = self.s3.add_verb(lex.getWord("make", "VERB"))
        np_the_coffee = self.s3.add_subject(lex.getWord("coffee"))
        np_the_coffee.add_determiner(lex.getWord("the"))
        
        #Put the beans in the machine
        self.s4 = ImperativeClause()
        vp_put = self.s4.add_verb(lex.getWord("put", "VERB"))
        np_the_machine = NounPhrase(lex.getWord("machine", "NOUN"), determiner=lex.getWord("the"))
        pp_in_the_machine = PrepositionalPhrase(lex.getWord("in", "PREPOSITION"), [np_the_machine])
        
        vp_put.add_prepositional_phrase(pp_in_the_machine)
        
        
        np_the_beans = self.s4.add_subject(lex.getWord("bean"))
        np_the_beans.add_determiner(lex.getWord("the"))
        np_the_beans.set_number("plural")
        
        
        
        

    def tearDown(self):
        pass


    def testBasic(self):
        self.assertEqual("the woman kissed the man", self.s1.realize())
        self.assertEqual("the man gives the woman John's flower", self.s2.realize())
        
        
    def testImperative(self):
        self.assertEqual("make the coffee", self.s3.realize())
        self.assertEqual("put the beans in the machine", self.s4.realize())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()