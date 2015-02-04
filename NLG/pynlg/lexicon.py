'''
Created on Sep 11, 2011

@author: Nich
'''
import xml.etree.ElementTree
import os.path
from collections import defaultdict

import pynlg.morphology as morph

DEFAULT_PATH = os.path.realpath("C:/Documents and Settings/lenovo/Desktop/SumMe/NLG/default-lexicon.xml")


class Word():
    def __init__(self, base, category, w_id = "E000000", features = None, inflections= None):
        self.base = base
        self.category = category
        self.id = w_id
        self.features = {} if features is None else features
        self.inflections = {} if inflections is None else inflections
    def hasFeature(self, key):
        return key.lower() in self.features  
    def hasInflection(self, key):
        return key.lower() in self.inflections
    def __str__(self):
        return self.base  

class Verb(Word):
    def tense(self, tense):
        return self.inflections[tense]

    
class Adjective(Word):
    def __str__(self):
        return self.base

class Noun(Word):
    def __init__(self, base, w_id = "E000000", features = None, inflections = None):
        super().__init__(base, category = "NOUN", w_id = w_id, features = features, inflections = inflections)
    
    def plural(self):
        return self.plural
    
    def __str__(self):
        if self.hasFeature("proper"):
            return self.base.capitalize()
        return self.base

class Determiner(Word):
    def __str__(self):
        return self.base  

class Modal(Word):
    def __str__(self):
        return self.base


class Lexicon():
    def __init__(self):
        self.words_by_id = {}
        self.words_by_base = defaultdict(list)
        self.words_by_category = defaultdict(list)
        self.words_by_variants = defaultdict(list)
        
         
    def hasWord(self, word, word_cat = None):
        if word in self.words_by_base.keys():
            if word_cat == None:
                return True
            else:
                for value in self.words_by_base[word]:
                    if value.category == word_cat:
                        return True
                return False
        
    def getWordByID(self, w_id):
        if w_id in self.words_by_id:
            return self.words_by_id[w_id]
        else:
            return None
    
    def getWords(self, word, word_cat = None):
        words = self.words_by_base[word]
        if not word_cat is None:
            return [w for w in words if w.category == word_cat]
        else:
            return words
        
    def getWord(self, word, word_cat = None):
        retr_word = self.getWords(word, word_cat)
        if len(retr_word) == 0:
            with open('C:/Documents and Settings/lenovo/Desktop/SumMe/NLG/default-lexicon.xml', 'a') as f:
               f.write('<word>\n')
               f.write('\t<base>'+word+'</base>\n')
               f.write('\t<category>noun</category>\n')
               f.write('</word>\n')
        if len(retr_word) > 1:
            raise Exception("The word '"+word+"' is ambiguous, and could be one of the following categories: "+", ".join([w.category for w in retr_word])+". Specify a category or use 'getWords()' to retrieve a list")        
        return retr_word[0]
        
    def getWordFromVariant(self, variant, word_cat = None):
        return self._getWordFromDict(self.words_by_variants, variant, word_cat)
    
    def _getWordFromDict(self, w_dict, word, word_cat = None):
        words = w_dict[word]
        if word_cat is None:
            if len(words) == 0:
                return None
            if len(words) == 1:
                return words[0]
            else:
                return words
        else:
            for w in words:
                if w.category == word_cat:
                    return w
        return None
    
    def makeVariants(self, word_elem):
        for variant in morph.makeVariants(word_elem):
            self.words_by_variants[variant].append(word_elem)
    
    def makeInflections(self, word_elem):
        inflections = morph.makeInflections(word_elem)
        for key, value in inflections.items():
            #add to variants list so we can search by it
            self.words_by_variants[value].append(word_elem)
            #and add it to the word itself
            word_elem.inflections[key] = value
            #finally, add it as an attribute
            setattr(word_elem, key.lower(), value)
            
    def lookup(self, word, word_cat = None):
        if not self.getWordByID(word) is None:
            return self.getWordByID(word)
        if not len(self.getWords(word, word_cat)) == 0:
            return self.getWord(word, word_cat)
        if not self.getWordFromVariant(word, word_cat) is None:
            return self.getWordFromVariant(word, word_cat)
        
    

class XMLLexicon(Lexicon):
    
    def __init__(self, filename=None):
        Lexicon.__init__(self)
        if filename is None:
            lex_tree = xml.etree.ElementTree.parse(DEFAULT_PATH)
        else:
            lex_tree = xml.etree.ElementTree.parse(filename)
        
        self.buildDicts(lex_tree)
        
    def buildDicts(self, lex_tree):
        lex = lex_tree.getroot()
        for word in lex.findall("word"):
            word_elem = self.makeWordElem(word)
            self.words_by_base[word_elem.base].append(word_elem)
            self.words_by_category[word_elem.category].append(word_elem)
            self.words_by_id[word_elem.id] = word_elem
            self.words_by_variants[word_elem.base].append(word_elem)
            self.makeInflections(word_elem)
        
    def makeWordElem(self, word):
        features = {}
        base = None
        w_id = None
        category = None
        for prop in list(word):
            if prop.tag == "base":
                base = prop.text.lower()
            elif prop.tag == "id":
                w_id = prop.text.upper()
            elif prop.tag == "category":
                category = prop.text.upper()
            else:
                if prop.text is None:
                    features[prop.tag.lower()] = True
                else:
                    features[prop.tag.lower()] = prop.text
                    
        if category == "VERB":
            return Verb(base, category, w_id, features)
        elif category == "ADJECTIVE":
            return Adjective(base, category, w_id, features)
        elif category == "DETERMINER":
            return Determiner(base, category, w_id, features)
        elif category == "NOUN":
            return Noun(base, w_id=w_id, features=features)
        elif category == "MODAL":
            return Modal(base, category, w_id, features)
        else:
            return Word(base, category, w_id, features)
    
    

if __name__ == "__main__":
    lex = XMLLexicon("C:/projects/Python-nlg/res/TestLexicon.xml")
    be = lex.getWord("be")
    print(be.base)
    print(be.id)
    print(be.category)
    print(be.features)
    print(be.inflections)
    
           
    
            
        
        

