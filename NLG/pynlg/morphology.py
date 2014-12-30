'''
Created on Sep 12, 2011

@author: Nich
'''
vowels = ('a', 'e', 'i','o', 'u') #fuck y
double_vowels = ('ea', 'ee', 'oo', 'ou')


def makeVariants(word):
    variants = []
    return variants

def makeInflections(word):
    inflections = {}
    if word.category == "NOUN":
        #do plural
        inflections["plural"] = noun_plural(word)
        
        
    if word.category == "VERB":
	
        inflections["infinitive"] = verb_inf(word)
        inflections["to-infinitive"] = verb_to_inf(word)
        inflections["present"] = verb_present(word)
        inflections["past"] = verb_past(word)
        inflections["present_participle"] = verb_present_participle(word)
        inflections["past_participle"] = verb_past_participle(word)
        inflections["present_progressive"] = verb_present_progressive(word)
        inflections["past_progressive"] = verb_past_progressive(word)
        inflections["focus"] = verb_focus(word)
    if word.category == "ADJECTIVE":
        inflections["superlative"] = adj_superlative(word)
        inflections["comparative"] = adj_comparative(word)
    if word.category == "MODAL":
        inflections["past"] = verb_past(word)
    return inflections

def verb_focus(word):
	if "focus"  in word.features:
		if word.features["focus"] == "actor":
			print("yay")
		else:
			print("wtf")
	else:
	#base lang iaaaoutput pag wala.
		return word.base
    
def noun_plural(word):
    base = word.base
    feat = word.features
    if "plural" in feat:
        return feat["plural"]
    
    if base[-2:] == "ss" or base[-2:] == "sh" or base[-2:] == "ch" or base[-1:] == "o":
        return base + "es"
    elif base[-1:] == "y" and not "proper" in feat:
        return base[:-1] + "ies"
    else:
        return base + "s"
    

def verb_to_inf(word):
    if "to-infinitive" in word.features:
        return word.features["to-infinitive"]
    else:
        return "to "+word.base
    
def verb_inf(word):
    if "infinitive" in word.features:
        return word.features["infinitive"]
    else:
        return word.base

def verb_present(word):
    if "present" in word.features:
        return word.features["present"]
    else:
        base = word.base
        if base[-2:] == "ss" or base[-2:] == "sh" or base[-2:] == "ch" or base[-1:] == "o":
            return base + "es"
        elif base[-1:] == "y":
            return base[:-1] + "ies"
        else:
            return base + "s"



def verb_past(word):
    if "past" in word.features:
        return word.features["past"]
    else:
        base = word.base
        if base[-1] == "e":
            return base+"d"
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'p', 's', 't', 'z') and not base[-3:-1] in double_vowels and not base[-2:] == "ss":
            return base+base[-1]+"ed"
        if base[-1] == 'y':
            return base[:-1]+"ied"
        else:
            return base+"ed"

def verb_present_participle(word):
    if "presentparticiple" in word.features:
        return word.features["presentparticiple"]
    else:
        base = word.base
        if base[-1] == "e":
            return base[:-1]+"ing"
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 's', 't', 'z') and not base[-3:-1] in double_vowels and not base[-2:] == "ss":
            return base+base[-1]+"ing"
        if base[-1] == 'y':
            return base+"ing"
        else:
            return base+"ing"

def verb_past_participle(word):
    if "pastparticiple" in word.features:
        return word.features["pastparticiple"]
    else:
        base = word.base
        if base[-1] == "e":
            return base[:-1]+"ed"
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 's', 't', 'z') and not base[-3:-1] in double_vowels:
            return base+base[-1]+"ed"
        if base[-1] == 'y':
            return base+"ed"
        else:
            return base+"ed"

def verb_present_progressive(word):
    if "presentprogressive" in word.features:
        return word.features["presentprogressive"]
    else:
        return "is "+verb_present_participle(word)
    
def verb_past_progressive(word):
    if "pastprogressive" in word.features:
        return word.features["pastprogressive"]
    else:
        return "was "+verb_present_participle(word)
        
    
        
        
def adj_comparative(word):
    if "comparative" in word.features:
        return word.features["comparative"]
    else:
        base = word.base
        if base[-1] == 'e':
            return base[:-1]+"er"
        if base[-3:] == "ful":
            return "more "+base
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 's', 't', 'z') and base[-2:] != "ll":
            return base+base[-1]+"er"
        if base[-1] == 'y':
            return base[:-1] + "ier"
        return word.base+"er"
    
def adj_superlative(word):
    if "superlative" in word.features:
        return word.features["superlative"]
    else:
        base = word.base
        if base[-1] == 'e':
            return base[:-1]+"est"
        if base[-3:] == "ful":
            return "most "+base
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 's', 't', 'z') and base[-2:] != "ll":
            return base+base[-1]+"est"
        if base[-1] == 'y':
            return base[:-1] + "iest"
        return word.base+"est"
    

    
    