vowels = ('a', 'e', 'i','o', 'u')
consonants = ('b', 'k', 'd', 'g', 'h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'y')


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
#        inflections["present_participle"] = verb_present_participle(word)
#        inflections["past_participle"] = verb_past_participle(word)
#        inflections["present_progressive"] = verb_present_progressive(word)
#        inflections["past_progressive"] = verb_past_progressive(word)
        inflections["focus"] = verb_focus(word)
        inflections["future"] = verb_future(word)
    if word.category == "ADJECTIVE":
        inflections["superlative"] = adj_superlative(word)
        inflections["comparative"] = adj_comparative(word)
    if word.category == "MODAL":
        inflections["past"] = verb_past(word)
    return inflections

    
def noun_plural(word):
    if "plural" in word.features:
        return word.features["plural"]
    else:
        return "mga" + " " + word.base
        
def verb_focus(word):
    if "focus" in word.features:
        return word.features["focus"]
            
def verb_to_inf(word):
    if "to-infinitive" in word.features:
        return word.features["to-infinitive"]
    
def verb_inf(word):
    if "focus" in word.features:
        base = word.base
        focus = word.features["focus"]

        if focus == "actin":
            if base[0] in vowels:
                return "um" + base
            elif base[0] in consonants:
                return base[0] + "um" + base[1:]
            else:
                return base
            
        elif focus == "actout":
            if base[0] == 't':
                return "ma" + base
            elif base[0] in vowels or ('b', 'k', 'd', 'g', 'h', 'l', 'm', 'n', 'p', 'r', 's', 'w', 'y'):
                return "mag-" + base
            else:
                return base
            
        elif focus == "object":
            if base[-1] in vowels:
                if base[-1] == 'o':
                    return base[:-1] + "u" + "in"
                elif base[-1] in ('a','i'):
                    return base + "in"
                else:
                    return base + "hin"
                
            elif base[-1] in consonants:
                if base[-2] == 'o':
                    return base[:-2] + "u" + base[-1] + "in"
                else:
                    return base + "in"
                
            elif base[-1] in vowels:
                if base[-2] in consonants and base[-1] == 'o':
                    return base[:-1] + "u" + "in"
            else:
                return base
        else:
            return base


def verb_present(word):
    if "focus" in word.features:
        base = word.base
        focus = word.features["focus"]
        x = ""
        y = ""
    
        if focus == "actin": #ipag- verbs & -um- verbs
            if base[:4] == "ipag" and base[4] != '-':
                return base[:2] + "in" + base[2:4] + base[4:6] + base[4:]
            elif base[:4] == "ipag" and base[4] == '-':
                return base[:2] + "in" + base[2:5] + base[5] + base[5:]
            
            if base[0] in consonants and base[:2] != "ng" and base[1:3] == "um":
                x = base[0] + base[3:]
                return base[:4] + x
            elif base[0] in consonants and base[:2] == "ng" and base[2:4] == "um":
                x = base[:2] + base[4:]
                return base[:5] + x
            elif base[0] in vowels and base[:2] == "um":
                return base[:2] + base[2] + base[2:]
            else:
                return base
        
        elif focus == "actout": #-an verbs & mag-
            if base[-2:] == "an" and base[:2] != "ng" and base[:4] != "mag-":
                if base[0] in consonants:
                    x = base[:2] + base
                    
                    if x[0] in ('l', 'r', 'w', 'y'):
                        return "ni" + x
                    else:
                        return x[:1] + "in" + x[1:]
                else:
                    x = base[0] + base
                    return "in" + x
                
            if base[-2:] == "an" and base[:2] == "ng" and base[:4] != "mag-":
                return base[:2] + "in" + base[2] + base                                

            if base[:4] == "mag-":
                if base[4] in consonants:
                    x = "n" + base[1:]
                    return x[:4] + x[4:6] + x[4:]
                else:
                    x = "n" + base[1:]
                    return x[:4] + x[4] + x[4:]

            if base[:4] == "mang":
                x = "n" + base[1:]
                return x[:4] + x[4:6] +x[4:]

            
        elif focus == "object":
            if base[-2:] == "in" and base[:2] != "ng" and base[:2] != "ma": #-in verbs
                x = base[:2] + base[:-2]
                
                if x[-2] == 'u' and x[-1] == 'h':
                    return base[:1] + "in" + base[1:-4] + "o"

                if x[-2] == 'u' and x[-1] in ('b', 'k', 'd', 'g', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'y'):
                   if x[2:7] == "papag" and x[2:8] != "papag-":
                       return x[2] + "in" + x[3:-2] + "o" + x[-1]
                   if x[:4] == "papa":
                       y = x[:-2] + "o" + x[-1]
                       return y[:1] + "in" + y[3:]
                   else:
                       y = x[:-2] + "o" + x[-1]
                       return y[:1] + "in" + y[1:]
                
                if x[-1] in vowels and x[-1] == 'u':
                    if x[2:7] == "papag" and x[2:8] != "papag-" and x[7:9] == "ka":
                        return x[2] + "in" + x[3:-1] + "o"
                    else:
                        y = x[:-1] + "o"
                        if y[0] in ('l', 'r'):
                            return "ni" + y
                        else:
                            return y[:1] + "in" + y[1:]
                    
                if x[-1] == 'h' and x[-2] in consonants:
                    y = x[:-1] + "i"
                    return y[:1] + "in" + y[1:]

                if x[:4] == "papa":
                    return x[:1] + "in" + x[3:]

                if x[2:7] == "papag" and x[2:8] != "papag-" and x[-1] != 'h':
                    return x[:1] + "in" + x[3:]
 
                if x[-1] == 'h' and x[-2] in ('a','e','i','o') and x[0] in consonants:
                    if x[2:8] == "papag-":
                        return base[:1] + "in" + base[1:-3]
                    elif x[2:7] == "papag" and x[2:8] != "papag-":
                        return base[:1] + "in" + base[1:-3]
                    else:
                        y = x[:-1]
                        return y[:1] + "in" + y[1:]

                if x[-1] == 'h' and x[-2] in ('a','e','i','o') and x[0] in vowels:
                    y = base[:-3]
                    return "in" + y[0] + y

                if x[-1] == 'r':
                    y = x[:-1] + "d"
                    if y[2:6] == "papa":
                        return y[:1] + "in" + y[3:]
                    else:
                        return y[:1] + "in" + y[1:]
                    
                if x[0] in ('l', 'r'):
                        return "ni" + x
                else:
                        return x[:1] + "in" + x[1:]

            if base[-2:] == "in" and base[:2] == "ng" and base[:2] != "ma":
                return base[:2] + base[5:] + base[2] + base[:5]
                    
            if base[0] == "i": #i- verbs
                if base[1] in vowels: 
                    x = base[0] + base[1:2] + base[1:]
                    return x[:1] + "ni" + x[1:]
                elif base[1] in ('l','r'):
                    x = base[0] + base[1:3] + base[1:]
                    return x[:1] + "ni" + x[1:]
                else:
                    x = base[0] + base[1:3] + base[1:]
                    return x[:2] + "in" + x[2:]

            if base[-2:] == "an" and base[:2] != "ma": #-an verbs
                if base[0] == 'l':
                    x = base[:2] + base
                    return "ni" + x
                elif base[0] in vowels:
                    return "in" + base[0] + base
                else:
                    x = base[:2] + base
                    return x[:1] + "in" + x[1:]
                
            if base[:2] == "ma": #ma- verbs
                if base[2] in consonants and base[2:4] != "ng":
                    x = "n" + base[1:]
                    return x[:2] + x[2:4] + x[2:]
                elif base[2] in consonants and base[2:4] == "ng":
                    x = "n" + base[1:]
                    return x[:2] + x[2:5] + x[2:]
                else:
                    x = "n" + base[1:]
                    return x[:2] + x[2] + x[2:]            
        else:
            return "TANGINA THIS!"                

def verb_past(word):
    if "focus" in word.features:
        base = word.base
        focus = word.features["focus"]
        x = ""
        y = ""
    
        if focus == "actin": #ipag- verbs & -um- verbs
            if base[:4] == "ipag" and base[4] != '-':
                return base[:2] + "in" + base[2:]
            elif base[:4] == "ipag" and base[4] == '-':
                return base[:2] + "in" + base[2:5] + base[5:]
            
            if base[0] in consonants and base[:2] != "ng" and base[1:3] == "um":
                return base
            elif base[0] in consonants and base[:2] == "ng" and base[2:4] == "um":
                return base
            elif base[0] in vowels and base[:2] == "um":
                return base
            else:
                return base
        
        elif focus == "actout": #-an verbs & mag- verbs
            if base[-2:] == "an" and base[:4] != "mag-":
                if base[0] in consonants:
                    if base[0] in ('l', 'r', 'w', 'y'):
                        return "ni" + base
                    else:
                        return base[0] + "in" + base[1:]
                else:
                    return "in" + base

            if base[-2:] == "an" and base[:2] == "ng" and base[:4] != "mag-":
                return base[:2] + "in" + base[2:]

            if base[:4] == "mag-":
                if base[4] in consonants:
                    x = "n" + base[1:]
                    return x
                else:
                    x = "n" + base[1:]
                    return x

            if base[:4] == "mang":
                x = "n" + base[1:]
                return x
            
        elif focus == "object":
            if base[-2:] == "in" and base[:2] != "ng" and base[:2] != "ma": #-in verbs
                x = base[:-2]

                if x[-2] == 'u' and x[-1] in ('b', 'k', 'd', 'g', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'y'):
                    y = x[:-2] + "o" + x[-1]
                    if x[:5] == "papag" and x[:6] != "papag-":
                        return y[:1] + "in" + y[3:]
                    if x[:4] == "papa":
                       return y[:1] + "in" + y[3:]
                    else:
                        return y[:1] + "in" + y[1:]

                if x[-2] == 'u' and x[-1] == 'h':
                    return base[:1] + "in" + base[3:-4] + "o"
                
                if x[-1] in vowels and x[-1] == 'u':
                    if x[:5] == "papag" and x[:6] != "papag-" and x[5:7] == "ka":
                        return x[2] + "in" + x[3:-1] + "o"
                    else:
                        y = x[:-1] + "o"
                        if y[0] in ('l', 'r'):
                            return "ni" + y
                        else:
                            return y[:1] + "in" + y[1:]
                
                if x[-1] == 'h' and x[-2] in consonants:
                    y = x[:-1] + "i"
                    return y[0] + "in" + y[1:]

                if x[:4] == "papa":
                    return x[:1] + "in" + x[3:]

                if x[:5] == "papag" and x[:6] != "papag-" and x[:-1] != 'h':
                    return x[:1] + "in" + x[3:]

                if x[-1] == 'h' and x[-2] in ('a','e','i','o') and x[0] in consonants:
                    y = x[:-1]
                    if y[:6] == "papag-":
                        return y[:1] + "in" + y[3:]
                    elif y[:5] == "papag" and y[:6] != "papag-":
                        return y[:1] + "in" + y[3:]
                    elif y[:4] == "papa" and y[:5] != "papag" and y[:6] != "papag-":
                        return y[:1] + "in" + y[3:]
                    else:
                        return y[:1] + "in" + y[1:]                                            

                if x[-1] == 'h' and x[-2] in ('a','e','i','o') and x[0] in vowels:
                    y = x[:-1]
                    return "in" + y

                if x[-1] == 'r':
                    y = x[:-1] + "d"
                    if y[:4] == "papa":
                        return y[:1] + "in" + y[3:]
                    else:
                        return y[:1] + "in" + y[1:]
                    
                if x[0] in ('l', 'r'):
                        return "ni" + x
                else:
                        return x[:1] + "in" + x[1:]


            if base[-2:] == "in" and base[:2] == "ng" and base[:2] != "ma":
                return base[:2] + base[5:] + base[2:5]
                    
            if base[0] == "i": #i- verbs
                if base[1] in vowels or base[1] in ('l','r'):
                    return base[:1] + "ni" + base[1:]
                else:
                    return base[:2] + "in" + base[2:]
                
            if base[-2:] == "an" and base[:2] != "ma": #-an verbs
                if base[0] == 'l':
                    return "ni" + base
                elif base[0] in vowels:
                    return "in" + base
                else:
                    return base[:1] + "in" + base[1:]

            if base[:2] == "ma": #ma- verbs                
                if base[2] in consonants:
                    x = "n" + base[1:]
                    return x
                else:
                    x = "n" + base[1:]
                    return x 
                    
        else:
            return "TANGINA THIS!"

def verb_future(word):
    if "focus" in word.features:
        base = word.base
        focus = word.features["focus"]
        x = ""
        y = ""

        if focus == "actin": #ipag- verbs & -um- verbs
            if base[:4] == "ipag" and base[4] != '-':
                return base[:4] + base[4:6] + base[4:]
            elif base[:4] == "ipag" and base[4] == "-":
                return base[:5] + base[5] + base[5:]
            
            if base[0] in consonants and base[:2] != "ng" and base[1:3] == "um":
                x = base[0] + base[3:]
                return x[:2] + x
            elif base[0] in consonants and base[:2] == "ng" and base[2:4] == "um":
                x = base[:2] + base[4:]
                y = base[:2] + base[4]
                return y + x
            elif base[0] in vowels and base[:2] == "um":
                return base[2] + base[2:]
            else:
                return base

        elif focus == "actout": #-an verbs
            if base[-2:] == "an" and base[:2] != "ng" and base[:4] != "mag-":
                if base[0] in consonants:
                    return base[:2] + base
                else:
                    return base[0] + base

            if base[-2:] == "an" and base[:2] == "ng" and base[:4] != "mag-":
                return base[:3] + base

            if base[:4] == "mag-":
                if base[4] in consonants:
                    return base[:4] + base[4:6] + base[4:]
                else:
                    return base[:4] + base[4] + base[4:]

            if base[:4] == "mang":
                return base[:4] + base[4:6] + base[4:]

        elif focus == "object":
            if base[-2:] == "in" and base[:2] != "ng" and base[:2] != "ma" and base[:5] != "papag" and base[:6] != "papag-": #-in verbs
                if base[0] in consonants and base[:4] != "papa":
                    return base[:2] + base
                elif base[0] in consonants and base[:4] == "papa":
                    return base
                else:
                    return base[0] + base

            if base[-2:] == "in" and base[:2] == "ng" and base[:2] != "ma":
                return base[:3] + base[:5]

            if base[-2:] == "in" and base[:6] == "papag-":
                return base

            if base[-2:] == "in" and base[:5] == "papag" and base[:6] != "papag-":
                return base
            
            if base[0] == "i": #i- verbs
                if base[1] in consonants:
                    return base[:1] + base[1:3] + base[1:]
                else:
                    return base[:1] + base[1:2] + base[1:]

            if base[-2:] == "an" and base[:2] != "ma": #-an verbs
                if base[0] in consonants:
                    return base[:2] + base
                else:
                    return base[:1] + base

            if base[:2] == "ma": #ma- verbs                
                if base[2] in consonants and base[2:4] != "ng":
                    return base[:2] + base[2:4] + base[2:]
                elif base[2] in consonants and base[2:4] == "ng":
                    return base[:2] + base[2:5] + base[2:]
                else:
                    return base[:2] + base[2] + base[2:]
        else:
            return "TANGINA THIS!"
        

#def verb_present_participle(word):
#    if "presentparticiple" in word.features:
#        return word.features["presentparticiple"]

#def verb_past_participle(word):
#    if "pastparticiple" in word.features:
#        return word.features["pastparticiple"]

#def verb_present_progressive(word):
#    if "presentprogressive" in word.features:
#        return word.features["presentprogressive"]
    
#def verb_past_progressive(word):
#    if "pastprogressive" in word.features:
#        return word.features["pastprogressive"]
        
    
        
        
def adj_comparative(word):
    if "comparative" in word.features:
        return "mas" + " " + word.base
    
def adj_superlative(word):
    if "superlative" in word.features:
        return "pinaka" + " " + word.base
