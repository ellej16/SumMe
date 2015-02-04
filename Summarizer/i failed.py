Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> import Summarizer
>>> import Summarizer as summe
>>> summe.getSentences("""	Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration. In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.

	With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience. In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas. What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.

	We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus. We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.

	With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business. We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business. Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.

	After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms. Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market. What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways. We will continue to value self-innovation in line with the times and aim for growth.

	Nintendo intends to make progress with the support and encouragement of its shareholders and investors.""")
en Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration.
en In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.
en With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience.
en In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas.
en What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.
en We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus.
en We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.
en With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business.
en We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business.
en Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.
en After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms.
en Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market.
en What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways.
en We will continue to value self-innovation in line with the times and aim for growth.
en Nintendo intends to make progress with the support and encouragement of its shareholders and investors.
>>> summe.doGet()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    summe.doGet()
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\Summarizer.py", line 164, in doGet
    getTriple()
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\Summarizer.py", line 62, in getTriple
    sents.append(preprocessor.getSVO(sents[0],sents[2],True))
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\PreProcessing\preprocessor.py", line 95, in getSVO
    posit = sent.index(vb)
ValueError: 'VBZ' is not in list
>>> ================================ RESTART ================================
>>> 
>>> import Summarizer as summe
>>> summe.getSentences("""	Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration. In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.

	With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience. In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas. What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.

	We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus. We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.

	With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business. We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business. Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.

	After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms. Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market. What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways. We will continue to value self-innovation in line with the times and aim for growth.

	Nintendo intends to make progress with the support and encouragement of its shareholders and investors.""")
en Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration.
en In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.
en With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience.
en In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas.
en What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.
en We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus.
en We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.
en With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business.
en We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business.
en Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.
en After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms.
en Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market.
en What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways.
en We will continue to value self-innovation in line with the times and aim for growth.
en Nintendo intends to make progress with the support and encouragement of its shareholders and investors.
>>> summe.doGet()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    summe.doGet()
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\Summarizer.py", line 164, in doGet
    getTriple()
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\Summarizer.py", line 62, in getTriple
    sents.append(preprocessor.getSVO(sents[0],sents[2],True))
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\PreProcessing\preprocessor.py", line 105, in getSVO
    for subj, obj in subjs, objs:
ValueError: too many values to unpack (expected 2)
>>> ================================ RESTART ================================
>>> 
>>> import Summarizer as summe
>>> summe.getSentences("""	Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration. In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.

	With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience. In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas. What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.

	We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus. We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.

	With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business. We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business. Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.

	After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms. Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market. What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways. We will continue to value self-innovation in line with the times and aim for growth.

	Nintendo intends to make progress with the support and encouragement of its shareholders and investors.""")
en Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration.
en In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.
en With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience.
en In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas.
en What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.
en We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus.
en We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.
en With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business.
en We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business.
en Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.
en After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms.
en Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market.
en What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways.
en We will continue to value self-innovation in line with the times and aim for growth.
en Nintendo intends to make progress with the support and encouragement of its shareholders and investors.
>>> summe.doGet()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    summe.doGet()
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\Summarizer.py", line 164, in doGet
    getTriple()
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\Summarizer.py", line 62, in getTriple
    sents.append(preprocessor.getSVO(sents[0],sents[2],True))
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\PreProcessing\preprocessor.py", line 105, in getSVO
    for subj in subs:
NameError: name 'subs' is not defined
>>> ================================ RESTART ================================
>>> 
>>> import Summarizer as summe
>>> summe.getSentences("""	Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration. In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.

	With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience. In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas. What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.

	We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus. We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.

	With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business. We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business. Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.

	After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms. Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market. What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways. We will continue to value self-innovation in line with the times and aim for growth.

	Nintendo intends to make progress with the support and encouragement of its shareholders and investors.""")
en Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration.
en In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.
en With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience.
en In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas.
en What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.
en We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus.
en We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.
en With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business.
en We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business.
en Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.
en After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms.
en Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market.
en What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways.
en We will continue to value self-innovation in line with the times and aim for growth.
en Nintendo intends to make progress with the support and encouragement of its shareholders and investors.
>>> summe.doGet()
>>> summe.sentences[0][5]
[<PreProcessing.preprocessor.SVO object at 0x051F6170>, <PreProcessing.preprocessor.SVO object at 0x051F6190>, <PreProcessing.preprocessor.SVO object at 0x051F61B0>, <PreProcessing.preprocessor.SVO object at 0x051F61D0>, <PreProcessing.preprocessor.SVO object at 0x051F61F0>, <PreProcessing.preprocessor.SVO object at 0x051F6210>, <PreProcessing.preprocessor.SVO object at 0x051F6230>, <PreProcessing.preprocessor.SVO object at 0x051F6250>, <PreProcessing.preprocessor.SVO object at 0x051F6270>, <PreProcessing.preprocessor.SVO object at 0x051F6290>, <PreProcessing.preprocessor.SVO object at 0x051F62B0>, <PreProcessing.preprocessor.SVO object at 0x051F62D0>, <PreProcessing.preprocessor.SVO object at 0x051F62F0>, <PreProcessing.preprocessor.SVO object at 0x051F6310>, <PreProcessing.preprocessor.SVO object at 0x051F6330>, <PreProcessing.preprocessor.SVO object at 0x051F6350>, <PreProcessing.preprocessor.SVO object at 0x051F6370>, <PreProcessing.preprocessor.SVO object at 0x051F6390>, <PreProcessing.preprocessor.SVO object at 0x051F63B0>, <PreProcessing.preprocessor.SVO object at 0x051F63D0>, <PreProcessing.preprocessor.SVO object at 0x051F63F0>, <PreProcessing.preprocessor.SVO object at 0x051F6410>, <PreProcessing.preprocessor.SVO object at 0x051F6430>, <PreProcessing.preprocessor.SVO object at 0x051F6450>, <PreProcessing.preprocessor.SVO object at 0x051F6470>, <PreProcessing.preprocessor.SVO object at 0x051F6490>, <PreProcessing.preprocessor.SVO object at 0x051F64B0>, <PreProcessing.preprocessor.SVO object at 0x051F64D0>, <PreProcessing.preprocessor.SVO object at 0x051F64F0>, <PreProcessing.preprocessor.SVO object at 0x051F6510>, <PreProcessing.preprocessor.SVO object at 0x051F6530>, <PreProcessing.preprocessor.SVO object at 0x051F6550>, <PreProcessing.preprocessor.SVO object at 0x051F6570>, <PreProcessing.preprocessor.SVO object at 0x051F6590>, <PreProcessing.preprocessor.SVO object at 0x051F65B0>, <PreProcessing.preprocessor.SVO object at 0x051F65D0>, <PreProcessing.preprocessor.SVO object at 0x051F65F0>, <PreProcessing.preprocessor.SVO object at 0x051F6610>, <PreProcessing.preprocessor.SVO object at 0x051F6630>, <PreProcessing.preprocessor.SVO object at 0x051F6650>, <PreProcessing.preprocessor.SVO object at 0x051F6670>, <PreProcessing.preprocessor.SVO object at 0x051F6690>, <PreProcessing.preprocessor.SVO object at 0x051F66B0>, <PreProcessing.preprocessor.SVO object at 0x051F66D0>, <PreProcessing.preprocessor.SVO object at 0x051F66F0>, <PreProcessing.preprocessor.SVO object at 0x051F6710>, <PreProcessing.preprocessor.SVO object at 0x051F6730>, <PreProcessing.preprocessor.SVO object at 0x051F6750>, <PreProcessing.preprocessor.SVO object at 0x051F6770>, <PreProcessing.preprocessor.SVO object at 0x051F6790>, <PreProcessing.preprocessor.SVO object at 0x051F67B0>, <PreProcessing.preprocessor.SVO object at 0x051F67D0>, <PreProcessing.preprocessor.SVO object at 0x051F67F0>, <PreProcessing.preprocessor.SVO object at 0x051F6810>, <PreProcessing.preprocessor.SVO object at 0x051F6830>, <PreProcessing.preprocessor.SVO object at 0x051F6850>, <PreProcessing.preprocessor.SVO object at 0x051F6870>, <PreProcessing.preprocessor.SVO object at 0x051F6890>, <PreProcessing.preprocessor.SVO object at 0x051F68B0>, <PreProcessing.preprocessor.SVO object at 0x051F68D0>, <PreProcessing.preprocessor.SVO object at 0x051F68F0>, <PreProcessing.preprocessor.SVO object at 0x051F6910>, <PreProcessing.preprocessor.SVO object at 0x051F6930>, <PreProcessing.preprocessor.SVO object at 0x051F6950>, <PreProcessing.preprocessor.SVO object at 0x051F6970>, <PreProcessing.preprocessor.SVO object at 0x051F6990>, <PreProcessing.preprocessor.SVO object at 0x051F69B0>, <PreProcessing.preprocessor.SVO object at 0x051F69D0>, <PreProcessing.preprocessor.SVO object at 0x051F69F0>, <PreProcessing.preprocessor.SVO object at 0x051F6A10>, <PreProcessing.preprocessor.SVO object at 0x051F6A30>, <PreProcessing.preprocessor.SVO object at 0x051F6A50>, <PreProcessing.preprocessor.SVO object at 0x051F6A70>, <PreProcessing.preprocessor.SVO object at 0x051F6A90>, <PreProcessing.preprocessor.SVO object at 0x051F6AB0>, <PreProcessing.preprocessor.SVO object at 0x051F6AD0>, <PreProcessing.preprocessor.SVO object at 0x051F6AF0>, <PreProcessing.preprocessor.SVO object at 0x051F6B10>, <PreProcessing.preprocessor.SVO object at 0x051F6B30>, <PreProcessing.preprocessor.SVO object at 0x051F6B50>, <PreProcessing.preprocessor.SVO object at 0x051F6B70>, <PreProcessing.preprocessor.SVO object at 0x051F6B90>, <PreProcessing.preprocessor.SVO object at 0x051F6BB0>, <PreProcessing.preprocessor.SVO object at 0x051F6BD0>, <PreProcessing.preprocessor.SVO object at 0x051F6BF0>, <PreProcessing.preprocessor.SVO object at 0x051F6C10>, <PreProcessing.preprocessor.SVO object at 0x051F6C30>, <PreProcessing.preprocessor.SVO object at 0x051F6C50>, <PreProcessing.preprocessor.SVO object at 0x051F6C70>, <PreProcessing.preprocessor.SVO object at 0x051F6C90>, <PreProcessing.preprocessor.SVO object at 0x051F6CB0>, <PreProcessing.preprocessor.SVO object at 0x051F6CD0>, <PreProcessing.preprocessor.SVO object at 0x051F6CF0>, <PreProcessing.preprocessor.SVO object at 0x051F6D10>, <PreProcessing.preprocessor.SVO object at 0x051F6D30>, <PreProcessing.preprocessor.SVO object at 0x051F6D50>, <PreProcessing.preprocessor.SVO object at 0x051F6D70>, <PreProcessing.preprocessor.SVO object at 0x051F6D90>, <PreProcessing.preprocessor.SVO object at 0x051F6DB0>, <PreProcessing.preprocessor.SVO object at 0x051F6DD0>, <PreProcessing.preprocessor.SVO object at 0x051F6DF0>, <PreProcessing.preprocessor.SVO object at 0x051F6E10>, <PreProcessing.preprocessor.SVO object at 0x051F6E30>, <PreProcessing.preprocessor.SVO object at 0x051F6E50>, <PreProcessing.preprocessor.SVO object at 0x051F6E70>, <PreProcessing.preprocessor.SVO object at 0x051F6E90>, <PreProcessing.preprocessor.SVO object at 0x051F6EB0>, <PreProcessing.preprocessor.SVO object at 0x051F6ED0>, <PreProcessing.preprocessor.SVO object at 0x051F6EF0>, <PreProcessing.preprocessor.SVO object at 0x051F6F10>, <PreProcessing.preprocessor.SVO object at 0x051F6F30>, <PreProcessing.preprocessor.SVO object at 0x051F6F50>, <PreProcessing.preprocessor.SVO object at 0x051F6F70>, <PreProcessing.preprocessor.SVO object at 0x051F6F90>, <PreProcessing.preprocessor.SVO object at 0x051F6FB0>, <PreProcessing.preprocessor.SVO object at 0x051F6FD0>, <PreProcessing.preprocessor.SVO object at 0x051F6FF0>, <PreProcessing.preprocessor.SVO object at 0x051F9030>, <PreProcessing.preprocessor.SVO object at 0x051F9050>, <PreProcessing.preprocessor.SVO object at 0x051F9070>, <PreProcessing.preprocessor.SVO object at 0x051F9090>, <PreProcessing.preprocessor.SVO object at 0x051F90B0>, <PreProcessing.preprocessor.SVO object at 0x051F90D0>, <PreProcessing.preprocessor.SVO object at 0x051F90F0>, <PreProcessing.preprocessor.SVO object at 0x051F9110>, <PreProcessing.preprocessor.SVO object at 0x051F9130>, <PreProcessing.preprocessor.SVO object at 0x051F9150>, <PreProcessing.preprocessor.SVO object at 0x051F9170>, <PreProcessing.preprocessor.SVO object at 0x051F9190>, <PreProcessing.preprocessor.SVO object at 0x051F91B0>, <PreProcessing.preprocessor.SVO object at 0x051F91D0>, <PreProcessing.preprocessor.SVO object at 0x051F91F0>, <PreProcessing.preprocessor.SVO object at 0x051F9210>, <PreProcessing.preprocessor.SVO object at 0x051F9230>, <PreProcessing.preprocessor.SVO object at 0x051F9250>]
>>> len(summe.sentences[0][5])
135
>>> for svo in summe.sentences:
	for rlysvo in svo[5]:
		print(rlysvo.subj)
		print(rlysvo.obj)
		print(rlysvo.verb)

		
[0, ('launch', 'NN')]
[0, ('world', 'NN')]
('has', 'VBZ')
[0, ('launch', 'NN')]
[0, ('unique', 'NN')]
('has', 'VBZ')
[0, ('launch', 'NN')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('launch', 'NN')]
[0, ('products', 'NNS')]
('has', 'VBZ')
[0, ('launch', 'NN')]
[0, ('development', 'NN')]
('has', 'VBZ')
[0, ('launch', 'NN')]
[0, ('concept', 'NN')]
('has', 'VBZ')
[0, ('launch', 'NN')]
[0, ('hardware', 'NN')]
('has', 'VBZ')
[0, ('launch', 'NN')]
[0, ('software', 'NN')]
('has', 'VBZ')
[0, ('launch', 'NN')]
[0, ('integration', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('world', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('unique', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('products', 'NNS')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('development', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('concept', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('hardware', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('software', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('integration', 'NN')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('world', 'NN')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('unique', 'NN')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('products', 'NNS')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('development', 'NN')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('concept', 'NN')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('hardware', 'NN')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('software', 'NN')]
('has', 'VBZ')
[0, ('Entertainment', 'NNP')]
[0, ('integration', 'NN')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('world', 'NN')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('unique', 'NN')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('products', 'NNS')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('development', 'NN')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('concept', 'NN')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('hardware', 'NN')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('software', 'NN')]
('has', 'VBZ')
[0, ('System', 'NNP')]
[0, ('integration', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('world', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('unique', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('products', 'NNS')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('development', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('concept', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('hardware', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('software', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('integration', 'NN')]
('has', 'VBZ')
[1, ('launch', 'NN')]
[1, ('world', 'NN')]
('been', 'VBN')
[1, ('launch', 'NN')]
[1, ('unique', 'NN')]
('been', 'VBN')
[1, ('launch', 'NN')]
[1, ('entertainment', 'NN')]
('been', 'VBN')
[1, ('launch', 'NN')]
[1, ('products', 'NNS')]
('been', 'VBN')
[1, ('launch', 'NN')]
[1, ('development', 'NN')]
('been', 'VBN')
[1, ('launch', 'NN')]
[1, ('concept', 'NN')]
('been', 'VBN')
[1, ('launch', 'NN')]
[1, ('hardware', 'NN')]
('been', 'VBN')
[1, ('launch', 'NN')]
[1, ('software', 'NN')]
('been', 'VBN')
[1, ('launch', 'NN')]
[1, ('integration', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('world', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('unique', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('entertainment', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('products', 'NNS')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('development', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('concept', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('hardware', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('software', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('integration', 'NN')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('world', 'NN')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('unique', 'NN')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('entertainment', 'NN')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('products', 'NNS')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('development', 'NN')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('concept', 'NN')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('hardware', 'NN')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('software', 'NN')]
('been', 'VBN')
[1, ('Entertainment', 'NNP')]
[1, ('integration', 'NN')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('world', 'NN')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('unique', 'NN')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('entertainment', 'NN')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('products', 'NNS')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('development', 'NN')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('concept', 'NN')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('hardware', 'NN')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('software', 'NN')]
('been', 'VBN')
[1, ('System', 'NNP')]
[1, ('integration', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('world', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('unique', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('entertainment', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('products', 'NNS')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('development', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('concept', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('hardware', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('software', 'NN')]
('been', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('integration', 'NN')]
('been', 'VBN')
[2, ('launch', 'NN')]
[2, ('world', 'NN')]
('offering', 'VBG')
[2, ('launch', 'NN')]
[2, ('unique', 'NN')]
('offering', 'VBG')
[2, ('launch', 'NN')]
[2, ('entertainment', 'NN')]
('offering', 'VBG')
[2, ('launch', 'NN')]
[2, ('products', 'NNS')]
('offering', 'VBG')
[2, ('launch', 'NN')]
[2, ('development', 'NN')]
('offering', 'VBG')
[2, ('launch', 'NN')]
[2, ('concept', 'NN')]
('offering', 'VBG')
[2, ('launch', 'NN')]
[2, ('hardware', 'NN')]
('offering', 'VBG')
[2, ('launch', 'NN')]
[2, ('software', 'NN')]
('offering', 'VBG')
[2, ('launch', 'NN')]
[2, ('integration', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('world', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('unique', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('entertainment', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('products', 'NNS')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('development', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('concept', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('hardware', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('software', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('integration', 'NN')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('world', 'NN')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('unique', 'NN')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('entertainment', 'NN')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('products', 'NNS')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('development', 'NN')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('concept', 'NN')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('hardware', 'NN')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('software', 'NN')]
('offering', 'VBG')
[2, ('Entertainment', 'NNP')]
[2, ('integration', 'NN')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('world', 'NN')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('unique', 'NN')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('entertainment', 'NN')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('products', 'NNS')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('development', 'NN')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('concept', 'NN')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('hardware', 'NN')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('software', 'NN')]
('offering', 'VBG')
[2, ('System', 'NNP')]
[2, ('integration', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('world', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('unique', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('entertainment', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('products', 'NNS')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('development', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('concept', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('hardware', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('software', 'NN')]
('offering', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('integration', 'NN')]
('offering', 'VBG')
[0, ('field', 'NN')]
[0, ('industries', 'NNS')]
('is', 'VBZ')
[0, ('field', 'NN')]
[0, ('Japan', 'NNP')]
('is', 'VBZ')
[0, ('field', 'NN')]
[0, ('spread', 'NN')]
('is', 'VBZ')
[0, ('field', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('field', 'NN')]
[0, ('Nintendo', 'NNP')]
('is', 'VBZ')
[0, ('field', 'NN')]
[0, ('brand', 'NN')]
('is', 'VBZ')
[0, ('field', 'NN')]
[0, ('culture', 'NN')]
('is', 'VBZ')
[0, ('field', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('home', 'NN')]
[0, ('industries', 'NNS')]
('is', 'VBZ')
[0, ('home', 'NN')]
[0, ('Japan', 'NNP')]
('is', 'VBZ')
[0, ('home', 'NN')]
[0, ('spread', 'NN')]
('is', 'VBZ')
[0, ('home', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('home', 'NN')]
[0, ('Nintendo', 'NNP')]
('is', 'VBZ')
[0, ('home', 'NN')]
[0, ('brand', 'NN')]
('is', 'VBZ')
[0, ('home', 'NN')]
[0, ('culture', 'NN')]
('is', 'VBZ')
[0, ('home', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('industries', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('Japan', 'NNP')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('spread', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('Nintendo', 'NNP')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('brand', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('culture', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('industries', 'NNS')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('Japan', 'NNP')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('spread', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('Nintendo', 'NNP')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('brand', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('culture', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('industries', 'NNS')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('Japan', 'NNP')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('spread', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('Nintendo', 'NNP')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('brand', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('culture', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('industry', 'NN')]
[0, ('industries', 'NNS')]
('is', 'VBZ')
[0, ('industry', 'NN')]
[0, ('Japan', 'NNP')]
('is', 'VBZ')
[0, ('industry', 'NN')]
[0, ('spread', 'NN')]
('is', 'VBZ')
[0, ('industry', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('industry', 'NN')]
[0, ('Nintendo', 'NNP')]
('is', 'VBZ')
[0, ('industry', 'NN')]
[0, ('brand', 'NN')]
('is', 'VBZ')
[0, ('industry', 'NN')]
[0, ('culture', 'NN')]
('is', 'VBZ')
[0, ('industry', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('industries', 'NNS')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('Japan', 'NNP')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('spread', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('Nintendo', 'NNP')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('brand', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('culture', 'NN')]
('is', 'VBZ')
[0, ('video', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('industries', 'NNS')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('Japan', 'NNP')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('spread', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('Nintendo', 'NNP')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('brand', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('culture', 'NN')]
('is', 'VBZ')
[0, ('game', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[1, ('field', 'NN')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('field', 'NN')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('field', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('field', 'NN')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('field', 'NN')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('field', 'NN')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('field', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('home', 'NN')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('home', 'NN')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('home', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('home', 'NN')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('home', 'NN')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('home', 'NN')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('home', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('entertainment', 'NN')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('entertainment', 'NN')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('entertainment', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('entertainment', 'NN')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('entertainment', 'NN')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('entertainment', 'NN')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('entertainment', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('industry', 'NN')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('industry', 'NN')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('industry', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('industry', 'NN')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('industry', 'NN')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('industry', 'NN')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('industry', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('industries', 'NNS')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('industries', 'NNS')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('industries', 'NNS')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('industries', 'NNS')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('industries', 'NNS')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('industries', 'NNS')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('industries', 'NNS')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('video', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('Japan', 'NNP')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('spread', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('Nintendo', 'NNP')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('brand', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('culture', 'NN')]
('established', 'VBD')
[1, ('game', 'NN')]
[1, ('world', 'NN')]
('established', 'VBD')
[2, ('field', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('field', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('home', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('home', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('entertainment', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('entertainment', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('video', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('video', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('game', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('game', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('industry', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('industry', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('industries', 'NNS')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('industries', 'NNS')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('Japan', 'NNP')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('Japan', 'NNP')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('spread', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('spread', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('world', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('world', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('Nintendo', 'NNP')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('Nintendo', 'NNP')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('video', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('video', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('game', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('game', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[2, ('world', 'NN')]
[2, ('brand', 'NN')]
('has', 'VBZ')
[2, ('world', 'NN')]
[2, ('culture', 'NN')]
('has', 'VBZ')
[3, ('field', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('field', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('home', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('home', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('video', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('video', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('game', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('game', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('industry', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('industry', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('industries', 'NNS')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('industries', 'NNS')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('Japan', 'NNP')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('Japan', 'NNP')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('spread', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('spread', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('world', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('world', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('Nintendo', 'NNP')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('Nintendo', 'NNP')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('video', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('video', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('game', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('game', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[3, ('world', 'NN')]
[3, ('brand', 'NN')]
('established', 'VBN')
[3, ('world', 'NN')]
[3, ('culture', 'NN')]
('established', 'VBN')
[4, ('field', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('field', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('home', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('home', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('entertainment', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('entertainment', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('video', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('video', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('game', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('game', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('industry', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('industry', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('industries', 'NNS')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('industries', 'NNS')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('Japan', 'NNP')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('Japan', 'NNP')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('spread', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('spread', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('world', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('world', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('Nintendo', 'NNP')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('Nintendo', 'NNP')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('video', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('video', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('game', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('game', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[4, ('world', 'NN')]
[4, ('brand', 'NN')]
('known', 'VBN')
[4, ('world', 'NN')]
[4, ('culture', 'NN')]
('known', 'VBN')
[5, ('field', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('home', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('video', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('game', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('industry', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('industries', 'NNS')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('Japan', 'NNP')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('spread', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('world', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('Nintendo', 'NNP')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('brand', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('video', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('game', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[5, ('world', 'NN')]
[5, ('culture', 'NN')]
('representing', 'VBG')
[0, ('belief', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[1, ('belief', 'NN')]
[1, ('smiles', 'NNS')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('people', 'NNS')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('s', 'NNS')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('faces', 'NNS')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('world', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('services', 'NNS')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('decade', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('strategy', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('gaming', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('population', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('offering', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('everyone', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('regardless', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('age', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('gender', 'NN')]
('put', 'VB')
[1, ('belief', 'NN')]
[1, ('experience', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('smiles', 'NNS')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('people', 'NNS')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('s', 'NNS')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('faces', 'NNS')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('world', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('services', 'NNS')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('decade', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('strategy', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('gaming', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('population', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('offering', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('everyone', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('regardless', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('age', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('gender', 'NN')]
('put', 'VB')
[1, ('raison', 'NN')]
[1, ('experience', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('smiles', 'NNS')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('people', 'NNS')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('s', 'NNS')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('faces', 'NNS')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('world', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('services', 'NNS')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('decade', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('strategy', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('gaming', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('population', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('offering', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('everyone', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('regardless', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('age', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('gender', 'NN')]
('put', 'VB')
[1, ('d', 'NN')]
[1, ('experience', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('smiles', 'NNS')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('people', 'NNS')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('s', 'NNS')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('faces', 'NNS')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('world', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('services', 'NNS')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('decade', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('strategy', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('gaming', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('population', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('offering', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('everyone', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('regardless', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('age', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('gender', 'NN')]
('put', 'VB')
[1, ('etre', 'NN')]
[1, ('experience', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('smiles', 'NNS')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('people', 'NNS')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('s', 'NNS')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('faces', 'NNS')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('world', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('services', 'NNS')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('decade', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('strategy', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('gaming', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('population', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('offering', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('products', 'NNS')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('everyone', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('regardless', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('age', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('gender', 'NN')]
('put', 'VB')
[1, ('entertainment', 'NN')]
[1, ('experience', 'NN')]
('put', 'VB')
[2, ('belief', 'NN')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('belief', 'NN')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('raison', 'NN')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('d', 'NN')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('etre', 'NN')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('entertainment', 'NN')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('smiles', 'NNS')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('people', 'NNS')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('s', 'NNS')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('faces', 'NNS')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('world', 'NN')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('services', 'NNS')]
[2, ('experience', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('decade', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('strategy', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('gaming', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('population', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('offering', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('everyone', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('regardless', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('age', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('gender', 'NN')]
('have', 'VBP')
[2, ('products', 'NNS')]
[2, ('experience', 'NN')]
('have', 'VBP')
[3, ('belief', 'NN')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('belief', 'NN')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('raison', 'NN')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('d', 'NN')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('etre', 'NN')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('entertainment', 'NN')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('smiles', 'NNS')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('people', 'NNS')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('s', 'NNS')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('faces', 'NNS')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('world', 'NN')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('services', 'NNS')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('decade', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('strategy', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('gaming', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('population', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('offering', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('everyone', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('regardless', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('age', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('gender', 'NN')]
('focused', 'VBN')
[3, ('products', 'NNS')]
[3, ('experience', 'NN')]
('focused', 'VBN')
[0, ('belief', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('belief', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('raison', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('d', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('etre', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('smiles', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('people', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('s', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('faces', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('world', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('services', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('decade', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('strategy', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gaming', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('population', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('offering', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('products', 'NNS')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('everyone', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('regardless', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('age', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('gender', 'NN')]
('is', 'VBZ')
[0, ('entertainment', 'NN')]
[0, ('experience', 'NN')]
('is', 'VBZ')
[5, ('belief', 'NN')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('belief', 'NN')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('belief', 'NN')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('belief', 'NN')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('belief', 'NN')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('belief', 'NN')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('belief', 'NN')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('belief', 'NN')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('raison', 'NN')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('raison', 'NN')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('raison', 'NN')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('raison', 'NN')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('raison', 'NN')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('raison', 'NN')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('raison', 'NN')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('raison', 'NN')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('d', 'NN')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('d', 'NN')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('d', 'NN')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('d', 'NN')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('d', 'NN')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('d', 'NN')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('d', 'NN')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('d', 'NN')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('etre', 'NN')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('etre', 'NN')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('etre', 'NN')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('etre', 'NN')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('etre', 'NN')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('etre', 'NN')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('etre', 'NN')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('etre', 'NN')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('entertainment', 'NN')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('smiles', 'NNS')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('smiles', 'NNS')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('smiles', 'NNS')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('smiles', 'NNS')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('smiles', 'NNS')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('smiles', 'NNS')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('smiles', 'NNS')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('smiles', 'NNS')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('people', 'NNS')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('people', 'NNS')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('people', 'NNS')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('people', 'NNS')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('people', 'NNS')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('people', 'NNS')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('people', 'NNS')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('people', 'NNS')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('s', 'NNS')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('s', 'NNS')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('s', 'NNS')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('s', 'NNS')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('s', 'NNS')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('s', 'NNS')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('s', 'NNS')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('s', 'NNS')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('faces', 'NNS')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('faces', 'NNS')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('faces', 'NNS')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('faces', 'NNS')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('faces', 'NNS')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('faces', 'NNS')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('faces', 'NNS')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('faces', 'NNS')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('world', 'NN')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('world', 'NN')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('world', 'NN')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('world', 'NN')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('world', 'NN')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('world', 'NN')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('world', 'NN')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('world', 'NN')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('services', 'NNS')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('services', 'NNS')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('services', 'NNS')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('services', 'NNS')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('services', 'NNS')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('services', 'NNS')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('services', 'NNS')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('services', 'NNS')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('decade', 'NN')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('decade', 'NN')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('decade', 'NN')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('decade', 'NN')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('decade', 'NN')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('decade', 'NN')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('decade', 'NN')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('decade', 'NN')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('strategy', 'NN')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('strategy', 'NN')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('strategy', 'NN')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('strategy', 'NN')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('strategy', 'NN')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('strategy', 'NN')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('strategy', 'NN')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('strategy', 'NN')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('gaming', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('population', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('offering', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('everyone', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('regardless', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('age', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('gender', 'NN')]
('expanding', 'VBG')
[5, ('products', 'NNS')]
[5, ('experience', 'NN')]
('expanding', 'VBG')
[6, ('belief', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('belief', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('belief', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('belief', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('belief', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('raison', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('raison', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('raison', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('raison', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('raison', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('d', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('d', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('d', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('d', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('d', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('etre', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('etre', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('etre', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('etre', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('etre', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('entertainment', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('entertainment', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('entertainment', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('entertainment', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('entertainment', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('smiles', 'NNS')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('smiles', 'NNS')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('smiles', 'NNS')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('smiles', 'NNS')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('smiles', 'NNS')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('people', 'NNS')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('people', 'NNS')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('people', 'NNS')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('people', 'NNS')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('people', 'NNS')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('s', 'NNS')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('s', 'NNS')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('s', 'NNS')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('s', 'NNS')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('s', 'NNS')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('faces', 'NNS')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('faces', 'NNS')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('faces', 'NNS')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('faces', 'NNS')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('faces', 'NNS')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('world', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('world', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('world', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('world', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('world', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('services', 'NNS')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('services', 'NNS')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('services', 'NNS')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('services', 'NNS')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('services', 'NNS')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('decade', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('decade', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('decade', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('decade', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('decade', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('strategy', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('strategy', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('strategy', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('strategy', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('strategy', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('gaming', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('gaming', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('gaming', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('gaming', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('gaming', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('population', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('population', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('population', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('population', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('population', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('offering', 'NN')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('offering', 'NN')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('offering', 'NN')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('offering', 'NN')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('offering', 'NN')]
[6, ('experience', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('everyone', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('regardless', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('age', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('gender', 'NN')]
('be', 'VB')
[6, ('products', 'NNS')]
[6, ('experience', 'NN')]
('be', 'VB')
[7, ('belief', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('belief', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('belief', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('belief', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('belief', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('raison', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('raison', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('raison', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('raison', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('raison', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('d', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('d', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('d', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('d', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('d', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('etre', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('etre', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('etre', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('etre', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('etre', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('entertainment', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('entertainment', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('entertainment', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('entertainment', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('entertainment', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('smiles', 'NNS')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('smiles', 'NNS')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('smiles', 'NNS')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('smiles', 'NNS')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('smiles', 'NNS')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('people', 'NNS')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('people', 'NNS')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('people', 'NNS')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('people', 'NNS')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('people', 'NNS')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('s', 'NNS')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('s', 'NNS')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('s', 'NNS')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('s', 'NNS')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('s', 'NNS')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('faces', 'NNS')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('faces', 'NNS')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('faces', 'NNS')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('faces', 'NNS')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('faces', 'NNS')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('world', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('world', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('world', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('world', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('world', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('services', 'NNS')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('services', 'NNS')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('services', 'NNS')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('services', 'NNS')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('services', 'NNS')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('decade', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('decade', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('decade', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('decade', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('decade', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('strategy', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('strategy', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('strategy', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('strategy', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('strategy', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('gaming', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('gaming', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('gaming', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('gaming', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('gaming', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('population', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('population', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('population', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('population', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('population', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('offering', 'NN')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('offering', 'NN')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('offering', 'NN')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('offering', 'NN')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('offering', 'NN')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('everyone', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('regardless', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('age', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('gender', 'NN')]
('enjoyed', 'VBN')
[7, ('products', 'NNS')]
[7, ('experience', 'NN')]
('enjoyed', 'VBN')
[8, ('belief', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('raison', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('d', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('etre', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('entertainment', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('smiles', 'NNS')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('people', 'NNS')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('s', 'NNS')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('faces', 'NNS')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('world', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('products', 'NNS')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('services', 'NNS')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('decade', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('strategy', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('gaming', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('population', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('offering', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('products', 'NNS')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('everyone', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('regardless', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('age', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[8, ('gender', 'NN')]
[8, ('experience', 'NN')]
('gaming', 'VBG')
[0, ('addition', 'NN')]
[0, ('times', 'NNS')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('something', 'NN')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('improves', 'NNS')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('people', 'NNS')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('s', 'NNS')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('quality', 'NN')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('life', 'NN')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('QOL', 'NNP')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('ways', 'NNS')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('expand', 'NN')]
('has', 'VBZ')
[0, ('addition', 'NN')]
[0, ('areas', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('times', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('something', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('improves', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('people', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('s', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('quality', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('life', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('QOL', 'NNP')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('ways', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('expand', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('areas', 'NNS')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('times', 'NNS')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('something', 'NN')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('improves', 'NNS')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('people', 'NNS')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('s', 'NNS')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('quality', 'NN')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('life', 'NN')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('QOL', 'NNP')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('ways', 'NNS')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('expand', 'NN')]
('has', 'VBZ')
[0, ('environment', 'NN')]
[0, ('areas', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('times', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('entertainment', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('something', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('improves', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('people', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('s', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('quality', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('life', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('QOL', 'NNP')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('ways', 'NNS')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('expand', 'NN')]
('has', 'VBZ')
[0, ('business', 'NN')]
[0, ('areas', 'NNS')]
('has', 'VBZ')
[1, ('addition', 'NN')]
[1, ('times', 'NNS')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('entertainment', 'NN')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('something', 'NN')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('improves', 'NNS')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('people', 'NNS')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('s', 'NNS')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('quality', 'NN')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('life', 'NN')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('QOL', 'NNP')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('ways', 'NNS')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('expand', 'NN')]
('shifted', 'VBN')
[1, ('addition', 'NN')]
[1, ('areas', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('times', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('entertainment', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('something', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('improves', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('people', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('s', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('quality', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('life', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('QOL', 'NNP')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('ways', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('expand', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('areas', 'NNS')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('times', 'NNS')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('entertainment', 'NN')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('something', 'NN')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('improves', 'NNS')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('people', 'NNS')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('s', 'NNS')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('quality', 'NN')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('life', 'NN')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('QOL', 'NNP')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('ways', 'NNS')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('expand', 'NN')]
('shifted', 'VBN')
[1, ('environment', 'NN')]
[1, ('areas', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('times', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('entertainment', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('something', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('improves', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('people', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('s', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('quality', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('life', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('QOL', 'NNP')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('ways', 'NNS')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('expand', 'NN')]
('shifted', 'VBN')
[1, ('business', 'NN')]
[1, ('areas', 'NNS')]
('shifted', 'VBN')
[2, ('addition', 'NN')]
[2, ('entertainment', 'NN')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('something', 'NN')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('improves', 'NNS')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('people', 'NNS')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('s', 'NNS')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('quality', 'NN')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('life', 'NN')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('QOL', 'NNP')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('ways', 'NNS')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('expand', 'NN')]
('have', 'VBP')
[2, ('addition', 'NN')]
[2, ('areas', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('entertainment', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('something', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('improves', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('people', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('s', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('quality', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('life', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('QOL', 'NNP')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('ways', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('expand', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('areas', 'NNS')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('entertainment', 'NN')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('something', 'NN')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('improves', 'NNS')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('people', 'NNS')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('s', 'NNS')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('quality', 'NN')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('life', 'NN')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('QOL', 'NNP')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('ways', 'NNS')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('expand', 'NN')]
('have', 'VBP')
[2, ('environment', 'NN')]
[2, ('areas', 'NNS')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('entertainment', 'NN')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('something', 'NN')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('improves', 'NNS')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('people', 'NNS')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('s', 'NNS')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('quality', 'NN')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('life', 'NN')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('QOL', 'NNP')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('ways', 'NNS')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('expand', 'NN')]
('have', 'VBP')
[2, ('times', 'NNS')]
[2, ('areas', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('entertainment', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('something', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('improves', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('people', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('s', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('quality', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('life', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('QOL', 'NNP')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('ways', 'NNS')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('expand', 'NN')]
('have', 'VBP')
[2, ('business', 'NN')]
[2, ('areas', 'NNS')]
('have', 'VBP')
[3, ('addition', 'NN')]
[3, ('entertainment', 'NN')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('something', 'NN')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('improves', 'NNS')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('people', 'NNS')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('s', 'NNS')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('quality', 'NN')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('life', 'NN')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('QOL', 'NNP')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('ways', 'NNS')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('expand', 'NN')]
('decided', 'VBN')
[3, ('addition', 'NN')]
[3, ('areas', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('entertainment', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('something', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('improves', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('people', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('s', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('quality', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('life', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('QOL', 'NNP')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('ways', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('expand', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('areas', 'NNS')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('entertainment', 'NN')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('something', 'NN')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('improves', 'NNS')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('people', 'NNS')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('s', 'NNS')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('quality', 'NN')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('life', 'NN')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('QOL', 'NNP')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('ways', 'NNS')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('expand', 'NN')]
('decided', 'VBN')
[3, ('environment', 'NN')]
[3, ('areas', 'NNS')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('entertainment', 'NN')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('something', 'NN')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('improves', 'NNS')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('people', 'NNS')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('s', 'NNS')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('quality', 'NN')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('life', 'NN')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('QOL', 'NNP')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('ways', 'NNS')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('expand', 'NN')]
('decided', 'VBN')
[3, ('times', 'NNS')]
[3, ('areas', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('entertainment', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('something', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('improves', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('people', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('s', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('quality', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('life', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('QOL', 'NNP')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('ways', 'NNS')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('expand', 'NN')]
('decided', 'VBN')
[3, ('business', 'NN')]
[3, ('areas', 'NNS')]
('decided', 'VBN')
[4, ('addition', 'NN')]
[4, ('entertainment', 'NN')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('something', 'NN')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('improves', 'NNS')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('people', 'NNS')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('s', 'NNS')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('quality', 'NN')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('life', 'NN')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('QOL', 'NNP')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('ways', 'NNS')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('expand', 'NN')]
('redefine', 'VB')
[4, ('addition', 'NN')]
[4, ('areas', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('entertainment', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('something', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('improves', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('people', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('s', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('quality', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('life', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('QOL', 'NNP')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('ways', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('expand', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('areas', 'NNS')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('entertainment', 'NN')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('something', 'NN')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('improves', 'NNS')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('people', 'NNS')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('s', 'NNS')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('quality', 'NN')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('life', 'NN')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('QOL', 'NNP')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('ways', 'NNS')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('expand', 'NN')]
('redefine', 'VB')
[4, ('environment', 'NN')]
[4, ('areas', 'NNS')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('entertainment', 'NN')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('something', 'NN')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('improves', 'NNS')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('people', 'NNS')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('s', 'NNS')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('quality', 'NN')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('life', 'NN')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('QOL', 'NNP')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('ways', 'NNS')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('expand', 'NN')]
('redefine', 'VB')
[4, ('times', 'NNS')]
[4, ('areas', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('entertainment', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('something', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('improves', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('people', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('s', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('quality', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('life', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('QOL', 'NNP')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('ways', 'NNS')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('expand', 'NN')]
('redefine', 'VB')
[4, ('business', 'NN')]
[4, ('areas', 'NNS')]
('redefine', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('years', 'NNS')]
('try', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('platform', 'NN')]
('try', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('business', 'NN')]
('try', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('people', 'NNS')]
('try', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('s', 'NNS')]
('try', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('QOL', 'NNP')]
('try', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('ways', 'NNS')]
('try', 'VB')
[1, ('Nintendo', 'NNP')]
[1, ('years', 'NNS')]
('achieve', 'VB')
[1, ('Nintendo', 'NNP')]
[1, ('platform', 'NN')]
('achieve', 'VB')
[1, ('Nintendo', 'NNP')]
[1, ('business', 'NN')]
('achieve', 'VB')
[1, ('Nintendo', 'NNP')]
[1, ('people', 'NNS')]
('achieve', 'VB')
[1, ('Nintendo', 'NNP')]
[1, ('s', 'NNS')]
('achieve', 'VB')
[1, ('Nintendo', 'NNP')]
[1, ('QOL', 'NNP')]
('achieve', 'VB')
[1, ('Nintendo', 'NNP')]
[1, ('ways', 'NNS')]
('achieve', 'VB')
[2, ('Nintendo', 'NNP')]
[2, ('platform', 'NN')]
('is', 'VBZ')
[2, ('Nintendo', 'NNP')]
[2, ('business', 'NN')]
('is', 'VBZ')
[2, ('Nintendo', 'NNP')]
[2, ('people', 'NNS')]
('is', 'VBZ')
[2, ('Nintendo', 'NNP')]
[2, ('s', 'NNS')]
('is', 'VBZ')
[2, ('Nintendo', 'NNP')]
[2, ('QOL', 'NNP')]
('is', 'VBZ')
[2, ('Nintendo', 'NNP')]
[2, ('ways', 'NNS')]
('is', 'VBZ')
[2, ('years', 'NNS')]
[2, ('platform', 'NN')]
('is', 'VBZ')
[2, ('years', 'NNS')]
[2, ('business', 'NN')]
('is', 'VBZ')
[2, ('years', 'NNS')]
[2, ('people', 'NNS')]
('is', 'VBZ')
[2, ('years', 'NNS')]
[2, ('s', 'NNS')]
('is', 'VBZ')
[2, ('years', 'NNS')]
[2, ('QOL', 'NNP')]
('is', 'VBZ')
[2, ('years', 'NNS')]
[2, ('ways', 'NNS')]
('is', 'VBZ')
[3, ('Nintendo', 'NNP')]
[3, ('people', 'NNS')]
('improves', 'VBZ')
[3, ('Nintendo', 'NNP')]
[3, ('s', 'NNS')]
('improves', 'VBZ')
[3, ('Nintendo', 'NNP')]
[3, ('QOL', 'NNP')]
('improves', 'VBZ')
[3, ('Nintendo', 'NNP')]
[3, ('ways', 'NNS')]
('improves', 'VBZ')
[3, ('years', 'NNS')]
[3, ('people', 'NNS')]
('improves', 'VBZ')
[3, ('years', 'NNS')]
[3, ('s', 'NNS')]
('improves', 'VBZ')
[3, ('years', 'NNS')]
[3, ('QOL', 'NNP')]
('improves', 'VBZ')
[3, ('years', 'NNS')]
[3, ('ways', 'NNS')]
('improves', 'VBZ')
[3, ('platform', 'NN')]
[3, ('people', 'NNS')]
('improves', 'VBZ')
[3, ('platform', 'NN')]
[3, ('s', 'NNS')]
('improves', 'VBZ')
[3, ('platform', 'NN')]
[3, ('QOL', 'NNP')]
('improves', 'VBZ')
[3, ('platform', 'NN')]
[3, ('ways', 'NNS')]
('improves', 'VBZ')
[3, ('business', 'NN')]
[3, ('people', 'NNS')]
('improves', 'VBZ')
[3, ('business', 'NN')]
[3, ('s', 'NNS')]
('improves', 'VBZ')
[3, ('business', 'NN')]
[3, ('QOL', 'NNP')]
('improves', 'VBZ')
[3, ('business', 'NN')]
[3, ('ways', 'NNS')]
('improves', 'VBZ')
[2, ('strengths', 'NNS')]
[2, ('platform', 'NN')]
('integrated', 'VBD')
[2, ('strengths', 'NNS')]
[2, ('business', 'NN')]
('integrated', 'VBD')
[2, ('strengths', 'NNS')]
[2, ('type', 'NN')]
('integrated', 'VBD')
[2, ('strengths', 'NNS')]
[2, ('video', 'NN')]
('integrated', 'VBD')
[2, ('strengths', 'NNS')]
[2, ('game', 'NN')]
('integrated', 'VBD')
[2, ('strengths', 'NNS')]
[2, ('platforms', 'NNS')]
('integrated', 'VBD')
[2, ('strengths', 'NNS')]
[2, ('core', 'NN')]
('integrated', 'VBD')
[2, ('strengths', 'NNS')]
[2, ('focus', 'NN')]
('integrated', 'VBD')
[2, ('hardware', 'NN')]
[2, ('platform', 'NN')]
('integrated', 'VBD')
[2, ('hardware', 'NN')]
[2, ('business', 'NN')]
('integrated', 'VBD')
[2, ('hardware', 'NN')]
[2, ('type', 'NN')]
('integrated', 'VBD')
[2, ('hardware', 'NN')]
[2, ('video', 'NN')]
('integrated', 'VBD')
[2, ('hardware', 'NN')]
[2, ('game', 'NN')]
('integrated', 'VBD')
[2, ('hardware', 'NN')]
[2, ('platforms', 'NNS')]
('integrated', 'VBD')
[2, ('hardware', 'NN')]
[2, ('core', 'NN')]
('integrated', 'VBD')
[2, ('hardware', 'NN')]
[2, ('focus', 'NN')]
('integrated', 'VBD')
[2, ('software', 'NN')]
[2, ('platform', 'NN')]
('integrated', 'VBD')
[2, ('software', 'NN')]
[2, ('business', 'NN')]
('integrated', 'VBD')
[2, ('software', 'NN')]
[2, ('type', 'NN')]
('integrated', 'VBD')
[2, ('software', 'NN')]
[2, ('video', 'NN')]
('integrated', 'VBD')
[2, ('software', 'NN')]
[2, ('game', 'NN')]
('integrated', 'VBD')
[2, ('software', 'NN')]
[2, ('platforms', 'NNS')]
('integrated', 'VBD')
[2, ('software', 'NN')]
[2, ('core', 'NN')]
('integrated', 'VBD')
[2, ('software', 'NN')]
[2, ('focus', 'NN')]
('integrated', 'VBD')
[3, ('strengths', 'NNS')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('strengths', 'NNS')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('strengths', 'NNS')]
[3, ('platforms', 'NNS')]
('dedicated', 'VBN')
[3, ('strengths', 'NNS')]
[3, ('core', 'NN')]
('dedicated', 'VBN')
[3, ('strengths', 'NNS')]
[3, ('focus', 'NN')]
('dedicated', 'VBN')
[3, ('hardware', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('hardware', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('hardware', 'NN')]
[3, ('platforms', 'NNS')]
('dedicated', 'VBN')
[3, ('hardware', 'NN')]
[3, ('core', 'NN')]
('dedicated', 'VBN')
[3, ('hardware', 'NN')]
[3, ('focus', 'NN')]
('dedicated', 'VBN')
[3, ('software', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('software', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('software', 'NN')]
[3, ('platforms', 'NNS')]
('dedicated', 'VBN')
[3, ('software', 'NN')]
[3, ('core', 'NN')]
('dedicated', 'VBN')
[3, ('software', 'NN')]
[3, ('focus', 'NN')]
('dedicated', 'VBN')
[3, ('platform', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('platform', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('platform', 'NN')]
[3, ('platforms', 'NNS')]
('dedicated', 'VBN')
[3, ('platform', 'NN')]
[3, ('core', 'NN')]
('dedicated', 'VBN')
[3, ('platform', 'NN')]
[3, ('focus', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('platforms', 'NNS')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('core', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('focus', 'NN')]
('dedicated', 'VBN')
[3, ('type', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('type', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('type', 'NN')]
[3, ('platforms', 'NNS')]
('dedicated', 'VBN')
[3, ('type', 'NN')]
[3, ('core', 'NN')]
('dedicated', 'VBN')
[3, ('type', 'NN')]
[3, ('focus', 'NN')]
('dedicated', 'VBN')
[4, ('strengths', 'NNS')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('strengths', 'NNS')]
[4, ('focus', 'NN')]
('remain', 'VB')
[4, ('hardware', 'NN')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('hardware', 'NN')]
[4, ('focus', 'NN')]
('remain', 'VB')
[4, ('software', 'NN')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('software', 'NN')]
[4, ('focus', 'NN')]
('remain', 'VB')
[4, ('platform', 'NN')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('platform', 'NN')]
[4, ('focus', 'NN')]
('remain', 'VB')
[4, ('business', 'NN')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('business', 'NN')]
[4, ('focus', 'NN')]
('remain', 'VB')
[4, ('type', 'NN')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('type', 'NN')]
[4, ('focus', 'NN')]
('remain', 'VB')
[4, ('video', 'NN')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('video', 'NN')]
[4, ('focus', 'NN')]
('remain', 'VB')
[4, ('game', 'NN')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('game', 'NN')]
[4, ('focus', 'NN')]
('remain', 'VB')
[4, ('platforms', 'NNS')]
[4, ('core', 'NN')]
('remain', 'VB')
[4, ('platforms', 'NNS')]
[4, ('focus', 'NN')]
('remain', 'VB')
[2, ('spirit', 'NN')]
[2, ('motto', 'NN')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, ('True', 'NNP')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, ('Value', 'NNP')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, ('Entertainment', 'NNP')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, ('Lies', 'NNPS')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, ('Individuality', 'NNP')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, (',"', 'NNP')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, ('products', 'NNS')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, ('services', 'NNS')]
('described', 'VBN')
[2, ('spirit', 'NN')]
[2, ('people', 'NNS')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('motto', 'NN')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('True', 'NNP')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('Value', 'NNP')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('Entertainment', 'NNP')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('Lies', 'NNPS')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('Individuality', 'NNP')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, (',"', 'NNP')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('products', 'NNS')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('services', 'NNS')]
('described', 'VBN')
[2, ('originality', 'NN')]
[2, ('people', 'NNS')]
('described', 'VBN')
[4, ('spirit', 'NN')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, ('spirit', 'NN')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, ('spirit', 'NN')]
[4, ('people', 'NNS')]
('provide', 'VB')
[4, ('originality', 'NN')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, ('originality', 'NN')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, ('originality', 'NN')]
[4, ('people', 'NNS')]
('provide', 'VB')
[4, ('motto', 'NN')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, ('motto', 'NN')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, ('motto', 'NN')]
[4, ('people', 'NNS')]
('provide', 'VB')
[4, ('True', 'NNP')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, ('True', 'NNP')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, ('True', 'NNP')]
[4, ('people', 'NNS')]
('provide', 'VB')
[4, ('Value', 'NNP')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, ('Value', 'NNP')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, ('Value', 'NNP')]
[4, ('people', 'NNS')]
('provide', 'VB')
[4, ('Entertainment', 'NNP')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, ('Entertainment', 'NNP')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, ('Entertainment', 'NNP')]
[4, ('people', 'NNS')]
('provide', 'VB')
[4, ('Lies', 'NNPS')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, ('Lies', 'NNPS')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, ('Lies', 'NNPS')]
[4, ('people', 'NNS')]
('provide', 'VB')
[4, ('Individuality', 'NNP')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, ('Individuality', 'NNP')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, ('Individuality', 'NNP')]
[4, ('people', 'NNS')]
('provide', 'VB')
[4, (',"', 'NNP')]
[4, ('products', 'NNS')]
('provide', 'VB')
[4, (',"', 'NNP')]
[4, ('services', 'NNS')]
('provide', 'VB')
[4, (',"', 'NNP')]
[4, ('people', 'NNS')]
('provide', 'VB')
[5, ('spirit', 'NN')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('originality', 'NN')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('motto', 'NN')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('True', 'NNP')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('Value', 'NNP')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('Entertainment', 'NNP')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('Lies', 'NNPS')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('Individuality', 'NNP')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, (',"', 'NNP')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('products', 'NNS')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[5, ('services', 'NNS')]
[5, ('people', 'NNS')]
('surprise', 'VBP')
[0, ('platform', 'NN')]
[0, ('people', 'NNS')]
('improves', 'VBZ')
[0, ('platform', 'NN')]
[0, ('s', 'NNS')]
('improves', 'VBZ')
[0, ('platform', 'NN')]
[0, ('QOL', 'NNP')]
('improves', 'VBZ')
[0, ('platform', 'NN')]
[0, ('ways', 'NNS')]
('improves', 'VBZ')
[0, ('platform', 'NN')]
[0, ('area', 'NN')]
('improves', 'VBZ')
[0, ('platform', 'NN')]
[0, ('apart', 'NN')]
('improves', 'VBZ')
[0, ('platform', 'NN')]
[0, ('video', 'NN')]
('improves', 'VBZ')
[0, ('platform', 'NN')]
[0, ('game', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('people', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('s', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('QOL', 'NNP')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('ways', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('area', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('apart', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('video', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('game', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('people', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('s', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('QOL', 'NNP')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('ways', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('area', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('apart', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('video', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('game', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('people', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('s', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('QOL', 'NNP')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('ways', 'NNS')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('area', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('apart', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('video', 'NN')]
('improves', 'VBZ')
[0, ('business', 'NN')]
[0, ('game', 'NN')]
('improves', 'VBZ')
[1, ('platform', 'NN')]
[1, ('area', 'NN')]
('attempt', 'VB')
[1, ('platform', 'NN')]
[1, ('apart', 'NN')]
('attempt', 'VB')
[1, ('platform', 'NN')]
[1, ('video', 'NN')]
('attempt', 'VB')
[1, ('platform', 'NN')]
[1, ('game', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('area', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('apart', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('video', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('game', 'NN')]
('attempt', 'VB')
[1, ('people', 'NNS')]
[1, ('area', 'NN')]
('attempt', 'VB')
[1, ('people', 'NNS')]
[1, ('apart', 'NN')]
('attempt', 'VB')
[1, ('people', 'NNS')]
[1, ('video', 'NN')]
('attempt', 'VB')
[1, ('people', 'NNS')]
[1, ('game', 'NN')]
('attempt', 'VB')
[1, ('s', 'NNS')]
[1, ('area', 'NN')]
('attempt', 'VB')
[1, ('s', 'NNS')]
[1, ('apart', 'NN')]
('attempt', 'VB')
[1, ('s', 'NNS')]
[1, ('video', 'NN')]
('attempt', 'VB')
[1, ('s', 'NNS')]
[1, ('game', 'NN')]
('attempt', 'VB')
[1, ('QOL', 'NNP')]
[1, ('area', 'NN')]
('attempt', 'VB')
[1, ('QOL', 'NNP')]
[1, ('apart', 'NN')]
('attempt', 'VB')
[1, ('QOL', 'NNP')]
[1, ('video', 'NN')]
('attempt', 'VB')
[1, ('QOL', 'NNP')]
[1, ('game', 'NN')]
('attempt', 'VB')
[1, ('ways', 'NNS')]
[1, ('area', 'NN')]
('attempt', 'VB')
[1, ('ways', 'NNS')]
[1, ('apart', 'NN')]
('attempt', 'VB')
[1, ('ways', 'NNS')]
[1, ('video', 'NN')]
('attempt', 'VB')
[1, ('ways', 'NNS')]
[1, ('game', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('area', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('apart', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('video', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('game', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('area', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('apart', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('video', 'NN')]
('attempt', 'VB')
[1, ('business', 'NN')]
[1, ('game', 'NN')]
('attempt', 'VB')
[2, ('platform', 'NN')]
[2, ('area', 'NN')]
('establish', 'VB')
[2, ('platform', 'NN')]
[2, ('apart', 'NN')]
('establish', 'VB')
[2, ('platform', 'NN')]
[2, ('video', 'NN')]
('establish', 'VB')
[2, ('platform', 'NN')]
[2, ('game', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('area', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('apart', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('video', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('game', 'NN')]
('establish', 'VB')
[2, ('people', 'NNS')]
[2, ('area', 'NN')]
('establish', 'VB')
[2, ('people', 'NNS')]
[2, ('apart', 'NN')]
('establish', 'VB')
[2, ('people', 'NNS')]
[2, ('video', 'NN')]
('establish', 'VB')
[2, ('people', 'NNS')]
[2, ('game', 'NN')]
('establish', 'VB')
[2, ('s', 'NNS')]
[2, ('area', 'NN')]
('establish', 'VB')
[2, ('s', 'NNS')]
[2, ('apart', 'NN')]
('establish', 'VB')
[2, ('s', 'NNS')]
[2, ('video', 'NN')]
('establish', 'VB')
[2, ('s', 'NNS')]
[2, ('game', 'NN')]
('establish', 'VB')
[2, ('QOL', 'NNP')]
[2, ('area', 'NN')]
('establish', 'VB')
[2, ('QOL', 'NNP')]
[2, ('apart', 'NN')]
('establish', 'VB')
[2, ('QOL', 'NNP')]
[2, ('video', 'NN')]
('establish', 'VB')
[2, ('QOL', 'NNP')]
[2, ('game', 'NN')]
('establish', 'VB')
[2, ('ways', 'NNS')]
[2, ('area', 'NN')]
('establish', 'VB')
[2, ('ways', 'NNS')]
[2, ('apart', 'NN')]
('establish', 'VB')
[2, ('ways', 'NNS')]
[2, ('video', 'NN')]
('establish', 'VB')
[2, ('ways', 'NNS')]
[2, ('game', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('area', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('apart', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('video', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('game', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('area', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('apart', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('video', 'NN')]
('establish', 'VB')
[2, ('business', 'NN')]
[2, ('game', 'NN')]
('establish', 'VB')
[3, ('platform', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('platform', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('people', 'NNS')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('people', 'NNS')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('s', 'NNS')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('s', 'NNS')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('QOL', 'NNP')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('QOL', 'NNP')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('ways', 'NNS')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('ways', 'NNS')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('area', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('area', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('apart', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('apart', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('video', 'NN')]
('dedicated', 'VBN')
[3, ('business', 'NN')]
[3, ('game', 'NN')]
('dedicated', 'VBN')
[2, ('health', 'NN')]
[2, ('strength', 'NN')]
('try', 'VB')
[2, ('health', 'NN')]
[2, ('entertainment', 'NN')]
('try', 'VB')
[2, ('health', 'NN')]
[2, ('company', 'NN')]
('try', 'VB')
[2, ('health', 'NN')]
[2, ('approaches', 'NNS')]
('try', 'VB')
[2, ('health', 'NN')]
[2, ('expand', 'NN')]
('try', 'VB')
[2, ('health', 'NN')]
[2, ('business', 'NN')]
('try', 'VB')
[2, ('theme', 'NN')]
[2, ('strength', 'NN')]
('try', 'VB')
[2, ('theme', 'NN')]
[2, ('entertainment', 'NN')]
('try', 'VB')
[2, ('theme', 'NN')]
[2, ('company', 'NN')]
('try', 'VB')
[2, ('theme', 'NN')]
[2, ('approaches', 'NNS')]
('try', 'VB')
[2, ('theme', 'NN')]
[2, ('expand', 'NN')]
('try', 'VB')
[2, ('theme', 'NN')]
[2, ('business', 'NN')]
('try', 'VB')
[2, ('step', 'NN')]
[2, ('strength', 'NN')]
('try', 'VB')
[2, ('step', 'NN')]
[2, ('entertainment', 'NN')]
('try', 'VB')
[2, ('step', 'NN')]
[2, ('company', 'NN')]
('try', 'VB')
[2, ('step', 'NN')]
[2, ('approaches', 'NNS')]
('try', 'VB')
[2, ('step', 'NN')]
[2, ('expand', 'NN')]
('try', 'VB')
[2, ('step', 'NN')]
[2, ('business', 'NN')]
('try', 'VB')
[3, ('health', 'NN')]
[3, ('strength', 'NN')]
('use', 'VB')
[3, ('health', 'NN')]
[3, ('entertainment', 'NN')]
('use', 'VB')
[3, ('health', 'NN')]
[3, ('company', 'NN')]
('use', 'VB')
[3, ('health', 'NN')]
[3, ('approaches', 'NNS')]
('use', 'VB')
[3, ('health', 'NN')]
[3, ('expand', 'NN')]
('use', 'VB')
[3, ('health', 'NN')]
[3, ('business', 'NN')]
('use', 'VB')
[3, ('theme', 'NN')]
[3, ('strength', 'NN')]
('use', 'VB')
[3, ('theme', 'NN')]
[3, ('entertainment', 'NN')]
('use', 'VB')
[3, ('theme', 'NN')]
[3, ('company', 'NN')]
('use', 'VB')
[3, ('theme', 'NN')]
[3, ('approaches', 'NNS')]
('use', 'VB')
[3, ('theme', 'NN')]
[3, ('expand', 'NN')]
('use', 'VB')
[3, ('theme', 'NN')]
[3, ('business', 'NN')]
('use', 'VB')
[3, ('step', 'NN')]
[3, ('strength', 'NN')]
('use', 'VB')
[3, ('step', 'NN')]
[3, ('entertainment', 'NN')]
('use', 'VB')
[3, ('step', 'NN')]
[3, ('company', 'NN')]
('use', 'VB')
[3, ('step', 'NN')]
[3, ('approaches', 'NNS')]
('use', 'VB')
[3, ('step', 'NN')]
[3, ('expand', 'NN')]
('use', 'VB')
[3, ('step', 'NN')]
[3, ('business', 'NN')]
('use', 'VB')
[4, ('health', 'NN')]
[4, ('approaches', 'NNS')]
('create', 'VB')
[4, ('health', 'NN')]
[4, ('expand', 'NN')]
('create', 'VB')
[4, ('health', 'NN')]
[4, ('business', 'NN')]
('create', 'VB')
[4, ('theme', 'NN')]
[4, ('approaches', 'NNS')]
('create', 'VB')
[4, ('theme', 'NN')]
[4, ('expand', 'NN')]
('create', 'VB')
[4, ('theme', 'NN')]
[4, ('business', 'NN')]
('create', 'VB')
[4, ('step', 'NN')]
[4, ('approaches', 'NNS')]
('create', 'VB')
[4, ('step', 'NN')]
[4, ('expand', 'NN')]
('create', 'VB')
[4, ('step', 'NN')]
[4, ('business', 'NN')]
('create', 'VB')
[4, ('strength', 'NN')]
[4, ('approaches', 'NNS')]
('create', 'VB')
[4, ('strength', 'NN')]
[4, ('expand', 'NN')]
('create', 'VB')
[4, ('strength', 'NN')]
[4, ('business', 'NN')]
('create', 'VB')
[4, ('entertainment', 'NN')]
[4, ('approaches', 'NNS')]
('create', 'VB')
[4, ('entertainment', 'NN')]
[4, ('expand', 'NN')]
('create', 'VB')
[4, ('entertainment', 'NN')]
[4, ('business', 'NN')]
('create', 'VB')
[4, ('company', 'NN')]
[4, ('approaches', 'NNS')]
('create', 'VB')
[4, ('company', 'NN')]
[4, ('expand', 'NN')]
('create', 'VB')
[4, ('company', 'NN')]
[4, ('business', 'NN')]
('create', 'VB')
[0, ('endeavors', 'NNS')]
[0, ('platform', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('strategy', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('user', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('base', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('environment', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('people', 'NNS')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('health', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('turn', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('expand', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('Nintendo', 'NNP')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('user', 'NN')]
('improving', 'VBG')
[0, ('endeavors', 'NNS')]
[0, ('base', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('platform', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('strategy', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('user', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('base', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('environment', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('people', 'NNS')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('health', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('turn', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('expand', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('Nintendo', 'NNP')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('user', 'NN')]
('improving', 'VBG')
[0, ('QOL', 'NNP')]
[0, ('base', 'NN')]
('improving', 'VBG')
[1, ('endeavors', 'NNS')]
[1, ('strategy', 'NN')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('user', 'NN')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('base', 'NN')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('environment', 'NN')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('people', 'NNS')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('health', 'NN')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('turn', 'NN')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('expand', 'NN')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('Nintendo', 'NNP')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('user', 'NN')]
('strive', 'VBP')
[1, ('endeavors', 'NNS')]
[1, ('base', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('strategy', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('user', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('base', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('environment', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('people', 'NNS')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('health', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('turn', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('expand', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('Nintendo', 'NNP')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('user', 'NN')]
('strive', 'VBP')
[1, ('QOL', 'NNP')]
[1, ('base', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('strategy', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('user', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('base', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('environment', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('people', 'NNS')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('health', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('turn', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('expand', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('Nintendo', 'NNP')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('user', 'NN')]
('strive', 'VBP')
[1, ('platform', 'NN')]
[1, ('base', 'NN')]
('strive', 'VBP')
[2, ('endeavors', 'NNS')]
[2, ('strategy', 'NN')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('user', 'NN')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('base', 'NN')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('environment', 'NN')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('people', 'NNS')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('health', 'NN')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('turn', 'NN')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('expand', 'NN')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('Nintendo', 'NNP')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('user', 'NN')]
('promote', 'VB')
[2, ('endeavors', 'NNS')]
[2, ('base', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('strategy', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('user', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('base', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('environment', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('people', 'NNS')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('health', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('turn', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('expand', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('Nintendo', 'NNP')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('user', 'NN')]
('promote', 'VB')
[2, ('QOL', 'NNP')]
[2, ('base', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('strategy', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('user', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('base', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('environment', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('people', 'NNS')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('health', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('turn', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('expand', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('Nintendo', 'NNP')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('user', 'NN')]
('promote', 'VB')
[2, ('platform', 'NN')]
[2, ('base', 'NN')]
('promote', 'VB')
[3, ('endeavors', 'NNS')]
[3, ('strategy', 'NN')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('user', 'NN')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('base', 'NN')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('environment', 'NN')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('people', 'NNS')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('health', 'NN')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('turn', 'NN')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('expand', 'NN')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('Nintendo', 'NNP')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('user', 'NN')]
('existing', 'VBG')
[3, ('endeavors', 'NNS')]
[3, ('base', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('strategy', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('user', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('base', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('environment', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('people', 'NNS')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('health', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('turn', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('expand', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('Nintendo', 'NNP')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('user', 'NN')]
('existing', 'VBG')
[3, ('QOL', 'NNP')]
[3, ('base', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('strategy', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('user', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('base', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('environment', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('people', 'NNS')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('health', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('turn', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('expand', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('Nintendo', 'NNP')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('user', 'NN')]
('existing', 'VBG')
[3, ('platform', 'NN')]
[3, ('base', 'NN')]
('existing', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('user', 'NN')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('base', 'NN')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('environment', 'NN')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('people', 'NNS')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('health', 'NN')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('turn', 'NN')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('expand', 'NN')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('Nintendo', 'NNP')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('user', 'NN')]
('expanding', 'VBG')
[4, ('endeavors', 'NNS')]
[4, ('base', 'NN')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('user', 'NN')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('base', 'NN')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('environment', 'NN')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('people', 'NNS')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('health', 'NN')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('turn', 'NN')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('expand', 'NN')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('Nintendo', 'NNP')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('user', 'NN')]
('expanding', 'VBG')
[4, ('QOL', 'NNP')]
[4, ('base', 'NN')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('user', 'NN')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('base', 'NN')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('environment', 'NN')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('people', 'NNS')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('health', 'NN')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('turn', 'NN')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('expand', 'NN')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('Nintendo', 'NNP')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('user', 'NN')]
('expanding', 'VBG')
[4, ('platform', 'NN')]
[4, ('base', 'NN')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('user', 'NN')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('base', 'NN')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('environment', 'NN')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('people', 'NNS')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('health', 'NN')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('turn', 'NN')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('expand', 'NN')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('Nintendo', 'NNP')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('user', 'NN')]
('expanding', 'VBG')
[4, ('strategy', 'NN')]
[4, ('base', 'NN')]
('expanding', 'VBG')
[5, ('endeavors', 'NNS')]
[5, ('environment', 'NN')]
('create', 'VB')
[5, ('endeavors', 'NNS')]
[5, ('people', 'NNS')]
('create', 'VB')
[5, ('endeavors', 'NNS')]
[5, ('health', 'NN')]
('create', 'VB')
[5, ('endeavors', 'NNS')]
[5, ('turn', 'NN')]
('create', 'VB')
[5, ('endeavors', 'NNS')]
[5, ('expand', 'NN')]
('create', 'VB')
[5, ('endeavors', 'NNS')]
[5, ('Nintendo', 'NNP')]
('create', 'VB')
[5, ('QOL', 'NNP')]
[5, ('environment', 'NN')]
('create', 'VB')
[5, ('QOL', 'NNP')]
[5, ('people', 'NNS')]
('create', 'VB')
[5, ('QOL', 'NNP')]
[5, ('health', 'NN')]
('create', 'VB')
[5, ('QOL', 'NNP')]
[5, ('turn', 'NN')]
('create', 'VB')
[5, ('QOL', 'NNP')]
[5, ('expand', 'NN')]
('create', 'VB')
[5, ('QOL', 'NNP')]
[5, ('Nintendo', 'NNP')]
('create', 'VB')
[5, ('platform', 'NN')]
[5, ('environment', 'NN')]
('create', 'VB')
[5, ('platform', 'NN')]
[5, ('people', 'NNS')]
('create', 'VB')
[5, ('platform', 'NN')]
[5, ('health', 'NN')]
('create', 'VB')
[5, ('platform', 'NN')]
[5, ('turn', 'NN')]
('create', 'VB')
[5, ('platform', 'NN')]
[5, ('expand', 'NN')]
('create', 'VB')
[5, ('platform', 'NN')]
[5, ('Nintendo', 'NNP')]
('create', 'VB')
[5, ('strategy', 'NN')]
[5, ('environment', 'NN')]
('create', 'VB')
[5, ('strategy', 'NN')]
[5, ('people', 'NNS')]
('create', 'VB')
[5, ('strategy', 'NN')]
[5, ('health', 'NN')]
('create', 'VB')
[5, ('strategy', 'NN')]
[5, ('turn', 'NN')]
('create', 'VB')
[5, ('strategy', 'NN')]
[5, ('expand', 'NN')]
('create', 'VB')
[5, ('strategy', 'NN')]
[5, ('Nintendo', 'NNP')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('environment', 'NN')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('people', 'NNS')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('health', 'NN')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('turn', 'NN')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('expand', 'NN')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('Nintendo', 'NNP')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('environment', 'NN')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('people', 'NNS')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('health', 'NN')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('turn', 'NN')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('expand', 'NN')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('Nintendo', 'NNP')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('environment', 'NN')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('people', 'NNS')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('health', 'NN')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('turn', 'NN')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('expand', 'NN')]
('create', 'VB')
[5, ('user', 'NN')]
[5, ('Nintendo', 'NNP')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('environment', 'NN')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('people', 'NNS')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('health', 'NN')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('turn', 'NN')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('expand', 'NN')]
('create', 'VB')
[5, ('base', 'NN')]
[5, ('Nintendo', 'NNP')]
('create', 'VB')
[6, ('endeavors', 'NNS')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('endeavors', 'NNS')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('endeavors', 'NNS')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('endeavors', 'NNS')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('QOL', 'NNP')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('QOL', 'NNP')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('QOL', 'NNP')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('QOL', 'NNP')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('platform', 'NN')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('platform', 'NN')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('platform', 'NN')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('platform', 'NN')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('strategy', 'NN')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('strategy', 'NN')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('strategy', 'NN')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('strategy', 'NN')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('user', 'NN')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('user', 'NN')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('user', 'NN')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('user', 'NN')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('base', 'NN')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('base', 'NN')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('base', 'NN')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('base', 'NN')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('environment', 'NN')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('environment', 'NN')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('environment', 'NN')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('environment', 'NN')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('people', 'NNS')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('people', 'NNS')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('people', 'NNS')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('people', 'NNS')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('user', 'NN')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('user', 'NN')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('user', 'NN')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('user', 'NN')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[6, ('base', 'NN')]
[6, ('health', 'NN')]
('are', 'VBP')
[6, ('base', 'NN')]
[6, ('turn', 'NN')]
('are', 'VBP')
[6, ('base', 'NN')]
[6, ('expand', 'NN')]
('are', 'VBP')
[6, ('base', 'NN')]
[6, ('Nintendo', 'NNP')]
('are', 'VBP')
[0, ('Nintendo', 'NNP')]
[0, ('manufacture', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('sale', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('Hanafuda', 'NNP')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('(', 'NNP')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('playing', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('cards', 'NNS')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('years', 'NNS')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('playing', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('card', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('company', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('toy', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('company', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('toy', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('company', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('toy', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('company', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('toy', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('company', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('company', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('video', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('game', 'NN')]
('started', 'VBD')
[0, ('Nintendo', 'NNP')]
[0, ('platforms', 'NNS')]
('started', 'VBD')
[1, ('Nintendo', 'NNP')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('manufacture', 'NN')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('sale', 'NN')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('Hanafuda', 'NNP')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('(', 'NNP')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('cards', 'NNS')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('years', 'NNS')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('card', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('toy', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('company', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('video', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('game', 'NN')]
('has', 'VBZ')
[1, ('playing', 'NN')]
[1, ('platforms', 'NNS')]
('has', 'VBZ')
[2, ('Nintendo', 'NNP')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('manufacture', 'NN')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('sale', 'NN')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('Hanafuda', 'NNP')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('(', 'NNP')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('cards', 'NNS')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('years', 'NNS')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('card', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('toy', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('company', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('video', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('game', 'NN')]
('innovated', 'VBN')
[2, ('playing', 'NN')]
[2, ('platforms', 'NNS')]
('innovated', 'VBN')
[3, ('Nintendo', 'NNP')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('Nintendo', 'NNP')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('Nintendo', 'NNP')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('manufacture', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('manufacture', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('manufacture', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('sale', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('sale', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('sale', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('Hanafuda', 'NNP')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('Hanafuda', 'NNP')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('Hanafuda', 'NNP')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('(', 'NNP')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('(', 'NNP')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('(', 'NNP')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('playing', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('playing', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('playing', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('cards', 'NNS')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('cards', 'NNS')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('cards', 'NNS')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('years', 'NNS')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('years', 'NNS')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('years', 'NNS')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('playing', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('playing', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('playing', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('card', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('card', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('card', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('toy', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('video', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('game', 'NN')]
('developing', 'VBG')
[3, ('company', 'NN')]
[3, ('platforms', 'NNS')]
('developing', 'VBG')
[0, ('Nintendo', 'NNP')]
[0, ('try', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('things', 'NNS')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('history', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('failures', 'NNS')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('successes', 'NNS')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('pioneer', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('home', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('video', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('game', 'NN')]
('has', 'VBZ')
[0, ('Nintendo', 'NNP')]
[0, ('market', 'NN')]
('has', 'VBZ')
[1, ('Nintendo', 'NNP')]
[1, ('try', 'NN')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('things', 'NNS')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('history', 'NN')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('failures', 'NNS')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('successes', 'NNS')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('pioneer', 'NN')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('home', 'NN')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('video', 'NN')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('game', 'NN')]
('continued', 'VBN')
[1, ('Nintendo', 'NNP')]
[1, ('market', 'NN')]
('continued', 'VBN')
[2, ('Nintendo', 'NNP')]
[2, ('failures', 'NNS')]
('experiencing', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('successes', 'NNS')]
('experiencing', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('pioneer', 'NN')]
('experiencing', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('home', 'NN')]
('experiencing', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('video', 'NN')]
('experiencing', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('game', 'NN')]
('experiencing', 'VBG')
[2, ('Nintendo', 'NNP')]
[2, ('market', 'NN')]
('experiencing', 'VBG')
[2, ('try', 'NN')]
[2, ('failures', 'NNS')]
('experiencing', 'VBG')
[2, ('try', 'NN')]
[2, ('successes', 'NNS')]
('experiencing', 'VBG')
[2, ('try', 'NN')]
[2, ('pioneer', 'NN')]
('experiencing', 'VBG')
[2, ('try', 'NN')]
[2, ('home', 'NN')]
('experiencing', 'VBG')
[2, ('try', 'NN')]
[2, ('video', 'NN')]
('experiencing', 'VBG')
[2, ('try', 'NN')]
[2, ('game', 'NN')]
('experiencing', 'VBG')
[2, ('try', 'NN')]
[2, ('market', 'NN')]
('experiencing', 'VBG')
[2, ('things', 'NNS')]
[2, ('failures', 'NNS')]
('experiencing', 'VBG')
[2, ('things', 'NNS')]
[2, ('successes', 'NNS')]
('experiencing', 'VBG')
[2, ('things', 'NNS')]
[2, ('pioneer', 'NN')]
('experiencing', 'VBG')
[2, ('things', 'NNS')]
[2, ('home', 'NN')]
('experiencing', 'VBG')
[2, ('things', 'NNS')]
[2, ('video', 'NN')]
('experiencing', 'VBG')
[2, ('things', 'NNS')]
[2, ('game', 'NN')]
('experiencing', 'VBG')
[2, ('things', 'NNS')]
[2, ('market', 'NN')]
('experiencing', 'VBG')
[2, ('history', 'NN')]
[2, ('failures', 'NNS')]
('experiencing', 'VBG')
[2, ('history', 'NN')]
[2, ('successes', 'NNS')]
('experiencing', 'VBG')
[2, ('history', 'NN')]
[2, ('pioneer', 'NN')]
('experiencing', 'VBG')
[2, ('history', 'NN')]
[2, ('home', 'NN')]
('experiencing', 'VBG')
[2, ('history', 'NN')]
[2, ('video', 'NN')]
('experiencing', 'VBG')
[2, ('history', 'NN')]
[2, ('game', 'NN')]
('experiencing', 'VBG')
[2, ('history', 'NN')]
[2, ('market', 'NN')]
('experiencing', 'VBG')
[3, ('Nintendo', 'NNP')]
[3, ('pioneer', 'NN')]
('managed', 'VBD')
[3, ('Nintendo', 'NNP')]
[3, ('home', 'NN')]
('managed', 'VBD')
[3, ('Nintendo', 'NNP')]
[3, ('video', 'NN')]
('managed', 'VBD')
[3, ('Nintendo', 'NNP')]
[3, ('game', 'NN')]
('managed', 'VBD')
[3, ('Nintendo', 'NNP')]
[3, ('market', 'NN')]
('managed', 'VBD')
[3, ('try', 'NN')]
[3, ('pioneer', 'NN')]
('managed', 'VBD')
[3, ('try', 'NN')]
[3, ('home', 'NN')]
('managed', 'VBD')
[3, ('try', 'NN')]
[3, ('video', 'NN')]
('managed', 'VBD')
[3, ('try', 'NN')]
[3, ('game', 'NN')]
('managed', 'VBD')
[3, ('try', 'NN')]
[3, ('market', 'NN')]
('managed', 'VBD')
[3, ('things', 'NNS')]
[3, ('pioneer', 'NN')]
('managed', 'VBD')
[3, ('things', 'NNS')]
[3, ('home', 'NN')]
('managed', 'VBD')
[3, ('things', 'NNS')]
[3, ('video', 'NN')]
('managed', 'VBD')
[3, ('things', 'NNS')]
[3, ('game', 'NN')]
('managed', 'VBD')
[3, ('things', 'NNS')]
[3, ('market', 'NN')]
('managed', 'VBD')
[3, ('history', 'NN')]
[3, ('pioneer', 'NN')]
('managed', 'VBD')
[3, ('history', 'NN')]
[3, ('home', 'NN')]
('managed', 'VBD')
[3, ('history', 'NN')]
[3, ('video', 'NN')]
('managed', 'VBD')
[3, ('history', 'NN')]
[3, ('game', 'NN')]
('managed', 'VBD')
[3, ('history', 'NN')]
[3, ('market', 'NN')]
('managed', 'VBD')
[3, ('failures', 'NNS')]
[3, ('pioneer', 'NN')]
('managed', 'VBD')
[3, ('failures', 'NNS')]
[3, ('home', 'NN')]
('managed', 'VBD')
[3, ('failures', 'NNS')]
[3, ('video', 'NN')]
('managed', 'VBD')
[3, ('failures', 'NNS')]
[3, ('game', 'NN')]
('managed', 'VBD')
[3, ('failures', 'NNS')]
[3, ('market', 'NN')]
('managed', 'VBD')
[3, ('successes', 'NNS')]
[3, ('pioneer', 'NN')]
('managed', 'VBD')
[3, ('successes', 'NNS')]
[3, ('home', 'NN')]
('managed', 'VBD')
[3, ('successes', 'NNS')]
[3, ('video', 'NN')]
('managed', 'VBD')
[3, ('successes', 'NNS')]
[3, ('game', 'NN')]
('managed', 'VBD')
[3, ('successes', 'NNS')]
[3, ('market', 'NN')]
('managed', 'VBD')
[6, ('something', 'NN')]
[6, ('people', 'NNS')]
('improve', 'VB')
[6, ('something', 'NN')]
[6, ('s', 'NNS')]
('improve', 'VB')
[6, ('something', 'NN')]
[6, ('QOL', 'NNP')]
('improve', 'VB')
[6, ('something', 'NN')]
[6, ('ways', 'NNS')]
('improve', 'VB')
[6, ('materials', 'NNS')]
[6, ('people', 'NNS')]
('improve', 'VB')
[6, ('materials', 'NNS')]
[6, ('s', 'NNS')]
('improve', 'VB')
[6, ('materials', 'NNS')]
[6, ('QOL', 'NNP')]
('improve', 'VB')
[6, ('materials', 'NNS')]
[6, ('ways', 'NNS')]
('improve', 'VB')
[6, ('technologies', 'NNS')]
[6, ('people', 'NNS')]
('improve', 'VB')
[6, ('technologies', 'NNS')]
[6, ('s', 'NNS')]
('improve', 'VB')
[6, ('technologies', 'NNS')]
[6, ('QOL', 'NNP')]
('improve', 'VB')
[6, ('technologies', 'NNS')]
[6, ('ways', 'NNS')]
('improve', 'VB')
[6, ('time', 'NN')]
[6, ('people', 'NNS')]
('improve', 'VB')
[6, ('time', 'NN')]
[6, ('s', 'NNS')]
('improve', 'VB')
[6, ('time', 'NN')]
[6, ('QOL', 'NNP')]
('improve', 'VB')
[6, ('time', 'NN')]
[6, ('ways', 'NNS')]
('improve', 'VB')
[6, ('position', 'NN')]
[6, ('people', 'NNS')]
('improve', 'VB')
[6, ('position', 'NN')]
[6, ('s', 'NNS')]
('improve', 'VB')
[6, ('position', 'NN')]
[6, ('QOL', 'NNP')]
('improve', 'VB')
[6, ('position', 'NN')]
[6, ('ways', 'NNS')]
('improve', 'VB')
[6, ('entertainment', 'NN')]
[6, ('people', 'NNS')]
('improve', 'VB')
[6, ('entertainment', 'NN')]
[6, ('s', 'NNS')]
('improve', 'VB')
[6, ('entertainment', 'NN')]
[6, ('QOL', 'NNP')]
('improve', 'VB')
[6, ('entertainment', 'NN')]
[6, ('ways', 'NNS')]
('improve', 'VB')
[6, ('core', 'NN')]
[6, ('people', 'NNS')]
('improve', 'VB')
[6, ('core', 'NN')]
[6, ('s', 'NNS')]
('improve', 'VB')
[6, ('core', 'NN')]
[6, ('QOL', 'NNP')]
('improve', 'VB')
[6, ('core', 'NN')]
[6, ('ways', 'NNS')]
('improve', 'VB')
[6, ('business', 'NN')]
[6, ('people', 'NNS')]
('improve', 'VB')
[6, ('business', 'NN')]
[6, ('s', 'NNS')]
('improve', 'VB')
[6, ('business', 'NN')]
[6, ('QOL', 'NNP')]
('improve', 'VB')
[6, ('business', 'NN')]
[6, ('ways', 'NNS')]
('improve', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('progress', 'NN')]
('make', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('support', 'NN')]
('make', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('encouragement', 'NN')]
('make', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('shareholders', 'NNS')]
('make', 'VB')
[0, ('Nintendo', 'NNP')]
[0, ('investors', 'NNS')]
('make', 'VB')
[0, ('intends', 'NNS')]
[0, ('progress', 'NN')]
('make', 'VB')
[0, ('intends', 'NNS')]
[0, ('support', 'NN')]
('make', 'VB')
[0, ('intends', 'NNS')]
[0, ('encouragement', 'NN')]
('make', 'VB')
[0, ('intends', 'NNS')]
[0, ('shareholders', 'NNS')]
('make', 'VB')
[0, ('intends', 'NNS')]
[0, ('investors', 'NNS')]
('make', 'VB')
>>> ================================ RESTART ================================
>>> 
>>> import Summarizer as summe
>>> summe.getSentences("""	Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration. In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.

	With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience. In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas. What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.

	We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus. We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.

	With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business. We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business. Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.

	After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms. Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market. What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways. We will continue to value self-innovation in line with the times and aim for growth.

	Nintendo intends to make progress with the support and encouragement of its shareholders and investors.""")
en Since the launch of the Nintendo Entertainment System in 1983, Nintendo has been offering the world unique and original entertainment products under the development concept of hardware and software integration.
en In the field of home entertainment, the video game industry is one of the few industries established in Japan that spread around the world, and Nintendo has established itself as a well-known brand truly representing video game culture throughout the world.
en With the belief that the raison d'etre of entertainment is to put smiles on people's faces around the world through products and services, what we have focused on for the last decade is our basic strategy of expanding the gaming population by offering products which can be enjoyed by everyone regardless of age, gender or gaming experience.
en In addition, as the business environment around us has shifted with the times, we have decided to redefine entertainment as something that improves people's quality of life ("QOL") in enjoyable ways and expand our business areas.
en What Nintendo will try to achieve in the next 10 years is a platform business that improves people's QOL in enjoyable ways.
en We believe that we can capitalize the most on our strengths through a hardware-software integrated platform business, and therefore this type of dedicated video game platforms will remain our core focus.
en We will continue to value the spirit of originality described in our motto "The True Value of Entertainment Lies in Individuality," and will continue to provide products and services which pleasantly surprise people.
en With a platform business that improves people's QOL in enjoyable ways, we will attempt to establish a new business area apart from our dedicated video game business.
en We have set "health" as the theme for our first step and we will try to use our strength as an entertainment company to create unique approaches that expand this business.
en Through our new endeavors with the QOL-improving platform, we strive to further promote our existing strategy of expanding our user base, create an environment in which more people are conscious about their health and in turn expand Nintendo's overall user base.
en After Nintendo started the manufacture and sale of Hanafuda (traditional Japanese playing cards) 125 years ago, it has innovated itself from a playing card company to a toy company, a toy company to an electronic toy company and finally from an electronic toy company to a company developing video game platforms.
en Nintendo has continued to try new things, and with a history of experiencing many failures and small successes, we managed to pioneer the home video game market.
en What has remained the same from the past is that we have always tried to create something new from materials and technologies available at that time, to position entertainment as our core business and to improve people's QOL in enjoyable ways.
en We will continue to value self-innovation in line with the times and aim for growth.
en Nintendo intends to make progress with the support and encouragement of its shareholders and investors.
>>> summe.doGet()
>>> for dem in summe.sentences:
	for svo in dem[5]:
		print(svo.subj)
		print(svo.verb)
		print(svo.obj)

		
('launch', 'NN')
('has', 'VBZ')
('world', 'NN')
('launch', 'NN')
('has', 'VBZ')
('unique', 'NN')
('launch', 'NN')
('has', 'VBZ')
('entertainment', 'NN')
('launch', 'NN')
('has', 'VBZ')
('products', 'NNS')
('launch', 'NN')
('has', 'VBZ')
('development', 'NN')
('launch', 'NN')
('has', 'VBZ')
('concept', 'NN')
('launch', 'NN')
('has', 'VBZ')
('hardware', 'NN')
('launch', 'NN')
('has', 'VBZ')
('software', 'NN')
('launch', 'NN')
('has', 'VBZ')
('integration', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('world', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('unique', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('entertainment', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('products', 'NNS')
('Nintendo', 'NNP')
('has', 'VBZ')
('development', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('concept', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('hardware', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('software', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('integration', 'NN')
('Entertainment', 'NNP')
('has', 'VBZ')
('world', 'NN')
('Entertainment', 'NNP')
('has', 'VBZ')
('unique', 'NN')
('Entertainment', 'NNP')
('has', 'VBZ')
('entertainment', 'NN')
('Entertainment', 'NNP')
('has', 'VBZ')
('products', 'NNS')
('Entertainment', 'NNP')
('has', 'VBZ')
('development', 'NN')
('Entertainment', 'NNP')
('has', 'VBZ')
('concept', 'NN')
('Entertainment', 'NNP')
('has', 'VBZ')
('hardware', 'NN')
('Entertainment', 'NNP')
('has', 'VBZ')
('software', 'NN')
('Entertainment', 'NNP')
('has', 'VBZ')
('integration', 'NN')
('System', 'NNP')
('has', 'VBZ')
('world', 'NN')
('System', 'NNP')
('has', 'VBZ')
('unique', 'NN')
('System', 'NNP')
('has', 'VBZ')
('entertainment', 'NN')
('System', 'NNP')
('has', 'VBZ')
('products', 'NNS')
('System', 'NNP')
('has', 'VBZ')
('development', 'NN')
('System', 'NNP')
('has', 'VBZ')
('concept', 'NN')
('System', 'NNP')
('has', 'VBZ')
('hardware', 'NN')
('System', 'NNP')
('has', 'VBZ')
('software', 'NN')
('System', 'NNP')
('has', 'VBZ')
('integration', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('world', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('unique', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('entertainment', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('products', 'NNS')
('Nintendo', 'NNP')
('has', 'VBZ')
('development', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('concept', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('hardware', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('software', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('integration', 'NN')
('launch', 'NN')
('been', 'VBN')
('world', 'NN')
('launch', 'NN')
('been', 'VBN')
('unique', 'NN')
('launch', 'NN')
('been', 'VBN')
('entertainment', 'NN')
('launch', 'NN')
('been', 'VBN')
('products', 'NNS')
('launch', 'NN')
('been', 'VBN')
('development', 'NN')
('launch', 'NN')
('been', 'VBN')
('concept', 'NN')
('launch', 'NN')
('been', 'VBN')
('hardware', 'NN')
('launch', 'NN')
('been', 'VBN')
('software', 'NN')
('launch', 'NN')
('been', 'VBN')
('integration', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('world', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('unique', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('entertainment', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('products', 'NNS')
('Nintendo', 'NNP')
('been', 'VBN')
('development', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('concept', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('hardware', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('software', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('integration', 'NN')
('Entertainment', 'NNP')
('been', 'VBN')
('world', 'NN')
('Entertainment', 'NNP')
('been', 'VBN')
('unique', 'NN')
('Entertainment', 'NNP')
('been', 'VBN')
('entertainment', 'NN')
('Entertainment', 'NNP')
('been', 'VBN')
('products', 'NNS')
('Entertainment', 'NNP')
('been', 'VBN')
('development', 'NN')
('Entertainment', 'NNP')
('been', 'VBN')
('concept', 'NN')
('Entertainment', 'NNP')
('been', 'VBN')
('hardware', 'NN')
('Entertainment', 'NNP')
('been', 'VBN')
('software', 'NN')
('Entertainment', 'NNP')
('been', 'VBN')
('integration', 'NN')
('System', 'NNP')
('been', 'VBN')
('world', 'NN')
('System', 'NNP')
('been', 'VBN')
('unique', 'NN')
('System', 'NNP')
('been', 'VBN')
('entertainment', 'NN')
('System', 'NNP')
('been', 'VBN')
('products', 'NNS')
('System', 'NNP')
('been', 'VBN')
('development', 'NN')
('System', 'NNP')
('been', 'VBN')
('concept', 'NN')
('System', 'NNP')
('been', 'VBN')
('hardware', 'NN')
('System', 'NNP')
('been', 'VBN')
('software', 'NN')
('System', 'NNP')
('been', 'VBN')
('integration', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('world', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('unique', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('entertainment', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('products', 'NNS')
('Nintendo', 'NNP')
('been', 'VBN')
('development', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('concept', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('hardware', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('software', 'NN')
('Nintendo', 'NNP')
('been', 'VBN')
('integration', 'NN')
('launch', 'NN')
('offering', 'VBG')
('world', 'NN')
('launch', 'NN')
('offering', 'VBG')
('unique', 'NN')
('launch', 'NN')
('offering', 'VBG')
('entertainment', 'NN')
('launch', 'NN')
('offering', 'VBG')
('products', 'NNS')
('launch', 'NN')
('offering', 'VBG')
('development', 'NN')
('launch', 'NN')
('offering', 'VBG')
('concept', 'NN')
('launch', 'NN')
('offering', 'VBG')
('hardware', 'NN')
('launch', 'NN')
('offering', 'VBG')
('software', 'NN')
('launch', 'NN')
('offering', 'VBG')
('integration', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('world', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('unique', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('entertainment', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('products', 'NNS')
('Nintendo', 'NNP')
('offering', 'VBG')
('development', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('concept', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('hardware', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('software', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('integration', 'NN')
('Entertainment', 'NNP')
('offering', 'VBG')
('world', 'NN')
('Entertainment', 'NNP')
('offering', 'VBG')
('unique', 'NN')
('Entertainment', 'NNP')
('offering', 'VBG')
('entertainment', 'NN')
('Entertainment', 'NNP')
('offering', 'VBG')
('products', 'NNS')
('Entertainment', 'NNP')
('offering', 'VBG')
('development', 'NN')
('Entertainment', 'NNP')
('offering', 'VBG')
('concept', 'NN')
('Entertainment', 'NNP')
('offering', 'VBG')
('hardware', 'NN')
('Entertainment', 'NNP')
('offering', 'VBG')
('software', 'NN')
('Entertainment', 'NNP')
('offering', 'VBG')
('integration', 'NN')
('System', 'NNP')
('offering', 'VBG')
('world', 'NN')
('System', 'NNP')
('offering', 'VBG')
('unique', 'NN')
('System', 'NNP')
('offering', 'VBG')
('entertainment', 'NN')
('System', 'NNP')
('offering', 'VBG')
('products', 'NNS')
('System', 'NNP')
('offering', 'VBG')
('development', 'NN')
('System', 'NNP')
('offering', 'VBG')
('concept', 'NN')
('System', 'NNP')
('offering', 'VBG')
('hardware', 'NN')
('System', 'NNP')
('offering', 'VBG')
('software', 'NN')
('System', 'NNP')
('offering', 'VBG')
('integration', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('world', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('unique', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('entertainment', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('products', 'NNS')
('Nintendo', 'NNP')
('offering', 'VBG')
('development', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('concept', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('hardware', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('software', 'NN')
('Nintendo', 'NNP')
('offering', 'VBG')
('integration', 'NN')
('field', 'NN')
('is', 'VBZ')
('industries', 'NNS')
('field', 'NN')
('is', 'VBZ')
('Japan', 'NNP')
('field', 'NN')
('is', 'VBZ')
('spread', 'NN')
('field', 'NN')
('is', 'VBZ')
('world', 'NN')
('field', 'NN')
('is', 'VBZ')
('Nintendo', 'NNP')
('field', 'NN')
('is', 'VBZ')
('brand', 'NN')
('field', 'NN')
('is', 'VBZ')
('culture', 'NN')
('field', 'NN')
('is', 'VBZ')
('world', 'NN')
('home', 'NN')
('is', 'VBZ')
('industries', 'NNS')
('home', 'NN')
('is', 'VBZ')
('Japan', 'NNP')
('home', 'NN')
('is', 'VBZ')
('spread', 'NN')
('home', 'NN')
('is', 'VBZ')
('world', 'NN')
('home', 'NN')
('is', 'VBZ')
('Nintendo', 'NNP')
('home', 'NN')
('is', 'VBZ')
('brand', 'NN')
('home', 'NN')
('is', 'VBZ')
('culture', 'NN')
('home', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('industries', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('Japan', 'NNP')
('entertainment', 'NN')
('is', 'VBZ')
('spread', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('Nintendo', 'NNP')
('entertainment', 'NN')
('is', 'VBZ')
('brand', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('culture', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('video', 'NN')
('is', 'VBZ')
('industries', 'NNS')
('video', 'NN')
('is', 'VBZ')
('Japan', 'NNP')
('video', 'NN')
('is', 'VBZ')
('spread', 'NN')
('video', 'NN')
('is', 'VBZ')
('world', 'NN')
('video', 'NN')
('is', 'VBZ')
('Nintendo', 'NNP')
('video', 'NN')
('is', 'VBZ')
('brand', 'NN')
('video', 'NN')
('is', 'VBZ')
('culture', 'NN')
('video', 'NN')
('is', 'VBZ')
('world', 'NN')
('game', 'NN')
('is', 'VBZ')
('industries', 'NNS')
('game', 'NN')
('is', 'VBZ')
('Japan', 'NNP')
('game', 'NN')
('is', 'VBZ')
('spread', 'NN')
('game', 'NN')
('is', 'VBZ')
('world', 'NN')
('game', 'NN')
('is', 'VBZ')
('Nintendo', 'NNP')
('game', 'NN')
('is', 'VBZ')
('brand', 'NN')
('game', 'NN')
('is', 'VBZ')
('culture', 'NN')
('game', 'NN')
('is', 'VBZ')
('world', 'NN')
('industry', 'NN')
('is', 'VBZ')
('industries', 'NNS')
('industry', 'NN')
('is', 'VBZ')
('Japan', 'NNP')
('industry', 'NN')
('is', 'VBZ')
('spread', 'NN')
('industry', 'NN')
('is', 'VBZ')
('world', 'NN')
('industry', 'NN')
('is', 'VBZ')
('Nintendo', 'NNP')
('industry', 'NN')
('is', 'VBZ')
('brand', 'NN')
('industry', 'NN')
('is', 'VBZ')
('culture', 'NN')
('industry', 'NN')
('is', 'VBZ')
('world', 'NN')
('video', 'NN')
('is', 'VBZ')
('industries', 'NNS')
('video', 'NN')
('is', 'VBZ')
('Japan', 'NNP')
('video', 'NN')
('is', 'VBZ')
('spread', 'NN')
('video', 'NN')
('is', 'VBZ')
('world', 'NN')
('video', 'NN')
('is', 'VBZ')
('Nintendo', 'NNP')
('video', 'NN')
('is', 'VBZ')
('brand', 'NN')
('video', 'NN')
('is', 'VBZ')
('culture', 'NN')
('video', 'NN')
('is', 'VBZ')
('world', 'NN')
('game', 'NN')
('is', 'VBZ')
('industries', 'NNS')
('game', 'NN')
('is', 'VBZ')
('Japan', 'NNP')
('game', 'NN')
('is', 'VBZ')
('spread', 'NN')
('game', 'NN')
('is', 'VBZ')
('world', 'NN')
('game', 'NN')
('is', 'VBZ')
('Nintendo', 'NNP')
('game', 'NN')
('is', 'VBZ')
('brand', 'NN')
('game', 'NN')
('is', 'VBZ')
('culture', 'NN')
('game', 'NN')
('is', 'VBZ')
('world', 'NN')
('field', 'NN')
('established', 'VBD')
('Japan', 'NNP')
('field', 'NN')
('established', 'VBD')
('spread', 'NN')
('field', 'NN')
('established', 'VBD')
('world', 'NN')
('field', 'NN')
('established', 'VBD')
('Nintendo', 'NNP')
('field', 'NN')
('established', 'VBD')
('brand', 'NN')
('field', 'NN')
('established', 'VBD')
('culture', 'NN')
('field', 'NN')
('established', 'VBD')
('world', 'NN')
('home', 'NN')
('established', 'VBD')
('Japan', 'NNP')
('home', 'NN')
('established', 'VBD')
('spread', 'NN')
('home', 'NN')
('established', 'VBD')
('world', 'NN')
('home', 'NN')
('established', 'VBD')
('Nintendo', 'NNP')
('home', 'NN')
('established', 'VBD')
('brand', 'NN')
('home', 'NN')
('established', 'VBD')
('culture', 'NN')
('home', 'NN')
('established', 'VBD')
('world', 'NN')
('entertainment', 'NN')
('established', 'VBD')
('Japan', 'NNP')
('entertainment', 'NN')
('established', 'VBD')
('spread', 'NN')
('entertainment', 'NN')
('established', 'VBD')
('world', 'NN')
('entertainment', 'NN')
('established', 'VBD')
('Nintendo', 'NNP')
('entertainment', 'NN')
('established', 'VBD')
('brand', 'NN')
('entertainment', 'NN')
('established', 'VBD')
('culture', 'NN')
('entertainment', 'NN')
('established', 'VBD')
('world', 'NN')
('video', 'NN')
('established', 'VBD')
('Japan', 'NNP')
('video', 'NN')
('established', 'VBD')
('spread', 'NN')
('video', 'NN')
('established', 'VBD')
('world', 'NN')
('video', 'NN')
('established', 'VBD')
('Nintendo', 'NNP')
('video', 'NN')
('established', 'VBD')
('brand', 'NN')
('video', 'NN')
('established', 'VBD')
('culture', 'NN')
('video', 'NN')
('established', 'VBD')
('world', 'NN')
('game', 'NN')
('established', 'VBD')
('Japan', 'NNP')
('game', 'NN')
('established', 'VBD')
('spread', 'NN')
('game', 'NN')
('established', 'VBD')
('world', 'NN')
('game', 'NN')
('established', 'VBD')
('Nintendo', 'NNP')
('game', 'NN')
('established', 'VBD')
('brand', 'NN')
('game', 'NN')
('established', 'VBD')
('culture', 'NN')
('game', 'NN')
('established', 'VBD')
('world', 'NN')
('industry', 'NN')
('established', 'VBD')
('Japan', 'NNP')
('industry', 'NN')
('established', 'VBD')
('spread', 'NN')
('industry', 'NN')
('established', 'VBD')
('world', 'NN')
('industry', 'NN')
('established', 'VBD')
('Nintendo', 'NNP')
('industry', 'NN')
('established', 'VBD')
('brand', 'NN')
('industry', 'NN')
('established', 'VBD')
('culture', 'NN')
('industry', 'NN')
('established', 'VBD')
('world', 'NN')
('industries', 'NNS')
('established', 'VBD')
('Japan', 'NNP')
('industries', 'NNS')
('established', 'VBD')
('spread', 'NN')
('industries', 'NNS')
('established', 'VBD')
('world', 'NN')
('industries', 'NNS')
('established', 'VBD')
('Nintendo', 'NNP')
('industries', 'NNS')
('established', 'VBD')
('brand', 'NN')
('industries', 'NNS')
('established', 'VBD')
('culture', 'NN')
('industries', 'NNS')
('established', 'VBD')
('world', 'NN')
('video', 'NN')
('established', 'VBD')
('Japan', 'NNP')
('video', 'NN')
('established', 'VBD')
('spread', 'NN')
('video', 'NN')
('established', 'VBD')
('world', 'NN')
('video', 'NN')
('established', 'VBD')
('Nintendo', 'NNP')
('video', 'NN')
('established', 'VBD')
('brand', 'NN')
('video', 'NN')
('established', 'VBD')
('culture', 'NN')
('video', 'NN')
('established', 'VBD')
('world', 'NN')
('game', 'NN')
('established', 'VBD')
('Japan', 'NNP')
('game', 'NN')
('established', 'VBD')
('spread', 'NN')
('game', 'NN')
('established', 'VBD')
('world', 'NN')
('game', 'NN')
('established', 'VBD')
('Nintendo', 'NNP')
('game', 'NN')
('established', 'VBD')
('brand', 'NN')
('game', 'NN')
('established', 'VBD')
('culture', 'NN')
('game', 'NN')
('established', 'VBD')
('world', 'NN')
('field', 'NN')
('has', 'VBZ')
('brand', 'NN')
('field', 'NN')
('has', 'VBZ')
('culture', 'NN')
('home', 'NN')
('has', 'VBZ')
('brand', 'NN')
('home', 'NN')
('has', 'VBZ')
('culture', 'NN')
('entertainment', 'NN')
('has', 'VBZ')
('brand', 'NN')
('entertainment', 'NN')
('has', 'VBZ')
('culture', 'NN')
('video', 'NN')
('has', 'VBZ')
('brand', 'NN')
('video', 'NN')
('has', 'VBZ')
('culture', 'NN')
('game', 'NN')
('has', 'VBZ')
('brand', 'NN')
('game', 'NN')
('has', 'VBZ')
('culture', 'NN')
('industry', 'NN')
('has', 'VBZ')
('brand', 'NN')
('industry', 'NN')
('has', 'VBZ')
('culture', 'NN')
('industries', 'NNS')
('has', 'VBZ')
('brand', 'NN')
('industries', 'NNS')
('has', 'VBZ')
('culture', 'NN')
('Japan', 'NNP')
('has', 'VBZ')
('brand', 'NN')
('Japan', 'NNP')
('has', 'VBZ')
('culture', 'NN')
('spread', 'NN')
('has', 'VBZ')
('brand', 'NN')
('spread', 'NN')
('has', 'VBZ')
('culture', 'NN')
('world', 'NN')
('has', 'VBZ')
('brand', 'NN')
('world', 'NN')
('has', 'VBZ')
('culture', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('brand', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('culture', 'NN')
('video', 'NN')
('has', 'VBZ')
('brand', 'NN')
('video', 'NN')
('has', 'VBZ')
('culture', 'NN')
('game', 'NN')
('has', 'VBZ')
('brand', 'NN')
('game', 'NN')
('has', 'VBZ')
('culture', 'NN')
('world', 'NN')
('has', 'VBZ')
('brand', 'NN')
('world', 'NN')
('has', 'VBZ')
('culture', 'NN')
('field', 'NN')
('established', 'VBN')
('brand', 'NN')
('field', 'NN')
('established', 'VBN')
('culture', 'NN')
('home', 'NN')
('established', 'VBN')
('brand', 'NN')
('home', 'NN')
('established', 'VBN')
('culture', 'NN')
('entertainment', 'NN')
('established', 'VBN')
('brand', 'NN')
('entertainment', 'NN')
('established', 'VBN')
('culture', 'NN')
('video', 'NN')
('established', 'VBN')
('brand', 'NN')
('video', 'NN')
('established', 'VBN')
('culture', 'NN')
('game', 'NN')
('established', 'VBN')
('brand', 'NN')
('game', 'NN')
('established', 'VBN')
('culture', 'NN')
('industry', 'NN')
('established', 'VBN')
('brand', 'NN')
('industry', 'NN')
('established', 'VBN')
('culture', 'NN')
('industries', 'NNS')
('established', 'VBN')
('brand', 'NN')
('industries', 'NNS')
('established', 'VBN')
('culture', 'NN')
('Japan', 'NNP')
('established', 'VBN')
('brand', 'NN')
('Japan', 'NNP')
('established', 'VBN')
('culture', 'NN')
('spread', 'NN')
('established', 'VBN')
('brand', 'NN')
('spread', 'NN')
('established', 'VBN')
('culture', 'NN')
('world', 'NN')
('established', 'VBN')
('brand', 'NN')
('world', 'NN')
('established', 'VBN')
('culture', 'NN')
('Nintendo', 'NNP')
('established', 'VBN')
('brand', 'NN')
('Nintendo', 'NNP')
('established', 'VBN')
('culture', 'NN')
('video', 'NN')
('established', 'VBN')
('brand', 'NN')
('video', 'NN')
('established', 'VBN')
('culture', 'NN')
('game', 'NN')
('established', 'VBN')
('brand', 'NN')
('game', 'NN')
('established', 'VBN')
('culture', 'NN')
('world', 'NN')
('established', 'VBN')
('brand', 'NN')
('world', 'NN')
('established', 'VBN')
('culture', 'NN')
('field', 'NN')
('known', 'VBN')
('brand', 'NN')
('field', 'NN')
('known', 'VBN')
('culture', 'NN')
('home', 'NN')
('known', 'VBN')
('brand', 'NN')
('home', 'NN')
('known', 'VBN')
('culture', 'NN')
('entertainment', 'NN')
('known', 'VBN')
('brand', 'NN')
('entertainment', 'NN')
('known', 'VBN')
('culture', 'NN')
('video', 'NN')
('known', 'VBN')
('brand', 'NN')
('video', 'NN')
('known', 'VBN')
('culture', 'NN')
('game', 'NN')
('known', 'VBN')
('brand', 'NN')
('game', 'NN')
('known', 'VBN')
('culture', 'NN')
('industry', 'NN')
('known', 'VBN')
('brand', 'NN')
('industry', 'NN')
('known', 'VBN')
('culture', 'NN')
('industries', 'NNS')
('known', 'VBN')
('brand', 'NN')
('industries', 'NNS')
('known', 'VBN')
('culture', 'NN')
('Japan', 'NNP')
('known', 'VBN')
('brand', 'NN')
('Japan', 'NNP')
('known', 'VBN')
('culture', 'NN')
('spread', 'NN')
('known', 'VBN')
('brand', 'NN')
('spread', 'NN')
('known', 'VBN')
('culture', 'NN')
('world', 'NN')
('known', 'VBN')
('brand', 'NN')
('world', 'NN')
('known', 'VBN')
('culture', 'NN')
('Nintendo', 'NNP')
('known', 'VBN')
('brand', 'NN')
('Nintendo', 'NNP')
('known', 'VBN')
('culture', 'NN')
('video', 'NN')
('known', 'VBN')
('brand', 'NN')
('video', 'NN')
('known', 'VBN')
('culture', 'NN')
('game', 'NN')
('known', 'VBN')
('brand', 'NN')
('game', 'NN')
('known', 'VBN')
('culture', 'NN')
('world', 'NN')
('known', 'VBN')
('brand', 'NN')
('world', 'NN')
('known', 'VBN')
('culture', 'NN')
('field', 'NN')
('representing', 'VBG')
('culture', 'NN')
('home', 'NN')
('representing', 'VBG')
('culture', 'NN')
('entertainment', 'NN')
('representing', 'VBG')
('culture', 'NN')
('video', 'NN')
('representing', 'VBG')
('culture', 'NN')
('game', 'NN')
('representing', 'VBG')
('culture', 'NN')
('industry', 'NN')
('representing', 'VBG')
('culture', 'NN')
('industries', 'NNS')
('representing', 'VBG')
('culture', 'NN')
('Japan', 'NNP')
('representing', 'VBG')
('culture', 'NN')
('spread', 'NN')
('representing', 'VBG')
('culture', 'NN')
('world', 'NN')
('representing', 'VBG')
('culture', 'NN')
('Nintendo', 'NNP')
('representing', 'VBG')
('culture', 'NN')
('brand', 'NN')
('representing', 'VBG')
('culture', 'NN')
('video', 'NN')
('representing', 'VBG')
('culture', 'NN')
('game', 'NN')
('representing', 'VBG')
('culture', 'NN')
('world', 'NN')
('representing', 'VBG')
('culture', 'NN')
('belief', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('people', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('s', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('world', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('services', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('decade', 'NN')
('belief', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('belief', 'NN')
('is', 'VBZ')
('population', 'NN')
('belief', 'NN')
('is', 'VBZ')
('offering', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('belief', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('belief', 'NN')
('is', 'VBZ')
('age', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gender', 'NN')
('belief', 'NN')
('is', 'VBZ')
('experience', 'NN')
('belief', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('people', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('s', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('world', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('services', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('decade', 'NN')
('belief', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('belief', 'NN')
('is', 'VBZ')
('population', 'NN')
('belief', 'NN')
('is', 'VBZ')
('offering', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('belief', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('belief', 'NN')
('is', 'VBZ')
('age', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gender', 'NN')
('belief', 'NN')
('is', 'VBZ')
('experience', 'NN')
('raison', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('people', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('s', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('world', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('services', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('decade', 'NN')
('raison', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('raison', 'NN')
('is', 'VBZ')
('population', 'NN')
('raison', 'NN')
('is', 'VBZ')
('offering', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('raison', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('raison', 'NN')
('is', 'VBZ')
('age', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gender', 'NN')
('raison', 'NN')
('is', 'VBZ')
('experience', 'NN')
('raison', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('people', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('s', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('world', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('services', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('decade', 'NN')
('raison', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('raison', 'NN')
('is', 'VBZ')
('population', 'NN')
('raison', 'NN')
('is', 'VBZ')
('offering', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('raison', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('raison', 'NN')
('is', 'VBZ')
('age', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gender', 'NN')
('raison', 'NN')
('is', 'VBZ')
('experience', 'NN')
('d', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('d', 'NN')
('is', 'VBZ')
('people', 'NNS')
('d', 'NN')
('is', 'VBZ')
('s', 'NNS')
('d', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('d', 'NN')
('is', 'VBZ')
('world', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('services', 'NNS')
('d', 'NN')
('is', 'VBZ')
('decade', 'NN')
('d', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('d', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('d', 'NN')
('is', 'VBZ')
('population', 'NN')
('d', 'NN')
('is', 'VBZ')
('offering', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('d', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('d', 'NN')
('is', 'VBZ')
('age', 'NN')
('d', 'NN')
('is', 'VBZ')
('gender', 'NN')
('d', 'NN')
('is', 'VBZ')
('experience', 'NN')
('d', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('d', 'NN')
('is', 'VBZ')
('people', 'NNS')
('d', 'NN')
('is', 'VBZ')
('s', 'NNS')
('d', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('d', 'NN')
('is', 'VBZ')
('world', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('services', 'NNS')
('d', 'NN')
('is', 'VBZ')
('decade', 'NN')
('d', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('d', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('d', 'NN')
('is', 'VBZ')
('population', 'NN')
('d', 'NN')
('is', 'VBZ')
('offering', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('d', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('d', 'NN')
('is', 'VBZ')
('age', 'NN')
('d', 'NN')
('is', 'VBZ')
('gender', 'NN')
('d', 'NN')
('is', 'VBZ')
('experience', 'NN')
('etre', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('people', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('s', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('world', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('services', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('decade', 'NN')
('etre', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('etre', 'NN')
('is', 'VBZ')
('population', 'NN')
('etre', 'NN')
('is', 'VBZ')
('offering', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('etre', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('etre', 'NN')
('is', 'VBZ')
('age', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gender', 'NN')
('etre', 'NN')
('is', 'VBZ')
('experience', 'NN')
('etre', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('people', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('s', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('world', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('services', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('decade', 'NN')
('etre', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('etre', 'NN')
('is', 'VBZ')
('population', 'NN')
('etre', 'NN')
('is', 'VBZ')
('offering', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('etre', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('etre', 'NN')
('is', 'VBZ')
('age', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gender', 'NN')
('etre', 'NN')
('is', 'VBZ')
('experience', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('people', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('s', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('services', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('decade', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('population', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('offering', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('age', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gender', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('experience', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('people', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('s', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('services', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('decade', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('population', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('offering', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('age', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gender', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('experience', 'NN')
('belief', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('people', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('s', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('world', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('services', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('decade', 'NN')
('belief', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('belief', 'NN')
('is', 'VBZ')
('population', 'NN')
('belief', 'NN')
('is', 'VBZ')
('offering', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('belief', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('belief', 'NN')
('is', 'VBZ')
('age', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gender', 'NN')
('belief', 'NN')
('is', 'VBZ')
('experience', 'NN')
('belief', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('people', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('s', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('world', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('services', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('decade', 'NN')
('belief', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('belief', 'NN')
('is', 'VBZ')
('population', 'NN')
('belief', 'NN')
('is', 'VBZ')
('offering', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('belief', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('belief', 'NN')
('is', 'VBZ')
('age', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gender', 'NN')
('belief', 'NN')
('is', 'VBZ')
('experience', 'NN')
('raison', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('people', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('s', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('world', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('services', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('decade', 'NN')
('raison', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('raison', 'NN')
('is', 'VBZ')
('population', 'NN')
('raison', 'NN')
('is', 'VBZ')
('offering', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('raison', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('raison', 'NN')
('is', 'VBZ')
('age', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gender', 'NN')
('raison', 'NN')
('is', 'VBZ')
('experience', 'NN')
('raison', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('people', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('s', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('world', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('services', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('decade', 'NN')
('raison', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('raison', 'NN')
('is', 'VBZ')
('population', 'NN')
('raison', 'NN')
('is', 'VBZ')
('offering', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('raison', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('raison', 'NN')
('is', 'VBZ')
('age', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gender', 'NN')
('raison', 'NN')
('is', 'VBZ')
('experience', 'NN')
('d', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('d', 'NN')
('is', 'VBZ')
('people', 'NNS')
('d', 'NN')
('is', 'VBZ')
('s', 'NNS')
('d', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('d', 'NN')
('is', 'VBZ')
('world', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('services', 'NNS')
('d', 'NN')
('is', 'VBZ')
('decade', 'NN')
('d', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('d', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('d', 'NN')
('is', 'VBZ')
('population', 'NN')
('d', 'NN')
('is', 'VBZ')
('offering', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('d', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('d', 'NN')
('is', 'VBZ')
('age', 'NN')
('d', 'NN')
('is', 'VBZ')
('gender', 'NN')
('d', 'NN')
('is', 'VBZ')
('experience', 'NN')
('d', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('d', 'NN')
('is', 'VBZ')
('people', 'NNS')
('d', 'NN')
('is', 'VBZ')
('s', 'NNS')
('d', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('d', 'NN')
('is', 'VBZ')
('world', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('services', 'NNS')
('d', 'NN')
('is', 'VBZ')
('decade', 'NN')
('d', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('d', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('d', 'NN')
('is', 'VBZ')
('population', 'NN')
('d', 'NN')
('is', 'VBZ')
('offering', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('d', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('d', 'NN')
('is', 'VBZ')
('age', 'NN')
('d', 'NN')
('is', 'VBZ')
('gender', 'NN')
('d', 'NN')
('is', 'VBZ')
('experience', 'NN')
('etre', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('people', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('s', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('world', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('services', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('decade', 'NN')
('etre', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('etre', 'NN')
('is', 'VBZ')
('population', 'NN')
('etre', 'NN')
('is', 'VBZ')
('offering', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('etre', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('etre', 'NN')
('is', 'VBZ')
('age', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gender', 'NN')
('etre', 'NN')
('is', 'VBZ')
('experience', 'NN')
('etre', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('people', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('s', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('world', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('services', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('decade', 'NN')
('etre', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('etre', 'NN')
('is', 'VBZ')
('population', 'NN')
('etre', 'NN')
('is', 'VBZ')
('offering', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('etre', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('etre', 'NN')
('is', 'VBZ')
('age', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gender', 'NN')
('etre', 'NN')
('is', 'VBZ')
('experience', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('people', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('s', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('services', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('decade', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('population', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('offering', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('age', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gender', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('experience', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('people', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('s', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('services', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('decade', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('population', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('offering', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('age', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gender', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('experience', 'NN')
('belief', 'NN')
('put', 'VB')
('smiles', 'NNS')
('belief', 'NN')
('put', 'VB')
('people', 'NNS')
('belief', 'NN')
('put', 'VB')
('s', 'NNS')
('belief', 'NN')
('put', 'VB')
('faces', 'NNS')
('belief', 'NN')
('put', 'VB')
('world', 'NN')
('belief', 'NN')
('put', 'VB')
('products', 'NNS')
('belief', 'NN')
('put', 'VB')
('services', 'NNS')
('belief', 'NN')
('put', 'VB')
('decade', 'NN')
('belief', 'NN')
('put', 'VB')
('strategy', 'NN')
('belief', 'NN')
('put', 'VB')
('gaming', 'NN')
('belief', 'NN')
('put', 'VB')
('population', 'NN')
('belief', 'NN')
('put', 'VB')
('offering', 'NN')
('belief', 'NN')
('put', 'VB')
('products', 'NNS')
('belief', 'NN')
('put', 'VB')
('everyone', 'NN')
('belief', 'NN')
('put', 'VB')
('regardless', 'NN')
('belief', 'NN')
('put', 'VB')
('age', 'NN')
('belief', 'NN')
('put', 'VB')
('gender', 'NN')
('belief', 'NN')
('put', 'VB')
('experience', 'NN')
('raison', 'NN')
('put', 'VB')
('smiles', 'NNS')
('raison', 'NN')
('put', 'VB')
('people', 'NNS')
('raison', 'NN')
('put', 'VB')
('s', 'NNS')
('raison', 'NN')
('put', 'VB')
('faces', 'NNS')
('raison', 'NN')
('put', 'VB')
('world', 'NN')
('raison', 'NN')
('put', 'VB')
('products', 'NNS')
('raison', 'NN')
('put', 'VB')
('services', 'NNS')
('raison', 'NN')
('put', 'VB')
('decade', 'NN')
('raison', 'NN')
('put', 'VB')
('strategy', 'NN')
('raison', 'NN')
('put', 'VB')
('gaming', 'NN')
('raison', 'NN')
('put', 'VB')
('population', 'NN')
('raison', 'NN')
('put', 'VB')
('offering', 'NN')
('raison', 'NN')
('put', 'VB')
('products', 'NNS')
('raison', 'NN')
('put', 'VB')
('everyone', 'NN')
('raison', 'NN')
('put', 'VB')
('regardless', 'NN')
('raison', 'NN')
('put', 'VB')
('age', 'NN')
('raison', 'NN')
('put', 'VB')
('gender', 'NN')
('raison', 'NN')
('put', 'VB')
('experience', 'NN')
('d', 'NN')
('put', 'VB')
('smiles', 'NNS')
('d', 'NN')
('put', 'VB')
('people', 'NNS')
('d', 'NN')
('put', 'VB')
('s', 'NNS')
('d', 'NN')
('put', 'VB')
('faces', 'NNS')
('d', 'NN')
('put', 'VB')
('world', 'NN')
('d', 'NN')
('put', 'VB')
('products', 'NNS')
('d', 'NN')
('put', 'VB')
('services', 'NNS')
('d', 'NN')
('put', 'VB')
('decade', 'NN')
('d', 'NN')
('put', 'VB')
('strategy', 'NN')
('d', 'NN')
('put', 'VB')
('gaming', 'NN')
('d', 'NN')
('put', 'VB')
('population', 'NN')
('d', 'NN')
('put', 'VB')
('offering', 'NN')
('d', 'NN')
('put', 'VB')
('products', 'NNS')
('d', 'NN')
('put', 'VB')
('everyone', 'NN')
('d', 'NN')
('put', 'VB')
('regardless', 'NN')
('d', 'NN')
('put', 'VB')
('age', 'NN')
('d', 'NN')
('put', 'VB')
('gender', 'NN')
('d', 'NN')
('put', 'VB')
('experience', 'NN')
('etre', 'NN')
('put', 'VB')
('smiles', 'NNS')
('etre', 'NN')
('put', 'VB')
('people', 'NNS')
('etre', 'NN')
('put', 'VB')
('s', 'NNS')
('etre', 'NN')
('put', 'VB')
('faces', 'NNS')
('etre', 'NN')
('put', 'VB')
('world', 'NN')
('etre', 'NN')
('put', 'VB')
('products', 'NNS')
('etre', 'NN')
('put', 'VB')
('services', 'NNS')
('etre', 'NN')
('put', 'VB')
('decade', 'NN')
('etre', 'NN')
('put', 'VB')
('strategy', 'NN')
('etre', 'NN')
('put', 'VB')
('gaming', 'NN')
('etre', 'NN')
('put', 'VB')
('population', 'NN')
('etre', 'NN')
('put', 'VB')
('offering', 'NN')
('etre', 'NN')
('put', 'VB')
('products', 'NNS')
('etre', 'NN')
('put', 'VB')
('everyone', 'NN')
('etre', 'NN')
('put', 'VB')
('regardless', 'NN')
('etre', 'NN')
('put', 'VB')
('age', 'NN')
('etre', 'NN')
('put', 'VB')
('gender', 'NN')
('etre', 'NN')
('put', 'VB')
('experience', 'NN')
('entertainment', 'NN')
('put', 'VB')
('smiles', 'NNS')
('entertainment', 'NN')
('put', 'VB')
('people', 'NNS')
('entertainment', 'NN')
('put', 'VB')
('s', 'NNS')
('entertainment', 'NN')
('put', 'VB')
('faces', 'NNS')
('entertainment', 'NN')
('put', 'VB')
('world', 'NN')
('entertainment', 'NN')
('put', 'VB')
('products', 'NNS')
('entertainment', 'NN')
('put', 'VB')
('services', 'NNS')
('entertainment', 'NN')
('put', 'VB')
('decade', 'NN')
('entertainment', 'NN')
('put', 'VB')
('strategy', 'NN')
('entertainment', 'NN')
('put', 'VB')
('gaming', 'NN')
('entertainment', 'NN')
('put', 'VB')
('population', 'NN')
('entertainment', 'NN')
('put', 'VB')
('offering', 'NN')
('entertainment', 'NN')
('put', 'VB')
('products', 'NNS')
('entertainment', 'NN')
('put', 'VB')
('everyone', 'NN')
('entertainment', 'NN')
('put', 'VB')
('regardless', 'NN')
('entertainment', 'NN')
('put', 'VB')
('age', 'NN')
('entertainment', 'NN')
('put', 'VB')
('gender', 'NN')
('entertainment', 'NN')
('put', 'VB')
('experience', 'NN')
('belief', 'NN')
('have', 'VBP')
('decade', 'NN')
('belief', 'NN')
('have', 'VBP')
('strategy', 'NN')
('belief', 'NN')
('have', 'VBP')
('gaming', 'NN')
('belief', 'NN')
('have', 'VBP')
('population', 'NN')
('belief', 'NN')
('have', 'VBP')
('offering', 'NN')
('belief', 'NN')
('have', 'VBP')
('everyone', 'NN')
('belief', 'NN')
('have', 'VBP')
('regardless', 'NN')
('belief', 'NN')
('have', 'VBP')
('age', 'NN')
('belief', 'NN')
('have', 'VBP')
('gender', 'NN')
('belief', 'NN')
('have', 'VBP')
('experience', 'NN')
('raison', 'NN')
('have', 'VBP')
('decade', 'NN')
('raison', 'NN')
('have', 'VBP')
('strategy', 'NN')
('raison', 'NN')
('have', 'VBP')
('gaming', 'NN')
('raison', 'NN')
('have', 'VBP')
('population', 'NN')
('raison', 'NN')
('have', 'VBP')
('offering', 'NN')
('raison', 'NN')
('have', 'VBP')
('everyone', 'NN')
('raison', 'NN')
('have', 'VBP')
('regardless', 'NN')
('raison', 'NN')
('have', 'VBP')
('age', 'NN')
('raison', 'NN')
('have', 'VBP')
('gender', 'NN')
('raison', 'NN')
('have', 'VBP')
('experience', 'NN')
('d', 'NN')
('have', 'VBP')
('decade', 'NN')
('d', 'NN')
('have', 'VBP')
('strategy', 'NN')
('d', 'NN')
('have', 'VBP')
('gaming', 'NN')
('d', 'NN')
('have', 'VBP')
('population', 'NN')
('d', 'NN')
('have', 'VBP')
('offering', 'NN')
('d', 'NN')
('have', 'VBP')
('everyone', 'NN')
('d', 'NN')
('have', 'VBP')
('regardless', 'NN')
('d', 'NN')
('have', 'VBP')
('age', 'NN')
('d', 'NN')
('have', 'VBP')
('gender', 'NN')
('d', 'NN')
('have', 'VBP')
('experience', 'NN')
('etre', 'NN')
('have', 'VBP')
('decade', 'NN')
('etre', 'NN')
('have', 'VBP')
('strategy', 'NN')
('etre', 'NN')
('have', 'VBP')
('gaming', 'NN')
('etre', 'NN')
('have', 'VBP')
('population', 'NN')
('etre', 'NN')
('have', 'VBP')
('offering', 'NN')
('etre', 'NN')
('have', 'VBP')
('everyone', 'NN')
('etre', 'NN')
('have', 'VBP')
('regardless', 'NN')
('etre', 'NN')
('have', 'VBP')
('age', 'NN')
('etre', 'NN')
('have', 'VBP')
('gender', 'NN')
('etre', 'NN')
('have', 'VBP')
('experience', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('decade', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('strategy', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('gaming', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('population', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('offering', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('everyone', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('regardless', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('age', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('gender', 'NN')
('entertainment', 'NN')
('have', 'VBP')
('experience', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('decade', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('strategy', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('gaming', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('population', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('offering', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('everyone', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('regardless', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('age', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('gender', 'NN')
('smiles', 'NNS')
('have', 'VBP')
('experience', 'NN')
('people', 'NNS')
('have', 'VBP')
('decade', 'NN')
('people', 'NNS')
('have', 'VBP')
('strategy', 'NN')
('people', 'NNS')
('have', 'VBP')
('gaming', 'NN')
('people', 'NNS')
('have', 'VBP')
('population', 'NN')
('people', 'NNS')
('have', 'VBP')
('offering', 'NN')
('people', 'NNS')
('have', 'VBP')
('everyone', 'NN')
('people', 'NNS')
('have', 'VBP')
('regardless', 'NN')
('people', 'NNS')
('have', 'VBP')
('age', 'NN')
('people', 'NNS')
('have', 'VBP')
('gender', 'NN')
('people', 'NNS')
('have', 'VBP')
('experience', 'NN')
('s', 'NNS')
('have', 'VBP')
('decade', 'NN')
('s', 'NNS')
('have', 'VBP')
('strategy', 'NN')
('s', 'NNS')
('have', 'VBP')
('gaming', 'NN')
('s', 'NNS')
('have', 'VBP')
('population', 'NN')
('s', 'NNS')
('have', 'VBP')
('offering', 'NN')
('s', 'NNS')
('have', 'VBP')
('everyone', 'NN')
('s', 'NNS')
('have', 'VBP')
('regardless', 'NN')
('s', 'NNS')
('have', 'VBP')
('age', 'NN')
('s', 'NNS')
('have', 'VBP')
('gender', 'NN')
('s', 'NNS')
('have', 'VBP')
('experience', 'NN')
('faces', 'NNS')
('have', 'VBP')
('decade', 'NN')
('faces', 'NNS')
('have', 'VBP')
('strategy', 'NN')
('faces', 'NNS')
('have', 'VBP')
('gaming', 'NN')
('faces', 'NNS')
('have', 'VBP')
('population', 'NN')
('faces', 'NNS')
('have', 'VBP')
('offering', 'NN')
('faces', 'NNS')
('have', 'VBP')
('everyone', 'NN')
('faces', 'NNS')
('have', 'VBP')
('regardless', 'NN')
('faces', 'NNS')
('have', 'VBP')
('age', 'NN')
('faces', 'NNS')
('have', 'VBP')
('gender', 'NN')
('faces', 'NNS')
('have', 'VBP')
('experience', 'NN')
('world', 'NN')
('have', 'VBP')
('decade', 'NN')
('world', 'NN')
('have', 'VBP')
('strategy', 'NN')
('world', 'NN')
('have', 'VBP')
('gaming', 'NN')
('world', 'NN')
('have', 'VBP')
('population', 'NN')
('world', 'NN')
('have', 'VBP')
('offering', 'NN')
('world', 'NN')
('have', 'VBP')
('everyone', 'NN')
('world', 'NN')
('have', 'VBP')
('regardless', 'NN')
('world', 'NN')
('have', 'VBP')
('age', 'NN')
('world', 'NN')
('have', 'VBP')
('gender', 'NN')
('world', 'NN')
('have', 'VBP')
('experience', 'NN')
('products', 'NNS')
('have', 'VBP')
('decade', 'NN')
('products', 'NNS')
('have', 'VBP')
('strategy', 'NN')
('products', 'NNS')
('have', 'VBP')
('gaming', 'NN')
('products', 'NNS')
('have', 'VBP')
('population', 'NN')
('products', 'NNS')
('have', 'VBP')
('offering', 'NN')
('products', 'NNS')
('have', 'VBP')
('everyone', 'NN')
('products', 'NNS')
('have', 'VBP')
('regardless', 'NN')
('products', 'NNS')
('have', 'VBP')
('age', 'NN')
('products', 'NNS')
('have', 'VBP')
('gender', 'NN')
('products', 'NNS')
('have', 'VBP')
('experience', 'NN')
('services', 'NNS')
('have', 'VBP')
('decade', 'NN')
('services', 'NNS')
('have', 'VBP')
('strategy', 'NN')
('services', 'NNS')
('have', 'VBP')
('gaming', 'NN')
('services', 'NNS')
('have', 'VBP')
('population', 'NN')
('services', 'NNS')
('have', 'VBP')
('offering', 'NN')
('services', 'NNS')
('have', 'VBP')
('everyone', 'NN')
('services', 'NNS')
('have', 'VBP')
('regardless', 'NN')
('services', 'NNS')
('have', 'VBP')
('age', 'NN')
('services', 'NNS')
('have', 'VBP')
('gender', 'NN')
('services', 'NNS')
('have', 'VBP')
('experience', 'NN')
('products', 'NNS')
('have', 'VBP')
('decade', 'NN')
('products', 'NNS')
('have', 'VBP')
('strategy', 'NN')
('products', 'NNS')
('have', 'VBP')
('gaming', 'NN')
('products', 'NNS')
('have', 'VBP')
('population', 'NN')
('products', 'NNS')
('have', 'VBP')
('offering', 'NN')
('products', 'NNS')
('have', 'VBP')
('everyone', 'NN')
('products', 'NNS')
('have', 'VBP')
('regardless', 'NN')
('products', 'NNS')
('have', 'VBP')
('age', 'NN')
('products', 'NNS')
('have', 'VBP')
('gender', 'NN')
('products', 'NNS')
('have', 'VBP')
('experience', 'NN')
('belief', 'NN')
('focused', 'VBN')
('decade', 'NN')
('belief', 'NN')
('focused', 'VBN')
('strategy', 'NN')
('belief', 'NN')
('focused', 'VBN')
('gaming', 'NN')
('belief', 'NN')
('focused', 'VBN')
('population', 'NN')
('belief', 'NN')
('focused', 'VBN')
('offering', 'NN')
('belief', 'NN')
('focused', 'VBN')
('everyone', 'NN')
('belief', 'NN')
('focused', 'VBN')
('regardless', 'NN')
('belief', 'NN')
('focused', 'VBN')
('age', 'NN')
('belief', 'NN')
('focused', 'VBN')
('gender', 'NN')
('belief', 'NN')
('focused', 'VBN')
('experience', 'NN')
('raison', 'NN')
('focused', 'VBN')
('decade', 'NN')
('raison', 'NN')
('focused', 'VBN')
('strategy', 'NN')
('raison', 'NN')
('focused', 'VBN')
('gaming', 'NN')
('raison', 'NN')
('focused', 'VBN')
('population', 'NN')
('raison', 'NN')
('focused', 'VBN')
('offering', 'NN')
('raison', 'NN')
('focused', 'VBN')
('everyone', 'NN')
('raison', 'NN')
('focused', 'VBN')
('regardless', 'NN')
('raison', 'NN')
('focused', 'VBN')
('age', 'NN')
('raison', 'NN')
('focused', 'VBN')
('gender', 'NN')
('raison', 'NN')
('focused', 'VBN')
('experience', 'NN')
('d', 'NN')
('focused', 'VBN')
('decade', 'NN')
('d', 'NN')
('focused', 'VBN')
('strategy', 'NN')
('d', 'NN')
('focused', 'VBN')
('gaming', 'NN')
('d', 'NN')
('focused', 'VBN')
('population', 'NN')
('d', 'NN')
('focused', 'VBN')
('offering', 'NN')
('d', 'NN')
('focused', 'VBN')
('everyone', 'NN')
('d', 'NN')
('focused', 'VBN')
('regardless', 'NN')
('d', 'NN')
('focused', 'VBN')
('age', 'NN')
('d', 'NN')
('focused', 'VBN')
('gender', 'NN')
('d', 'NN')
('focused', 'VBN')
('experience', 'NN')
('etre', 'NN')
('focused', 'VBN')
('decade', 'NN')
('etre', 'NN')
('focused', 'VBN')
('strategy', 'NN')
('etre', 'NN')
('focused', 'VBN')
('gaming', 'NN')
('etre', 'NN')
('focused', 'VBN')
('population', 'NN')
('etre', 'NN')
('focused', 'VBN')
('offering', 'NN')
('etre', 'NN')
('focused', 'VBN')
('everyone', 'NN')
('etre', 'NN')
('focused', 'VBN')
('regardless', 'NN')
('etre', 'NN')
('focused', 'VBN')
('age', 'NN')
('etre', 'NN')
('focused', 'VBN')
('gender', 'NN')
('etre', 'NN')
('focused', 'VBN')
('experience', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('decade', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('strategy', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('gaming', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('population', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('offering', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('everyone', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('regardless', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('age', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('gender', 'NN')
('entertainment', 'NN')
('focused', 'VBN')
('experience', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('decade', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('strategy', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('gaming', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('population', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('offering', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('everyone', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('regardless', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('age', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('gender', 'NN')
('smiles', 'NNS')
('focused', 'VBN')
('experience', 'NN')
('people', 'NNS')
('focused', 'VBN')
('decade', 'NN')
('people', 'NNS')
('focused', 'VBN')
('strategy', 'NN')
('people', 'NNS')
('focused', 'VBN')
('gaming', 'NN')
('people', 'NNS')
('focused', 'VBN')
('population', 'NN')
('people', 'NNS')
('focused', 'VBN')
('offering', 'NN')
('people', 'NNS')
('focused', 'VBN')
('everyone', 'NN')
('people', 'NNS')
('focused', 'VBN')
('regardless', 'NN')
('people', 'NNS')
('focused', 'VBN')
('age', 'NN')
('people', 'NNS')
('focused', 'VBN')
('gender', 'NN')
('people', 'NNS')
('focused', 'VBN')
('experience', 'NN')
('s', 'NNS')
('focused', 'VBN')
('decade', 'NN')
('s', 'NNS')
('focused', 'VBN')
('strategy', 'NN')
('s', 'NNS')
('focused', 'VBN')
('gaming', 'NN')
('s', 'NNS')
('focused', 'VBN')
('population', 'NN')
('s', 'NNS')
('focused', 'VBN')
('offering', 'NN')
('s', 'NNS')
('focused', 'VBN')
('everyone', 'NN')
('s', 'NNS')
('focused', 'VBN')
('regardless', 'NN')
('s', 'NNS')
('focused', 'VBN')
('age', 'NN')
('s', 'NNS')
('focused', 'VBN')
('gender', 'NN')
('s', 'NNS')
('focused', 'VBN')
('experience', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('decade', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('strategy', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('gaming', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('population', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('offering', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('everyone', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('regardless', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('age', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('gender', 'NN')
('faces', 'NNS')
('focused', 'VBN')
('experience', 'NN')
('world', 'NN')
('focused', 'VBN')
('decade', 'NN')
('world', 'NN')
('focused', 'VBN')
('strategy', 'NN')
('world', 'NN')
('focused', 'VBN')
('gaming', 'NN')
('world', 'NN')
('focused', 'VBN')
('population', 'NN')
('world', 'NN')
('focused', 'VBN')
('offering', 'NN')
('world', 'NN')
('focused', 'VBN')
('everyone', 'NN')
('world', 'NN')
('focused', 'VBN')
('regardless', 'NN')
('world', 'NN')
('focused', 'VBN')
('age', 'NN')
('world', 'NN')
('focused', 'VBN')
('gender', 'NN')
('world', 'NN')
('focused', 'VBN')
('experience', 'NN')
('products', 'NNS')
('focused', 'VBN')
('decade', 'NN')
('products', 'NNS')
('focused', 'VBN')
('strategy', 'NN')
('products', 'NNS')
('focused', 'VBN')
('gaming', 'NN')
('products', 'NNS')
('focused', 'VBN')
('population', 'NN')
('products', 'NNS')
('focused', 'VBN')
('offering', 'NN')
('products', 'NNS')
('focused', 'VBN')
('everyone', 'NN')
('products', 'NNS')
('focused', 'VBN')
('regardless', 'NN')
('products', 'NNS')
('focused', 'VBN')
('age', 'NN')
('products', 'NNS')
('focused', 'VBN')
('gender', 'NN')
('products', 'NNS')
('focused', 'VBN')
('experience', 'NN')
('services', 'NNS')
('focused', 'VBN')
('decade', 'NN')
('services', 'NNS')
('focused', 'VBN')
('strategy', 'NN')
('services', 'NNS')
('focused', 'VBN')
('gaming', 'NN')
('services', 'NNS')
('focused', 'VBN')
('population', 'NN')
('services', 'NNS')
('focused', 'VBN')
('offering', 'NN')
('services', 'NNS')
('focused', 'VBN')
('everyone', 'NN')
('services', 'NNS')
('focused', 'VBN')
('regardless', 'NN')
('services', 'NNS')
('focused', 'VBN')
('age', 'NN')
('services', 'NNS')
('focused', 'VBN')
('gender', 'NN')
('services', 'NNS')
('focused', 'VBN')
('experience', 'NN')
('products', 'NNS')
('focused', 'VBN')
('decade', 'NN')
('products', 'NNS')
('focused', 'VBN')
('strategy', 'NN')
('products', 'NNS')
('focused', 'VBN')
('gaming', 'NN')
('products', 'NNS')
('focused', 'VBN')
('population', 'NN')
('products', 'NNS')
('focused', 'VBN')
('offering', 'NN')
('products', 'NNS')
('focused', 'VBN')
('everyone', 'NN')
('products', 'NNS')
('focused', 'VBN')
('regardless', 'NN')
('products', 'NNS')
('focused', 'VBN')
('age', 'NN')
('products', 'NNS')
('focused', 'VBN')
('gender', 'NN')
('products', 'NNS')
('focused', 'VBN')
('experience', 'NN')
('belief', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('people', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('s', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('world', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('services', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('decade', 'NN')
('belief', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('belief', 'NN')
('is', 'VBZ')
('population', 'NN')
('belief', 'NN')
('is', 'VBZ')
('offering', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('belief', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('belief', 'NN')
('is', 'VBZ')
('age', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gender', 'NN')
('belief', 'NN')
('is', 'VBZ')
('experience', 'NN')
('belief', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('people', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('s', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('world', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('services', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('decade', 'NN')
('belief', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('belief', 'NN')
('is', 'VBZ')
('population', 'NN')
('belief', 'NN')
('is', 'VBZ')
('offering', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('belief', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('belief', 'NN')
('is', 'VBZ')
('age', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gender', 'NN')
('belief', 'NN')
('is', 'VBZ')
('experience', 'NN')
('raison', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('people', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('s', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('world', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('services', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('decade', 'NN')
('raison', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('raison', 'NN')
('is', 'VBZ')
('population', 'NN')
('raison', 'NN')
('is', 'VBZ')
('offering', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('raison', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('raison', 'NN')
('is', 'VBZ')
('age', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gender', 'NN')
('raison', 'NN')
('is', 'VBZ')
('experience', 'NN')
('raison', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('people', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('s', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('world', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('services', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('decade', 'NN')
('raison', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('raison', 'NN')
('is', 'VBZ')
('population', 'NN')
('raison', 'NN')
('is', 'VBZ')
('offering', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('raison', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('raison', 'NN')
('is', 'VBZ')
('age', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gender', 'NN')
('raison', 'NN')
('is', 'VBZ')
('experience', 'NN')
('d', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('d', 'NN')
('is', 'VBZ')
('people', 'NNS')
('d', 'NN')
('is', 'VBZ')
('s', 'NNS')
('d', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('d', 'NN')
('is', 'VBZ')
('world', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('services', 'NNS')
('d', 'NN')
('is', 'VBZ')
('decade', 'NN')
('d', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('d', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('d', 'NN')
('is', 'VBZ')
('population', 'NN')
('d', 'NN')
('is', 'VBZ')
('offering', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('d', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('d', 'NN')
('is', 'VBZ')
('age', 'NN')
('d', 'NN')
('is', 'VBZ')
('gender', 'NN')
('d', 'NN')
('is', 'VBZ')
('experience', 'NN')
('d', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('d', 'NN')
('is', 'VBZ')
('people', 'NNS')
('d', 'NN')
('is', 'VBZ')
('s', 'NNS')
('d', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('d', 'NN')
('is', 'VBZ')
('world', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('services', 'NNS')
('d', 'NN')
('is', 'VBZ')
('decade', 'NN')
('d', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('d', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('d', 'NN')
('is', 'VBZ')
('population', 'NN')
('d', 'NN')
('is', 'VBZ')
('offering', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('d', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('d', 'NN')
('is', 'VBZ')
('age', 'NN')
('d', 'NN')
('is', 'VBZ')
('gender', 'NN')
('d', 'NN')
('is', 'VBZ')
('experience', 'NN')
('etre', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('people', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('s', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('world', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('services', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('decade', 'NN')
('etre', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('etre', 'NN')
('is', 'VBZ')
('population', 'NN')
('etre', 'NN')
('is', 'VBZ')
('offering', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('etre', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('etre', 'NN')
('is', 'VBZ')
('age', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gender', 'NN')
('etre', 'NN')
('is', 'VBZ')
('experience', 'NN')
('etre', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('people', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('s', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('world', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('services', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('decade', 'NN')
('etre', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('etre', 'NN')
('is', 'VBZ')
('population', 'NN')
('etre', 'NN')
('is', 'VBZ')
('offering', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('etre', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('etre', 'NN')
('is', 'VBZ')
('age', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gender', 'NN')
('etre', 'NN')
('is', 'VBZ')
('experience', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('people', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('s', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('services', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('decade', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('population', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('offering', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('age', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gender', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('experience', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('people', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('s', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('services', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('decade', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('population', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('offering', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('age', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gender', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('experience', 'NN')
('belief', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('people', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('s', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('world', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('services', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('decade', 'NN')
('belief', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('belief', 'NN')
('is', 'VBZ')
('population', 'NN')
('belief', 'NN')
('is', 'VBZ')
('offering', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('belief', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('belief', 'NN')
('is', 'VBZ')
('age', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gender', 'NN')
('belief', 'NN')
('is', 'VBZ')
('experience', 'NN')
('belief', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('people', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('s', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('world', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('services', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('decade', 'NN')
('belief', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('belief', 'NN')
('is', 'VBZ')
('population', 'NN')
('belief', 'NN')
('is', 'VBZ')
('offering', 'NN')
('belief', 'NN')
('is', 'VBZ')
('products', 'NNS')
('belief', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('belief', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('belief', 'NN')
('is', 'VBZ')
('age', 'NN')
('belief', 'NN')
('is', 'VBZ')
('gender', 'NN')
('belief', 'NN')
('is', 'VBZ')
('experience', 'NN')
('raison', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('people', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('s', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('world', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('services', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('decade', 'NN')
('raison', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('raison', 'NN')
('is', 'VBZ')
('population', 'NN')
('raison', 'NN')
('is', 'VBZ')
('offering', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('raison', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('raison', 'NN')
('is', 'VBZ')
('age', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gender', 'NN')
('raison', 'NN')
('is', 'VBZ')
('experience', 'NN')
('raison', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('people', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('s', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('world', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('services', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('decade', 'NN')
('raison', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('raison', 'NN')
('is', 'VBZ')
('population', 'NN')
('raison', 'NN')
('is', 'VBZ')
('offering', 'NN')
('raison', 'NN')
('is', 'VBZ')
('products', 'NNS')
('raison', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('raison', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('raison', 'NN')
('is', 'VBZ')
('age', 'NN')
('raison', 'NN')
('is', 'VBZ')
('gender', 'NN')
('raison', 'NN')
('is', 'VBZ')
('experience', 'NN')
('d', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('d', 'NN')
('is', 'VBZ')
('people', 'NNS')
('d', 'NN')
('is', 'VBZ')
('s', 'NNS')
('d', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('d', 'NN')
('is', 'VBZ')
('world', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('services', 'NNS')
('d', 'NN')
('is', 'VBZ')
('decade', 'NN')
('d', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('d', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('d', 'NN')
('is', 'VBZ')
('population', 'NN')
('d', 'NN')
('is', 'VBZ')
('offering', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('d', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('d', 'NN')
('is', 'VBZ')
('age', 'NN')
('d', 'NN')
('is', 'VBZ')
('gender', 'NN')
('d', 'NN')
('is', 'VBZ')
('experience', 'NN')
('d', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('d', 'NN')
('is', 'VBZ')
('people', 'NNS')
('d', 'NN')
('is', 'VBZ')
('s', 'NNS')
('d', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('d', 'NN')
('is', 'VBZ')
('world', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('services', 'NNS')
('d', 'NN')
('is', 'VBZ')
('decade', 'NN')
('d', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('d', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('d', 'NN')
('is', 'VBZ')
('population', 'NN')
('d', 'NN')
('is', 'VBZ')
('offering', 'NN')
('d', 'NN')
('is', 'VBZ')
('products', 'NNS')
('d', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('d', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('d', 'NN')
('is', 'VBZ')
('age', 'NN')
('d', 'NN')
('is', 'VBZ')
('gender', 'NN')
('d', 'NN')
('is', 'VBZ')
('experience', 'NN')
('etre', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('people', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('s', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('world', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('services', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('decade', 'NN')
('etre', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('etre', 'NN')
('is', 'VBZ')
('population', 'NN')
('etre', 'NN')
('is', 'VBZ')
('offering', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('etre', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('etre', 'NN')
('is', 'VBZ')
('age', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gender', 'NN')
('etre', 'NN')
('is', 'VBZ')
('experience', 'NN')
('etre', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('people', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('s', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('world', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('services', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('decade', 'NN')
('etre', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('etre', 'NN')
('is', 'VBZ')
('population', 'NN')
('etre', 'NN')
('is', 'VBZ')
('offering', 'NN')
('etre', 'NN')
('is', 'VBZ')
('products', 'NNS')
('etre', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('etre', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('etre', 'NN')
('is', 'VBZ')
('age', 'NN')
('etre', 'NN')
('is', 'VBZ')
('gender', 'NN')
('etre', 'NN')
('is', 'VBZ')
('experience', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('people', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('s', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('services', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('decade', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('population', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('offering', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('age', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gender', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('experience', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('smiles', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('people', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('s', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('faces', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('world', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('services', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('decade', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('strategy', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gaming', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('population', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('offering', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('products', 'NNS')
('entertainment', 'NN')
('is', 'VBZ')
('everyone', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('regardless', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('age', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('gender', 'NN')
('entertainment', 'NN')
('is', 'VBZ')
('experience', 'NN')
('belief', 'NN')
('expanding', 'VBG')
('gaming', 'NN')
('belief', 'NN')
('expanding', 'VBG')
('population', 'NN')
('belief', 'NN')
('expanding', 'VBG')
('offering', 'NN')
('belief', 'NN')
('expanding', 'VBG')
('everyone', 'NN')
('belief', 'NN')
('expanding', 'VBG')
('regardless', 'NN')
('belief', 'NN')
('expanding', 'VBG')
('age', 'NN')
('belief', 'NN')
('expanding', 'VBG')
('gender', 'NN')
('belief', 'NN')
('expanding', 'VBG')
('experience', 'NN')
('raison', 'NN')
('expanding', 'VBG')
('gaming', 'NN')
('raison', 'NN')
('expanding', 'VBG')
('population', 'NN')
('raison', 'NN')
('expanding', 'VBG')
('offering', 'NN')
('raison', 'NN')
('expanding', 'VBG')
('everyone', 'NN')
('raison', 'NN')
('expanding', 'VBG')
('regardless', 'NN')
('raison', 'NN')
('expanding', 'VBG')
('age', 'NN')
('raison', 'NN')
('expanding', 'VBG')
('gender', 'NN')
('raison', 'NN')
('expanding', 'VBG')
('experience', 'NN')
('d', 'NN')
('expanding', 'VBG')
('gaming', 'NN')
('d', 'NN')
('expanding', 'VBG')
('population', 'NN')
('d', 'NN')
('expanding', 'VBG')
('offering', 'NN')
('d', 'NN')
('expanding', 'VBG')
('everyone', 'NN')
('d', 'NN')
('expanding', 'VBG')
('regardless', 'NN')
('d', 'NN')
('expanding', 'VBG')
('age', 'NN')
('d', 'NN')
('expanding', 'VBG')
('gender', 'NN')
('d', 'NN')
('expanding', 'VBG')
('experience', 'NN')
('etre', 'NN')
('expanding', 'VBG')
('gaming', 'NN')
('etre', 'NN')
('expanding', 'VBG')
('population', 'NN')
('etre', 'NN')
('expanding', 'VBG')
('offering', 'NN')
('etre', 'NN')
('expanding', 'VBG')
('everyone', 'NN')
('etre', 'NN')
('expanding', 'VBG')
('regardless', 'NN')
('etre', 'NN')
('expanding', 'VBG')
('age', 'NN')
('etre', 'NN')
('expanding', 'VBG')
('gender', 'NN')
('etre', 'NN')
('expanding', 'VBG')
('experience', 'NN')
('entertainment', 'NN')
('expanding', 'VBG')
('gaming', 'NN')
('entertainment', 'NN')
('expanding', 'VBG')
('population', 'NN')
('entertainment', 'NN')
('expanding', 'VBG')
('offering', 'NN')
('entertainment', 'NN')
('expanding', 'VBG')
('everyone', 'NN')
('entertainment', 'NN')
('expanding', 'VBG')
('regardless', 'NN')
('entertainment', 'NN')
('expanding', 'VBG')
('age', 'NN')
('entertainment', 'NN')
('expanding', 'VBG')
('gender', 'NN')
('entertainment', 'NN')
('expanding', 'VBG')
('experience', 'NN')
('smiles', 'NNS')
('expanding', 'VBG')
('gaming', 'NN')
('smiles', 'NNS')
('expanding', 'VBG')
('population', 'NN')
('smiles', 'NNS')
('expanding', 'VBG')
('offering', 'NN')
('smiles', 'NNS')
('expanding', 'VBG')
('everyone', 'NN')
('smiles', 'NNS')
('expanding', 'VBG')
('regardless', 'NN')
('smiles', 'NNS')
('expanding', 'VBG')
('age', 'NN')
('smiles', 'NNS')
('expanding', 'VBG')
('gender', 'NN')
('smiles', 'NNS')
('expanding', 'VBG')
('experience', 'NN')
('people', 'NNS')
('expanding', 'VBG')
('gaming', 'NN')
('people', 'NNS')
('expanding', 'VBG')
('population', 'NN')
('people', 'NNS')
('expanding', 'VBG')
('offering', 'NN')
('people', 'NNS')
('expanding', 'VBG')
('everyone', 'NN')
('people', 'NNS')
('expanding', 'VBG')
('regardless', 'NN')
('people', 'NNS')
('expanding', 'VBG')
('age', 'NN')
('people', 'NNS')
('expanding', 'VBG')
('gender', 'NN')
('people', 'NNS')
('expanding', 'VBG')
('experience', 'NN')
('s', 'NNS')
('expanding', 'VBG')
('gaming', 'NN')
('s', 'NNS')
('expanding', 'VBG')
('population', 'NN')
('s', 'NNS')
('expanding', 'VBG')
('offering', 'NN')
('s', 'NNS')
('expanding', 'VBG')
('everyone', 'NN')
('s', 'NNS')
('expanding', 'VBG')
('regardless', 'NN')
('s', 'NNS')
('expanding', 'VBG')
('age', 'NN')
('s', 'NNS')
('expanding', 'VBG')
('gender', 'NN')
('s', 'NNS')
('expanding', 'VBG')
('experience', 'NN')
('faces', 'NNS')
('expanding', 'VBG')
('gaming', 'NN')
('faces', 'NNS')
('expanding', 'VBG')
('population', 'NN')
('faces', 'NNS')
('expanding', 'VBG')
('offering', 'NN')
('faces', 'NNS')
('expanding', 'VBG')
('everyone', 'NN')
('faces', 'NNS')
('expanding', 'VBG')
('regardless', 'NN')
('faces', 'NNS')
('expanding', 'VBG')
('age', 'NN')
('faces', 'NNS')
('expanding', 'VBG')
('gender', 'NN')
('faces', 'NNS')
('expanding', 'VBG')
('experience', 'NN')
('world', 'NN')
('expanding', 'VBG')
('gaming', 'NN')
('world', 'NN')
('expanding', 'VBG')
('population', 'NN')
('world', 'NN')
('expanding', 'VBG')
('offering', 'NN')
('world', 'NN')
('expanding', 'VBG')
('everyone', 'NN')
('world', 'NN')
('expanding', 'VBG')
('regardless', 'NN')
('world', 'NN')
('expanding', 'VBG')
('age', 'NN')
('world', 'NN')
('expanding', 'VBG')
('gender', 'NN')
('world', 'NN')
('expanding', 'VBG')
('experience', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('gaming', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('population', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('offering', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('everyone', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('regardless', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('age', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('gender', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('experience', 'NN')
('services', 'NNS')
('expanding', 'VBG')
('gaming', 'NN')
('services', 'NNS')
('expanding', 'VBG')
('population', 'NN')
('services', 'NNS')
('expanding', 'VBG')
('offering', 'NN')
('services', 'NNS')
('expanding', 'VBG')
('everyone', 'NN')
('services', 'NNS')
('expanding', 'VBG')
('regardless', 'NN')
('services', 'NNS')
('expanding', 'VBG')
('age', 'NN')
('services', 'NNS')
('expanding', 'VBG')
('gender', 'NN')
('services', 'NNS')
('expanding', 'VBG')
('experience', 'NN')
('decade', 'NN')
('expanding', 'VBG')
('gaming', 'NN')
('decade', 'NN')
('expanding', 'VBG')
('population', 'NN')
('decade', 'NN')
('expanding', 'VBG')
('offering', 'NN')
('decade', 'NN')
('expanding', 'VBG')
('everyone', 'NN')
('decade', 'NN')
('expanding', 'VBG')
('regardless', 'NN')
('decade', 'NN')
('expanding', 'VBG')
('age', 'NN')
('decade', 'NN')
('expanding', 'VBG')
('gender', 'NN')
('decade', 'NN')
('expanding', 'VBG')
('experience', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('gaming', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('population', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('offering', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('everyone', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('regardless', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('age', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('gender', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('experience', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('gaming', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('population', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('offering', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('everyone', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('regardless', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('age', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('gender', 'NN')
('products', 'NNS')
('expanding', 'VBG')
('experience', 'NN')
('belief', 'NN')
('be', 'VB')
('everyone', 'NN')
('belief', 'NN')
('be', 'VB')
('regardless', 'NN')
('belief', 'NN')
('be', 'VB')
('age', 'NN')
('belief', 'NN')
('be', 'VB')
('gender', 'NN')
('belief', 'NN')
('be', 'VB')
('experience', 'NN')
('raison', 'NN')
('be', 'VB')
('everyone', 'NN')
('raison', 'NN')
('be', 'VB')
('regardless', 'NN')
('raison', 'NN')
('be', 'VB')
('age', 'NN')
('raison', 'NN')
('be', 'VB')
('gender', 'NN')
('raison', 'NN')
('be', 'VB')
('experience', 'NN')
('d', 'NN')
('be', 'VB')
('everyone', 'NN')
('d', 'NN')
('be', 'VB')
('regardless', 'NN')
('d', 'NN')
('be', 'VB')
('age', 'NN')
('d', 'NN')
('be', 'VB')
('gender', 'NN')
('d', 'NN')
('be', 'VB')
('experience', 'NN')
('etre', 'NN')
('be', 'VB')
('everyone', 'NN')
('etre', 'NN')
('be', 'VB')
('regardless', 'NN')
('etre', 'NN')
('be', 'VB')
('age', 'NN')
('etre', 'NN')
('be', 'VB')
('gender', 'NN')
('etre', 'NN')
('be', 'VB')
('experience', 'NN')
('entertainment', 'NN')
('be', 'VB')
('everyone', 'NN')
('entertainment', 'NN')
('be', 'VB')
('regardless', 'NN')
('entertainment', 'NN')
('be', 'VB')
('age', 'NN')
('entertainment', 'NN')
('be', 'VB')
('gender', 'NN')
('entertainment', 'NN')
('be', 'VB')
('experience', 'NN')
('smiles', 'NNS')
('be', 'VB')
('everyone', 'NN')
('smiles', 'NNS')
('be', 'VB')
('regardless', 'NN')
('smiles', 'NNS')
('be', 'VB')
('age', 'NN')
('smiles', 'NNS')
('be', 'VB')
('gender', 'NN')
('smiles', 'NNS')
('be', 'VB')
('experience', 'NN')
('people', 'NNS')
('be', 'VB')
('everyone', 'NN')
('people', 'NNS')
('be', 'VB')
('regardless', 'NN')
('people', 'NNS')
('be', 'VB')
('age', 'NN')
('people', 'NNS')
('be', 'VB')
('gender', 'NN')
('people', 'NNS')
('be', 'VB')
('experience', 'NN')
('s', 'NNS')
('be', 'VB')
('everyone', 'NN')
('s', 'NNS')
('be', 'VB')
('regardless', 'NN')
('s', 'NNS')
('be', 'VB')
('age', 'NN')
('s', 'NNS')
('be', 'VB')
('gender', 'NN')
('s', 'NNS')
('be', 'VB')
('experience', 'NN')
('faces', 'NNS')
('be', 'VB')
('everyone', 'NN')
('faces', 'NNS')
('be', 'VB')
('regardless', 'NN')
('faces', 'NNS')
('be', 'VB')
('age', 'NN')
('faces', 'NNS')
('be', 'VB')
('gender', 'NN')
('faces', 'NNS')
('be', 'VB')
('experience', 'NN')
('world', 'NN')
('be', 'VB')
('everyone', 'NN')
('world', 'NN')
('be', 'VB')
('regardless', 'NN')
('world', 'NN')
('be', 'VB')
('age', 'NN')
('world', 'NN')
('be', 'VB')
('gender', 'NN')
('world', 'NN')
('be', 'VB')
('experience', 'NN')
('products', 'NNS')
('be', 'VB')
('everyone', 'NN')
('products', 'NNS')
('be', 'VB')
('regardless', 'NN')
('products', 'NNS')
('be', 'VB')
('age', 'NN')
('products', 'NNS')
('be', 'VB')
('gender', 'NN')
('products', 'NNS')
('be', 'VB')
('experience', 'NN')
('services', 'NNS')
('be', 'VB')
('everyone', 'NN')
('services', 'NNS')
('be', 'VB')
('regardless', 'NN')
('services', 'NNS')
('be', 'VB')
('age', 'NN')
('services', 'NNS')
('be', 'VB')
('gender', 'NN')
('services', 'NNS')
('be', 'VB')
('experience', 'NN')
('decade', 'NN')
('be', 'VB')
('everyone', 'NN')
('decade', 'NN')
('be', 'VB')
('regardless', 'NN')
('decade', 'NN')
('be', 'VB')
('age', 'NN')
('decade', 'NN')
('be', 'VB')
('gender', 'NN')
('decade', 'NN')
('be', 'VB')
('experience', 'NN')
('strategy', 'NN')
('be', 'VB')
('everyone', 'NN')
('strategy', 'NN')
('be', 'VB')
('regardless', 'NN')
('strategy', 'NN')
('be', 'VB')
('age', 'NN')
('strategy', 'NN')
('be', 'VB')
('gender', 'NN')
('strategy', 'NN')
('be', 'VB')
('experience', 'NN')
('gaming', 'NN')
('be', 'VB')
('everyone', 'NN')
('gaming', 'NN')
('be', 'VB')
('regardless', 'NN')
('gaming', 'NN')
('be', 'VB')
('age', 'NN')
('gaming', 'NN')
('be', 'VB')
('gender', 'NN')
('gaming', 'NN')
('be', 'VB')
('experience', 'NN')
('population', 'NN')
('be', 'VB')
('everyone', 'NN')
('population', 'NN')
('be', 'VB')
('regardless', 'NN')
('population', 'NN')
('be', 'VB')
('age', 'NN')
('population', 'NN')
('be', 'VB')
('gender', 'NN')
('population', 'NN')
('be', 'VB')
('experience', 'NN')
('offering', 'NN')
('be', 'VB')
('everyone', 'NN')
('offering', 'NN')
('be', 'VB')
('regardless', 'NN')
('offering', 'NN')
('be', 'VB')
('age', 'NN')
('offering', 'NN')
('be', 'VB')
('gender', 'NN')
('offering', 'NN')
('be', 'VB')
('experience', 'NN')
('products', 'NNS')
('be', 'VB')
('everyone', 'NN')
('products', 'NNS')
('be', 'VB')
('regardless', 'NN')
('products', 'NNS')
('be', 'VB')
('age', 'NN')
('products', 'NNS')
('be', 'VB')
('gender', 'NN')
('products', 'NNS')
('be', 'VB')
('experience', 'NN')
('belief', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('belief', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('belief', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('belief', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('belief', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('raison', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('raison', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('raison', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('raison', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('raison', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('d', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('d', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('d', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('d', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('d', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('etre', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('etre', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('etre', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('etre', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('etre', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('entertainment', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('entertainment', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('entertainment', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('entertainment', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('entertainment', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('smiles', 'NNS')
('enjoyed', 'VBN')
('everyone', 'NN')
('smiles', 'NNS')
('enjoyed', 'VBN')
('regardless', 'NN')
('smiles', 'NNS')
('enjoyed', 'VBN')
('age', 'NN')
('smiles', 'NNS')
('enjoyed', 'VBN')
('gender', 'NN')
('smiles', 'NNS')
('enjoyed', 'VBN')
('experience', 'NN')
('people', 'NNS')
('enjoyed', 'VBN')
('everyone', 'NN')
('people', 'NNS')
('enjoyed', 'VBN')
('regardless', 'NN')
('people', 'NNS')
('enjoyed', 'VBN')
('age', 'NN')
('people', 'NNS')
('enjoyed', 'VBN')
('gender', 'NN')
('people', 'NNS')
('enjoyed', 'VBN')
('experience', 'NN')
('s', 'NNS')
('enjoyed', 'VBN')
('everyone', 'NN')
('s', 'NNS')
('enjoyed', 'VBN')
('regardless', 'NN')
('s', 'NNS')
('enjoyed', 'VBN')
('age', 'NN')
('s', 'NNS')
('enjoyed', 'VBN')
('gender', 'NN')
('s', 'NNS')
('enjoyed', 'VBN')
('experience', 'NN')
('faces', 'NNS')
('enjoyed', 'VBN')
('everyone', 'NN')
('faces', 'NNS')
('enjoyed', 'VBN')
('regardless', 'NN')
('faces', 'NNS')
('enjoyed', 'VBN')
('age', 'NN')
('faces', 'NNS')
('enjoyed', 'VBN')
('gender', 'NN')
('faces', 'NNS')
('enjoyed', 'VBN')
('experience', 'NN')
('world', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('world', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('world', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('world', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('world', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('everyone', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('regardless', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('age', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('gender', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('experience', 'NN')
('services', 'NNS')
('enjoyed', 'VBN')
('everyone', 'NN')
('services', 'NNS')
('enjoyed', 'VBN')
('regardless', 'NN')
('services', 'NNS')
('enjoyed', 'VBN')
('age', 'NN')
('services', 'NNS')
('enjoyed', 'VBN')
('gender', 'NN')
('services', 'NNS')
('enjoyed', 'VBN')
('experience', 'NN')
('decade', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('decade', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('decade', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('decade', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('decade', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('strategy', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('strategy', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('strategy', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('strategy', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('strategy', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('gaming', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('gaming', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('gaming', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('gaming', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('gaming', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('population', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('population', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('population', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('population', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('population', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('offering', 'NN')
('enjoyed', 'VBN')
('everyone', 'NN')
('offering', 'NN')
('enjoyed', 'VBN')
('regardless', 'NN')
('offering', 'NN')
('enjoyed', 'VBN')
('age', 'NN')
('offering', 'NN')
('enjoyed', 'VBN')
('gender', 'NN')
('offering', 'NN')
('enjoyed', 'VBN')
('experience', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('everyone', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('regardless', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('age', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('gender', 'NN')
('products', 'NNS')
('enjoyed', 'VBN')
('experience', 'NN')
('belief', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('raison', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('d', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('etre', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('entertainment', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('smiles', 'NNS')
('gaming', 'VBG')
('experience', 'NN')
('people', 'NNS')
('gaming', 'VBG')
('experience', 'NN')
('s', 'NNS')
('gaming', 'VBG')
('experience', 'NN')
('faces', 'NNS')
('gaming', 'VBG')
('experience', 'NN')
('world', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('products', 'NNS')
('gaming', 'VBG')
('experience', 'NN')
('services', 'NNS')
('gaming', 'VBG')
('experience', 'NN')
('decade', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('strategy', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('gaming', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('population', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('offering', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('products', 'NNS')
('gaming', 'VBG')
('experience', 'NN')
('everyone', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('regardless', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('age', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('gender', 'NN')
('gaming', 'VBG')
('experience', 'NN')
('addition', 'NN')
('has', 'VBZ')
('times', 'NNS')
('addition', 'NN')
('has', 'VBZ')
('entertainment', 'NN')
('addition', 'NN')
('has', 'VBZ')
('something', 'NN')
('addition', 'NN')
('has', 'VBZ')
('improves', 'NNS')
('addition', 'NN')
('has', 'VBZ')
('people', 'NNS')
('addition', 'NN')
('has', 'VBZ')
('s', 'NNS')
('addition', 'NN')
('has', 'VBZ')
('quality', 'NN')
('addition', 'NN')
('has', 'VBZ')
('life', 'NN')
('addition', 'NN')
('has', 'VBZ')
('QOL', 'NNP')
('addition', 'NN')
('has', 'VBZ')
('ways', 'NNS')
('addition', 'NN')
('has', 'VBZ')
('expand', 'NN')
('addition', 'NN')
('has', 'VBZ')
('areas', 'NNS')
('business', 'NN')
('has', 'VBZ')
('times', 'NNS')
('business', 'NN')
('has', 'VBZ')
('entertainment', 'NN')
('business', 'NN')
('has', 'VBZ')
('something', 'NN')
('business', 'NN')
('has', 'VBZ')
('improves', 'NNS')
('business', 'NN')
('has', 'VBZ')
('people', 'NNS')
('business', 'NN')
('has', 'VBZ')
('s', 'NNS')
('business', 'NN')
('has', 'VBZ')
('quality', 'NN')
('business', 'NN')
('has', 'VBZ')
('life', 'NN')
('business', 'NN')
('has', 'VBZ')
('QOL', 'NNP')
('business', 'NN')
('has', 'VBZ')
('ways', 'NNS')
('business', 'NN')
('has', 'VBZ')
('expand', 'NN')
('business', 'NN')
('has', 'VBZ')
('areas', 'NNS')
('environment', 'NN')
('has', 'VBZ')
('times', 'NNS')
('environment', 'NN')
('has', 'VBZ')
('entertainment', 'NN')
('environment', 'NN')
('has', 'VBZ')
('something', 'NN')
('environment', 'NN')
('has', 'VBZ')
('improves', 'NNS')
('environment', 'NN')
('has', 'VBZ')
('people', 'NNS')
('environment', 'NN')
('has', 'VBZ')
('s', 'NNS')
('environment', 'NN')
('has', 'VBZ')
('quality', 'NN')
('environment', 'NN')
('has', 'VBZ')
('life', 'NN')
('environment', 'NN')
('has', 'VBZ')
('QOL', 'NNP')
('environment', 'NN')
('has', 'VBZ')
('ways', 'NNS')
('environment', 'NN')
('has', 'VBZ')
('expand', 'NN')
('environment', 'NN')
('has', 'VBZ')
('areas', 'NNS')
('business', 'NN')
('has', 'VBZ')
('times', 'NNS')
('business', 'NN')
('has', 'VBZ')
('entertainment', 'NN')
('business', 'NN')
('has', 'VBZ')
('something', 'NN')
('business', 'NN')
('has', 'VBZ')
('improves', 'NNS')
('business', 'NN')
('has', 'VBZ')
('people', 'NNS')
('business', 'NN')
('has', 'VBZ')
('s', 'NNS')
('business', 'NN')
('has', 'VBZ')
('quality', 'NN')
('business', 'NN')
('has', 'VBZ')
('life', 'NN')
('business', 'NN')
('has', 'VBZ')
('QOL', 'NNP')
('business', 'NN')
('has', 'VBZ')
('ways', 'NNS')
('business', 'NN')
('has', 'VBZ')
('expand', 'NN')
('business', 'NN')
('has', 'VBZ')
('areas', 'NNS')
('addition', 'NN')
('shifted', 'VBN')
('times', 'NNS')
('addition', 'NN')
('shifted', 'VBN')
('entertainment', 'NN')
('addition', 'NN')
('shifted', 'VBN')
('something', 'NN')
('addition', 'NN')
('shifted', 'VBN')
('improves', 'NNS')
('addition', 'NN')
('shifted', 'VBN')
('people', 'NNS')
('addition', 'NN')
('shifted', 'VBN')
('s', 'NNS')
('addition', 'NN')
('shifted', 'VBN')
('quality', 'NN')
('addition', 'NN')
('shifted', 'VBN')
('life', 'NN')
('addition', 'NN')
('shifted', 'VBN')
('QOL', 'NNP')
('addition', 'NN')
('shifted', 'VBN')
('ways', 'NNS')
('addition', 'NN')
('shifted', 'VBN')
('expand', 'NN')
('addition', 'NN')
('shifted', 'VBN')
('areas', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('times', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('entertainment', 'NN')
('business', 'NN')
('shifted', 'VBN')
('something', 'NN')
('business', 'NN')
('shifted', 'VBN')
('improves', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('people', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('s', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('quality', 'NN')
('business', 'NN')
('shifted', 'VBN')
('life', 'NN')
('business', 'NN')
('shifted', 'VBN')
('QOL', 'NNP')
('business', 'NN')
('shifted', 'VBN')
('ways', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('expand', 'NN')
('business', 'NN')
('shifted', 'VBN')
('areas', 'NNS')
('environment', 'NN')
('shifted', 'VBN')
('times', 'NNS')
('environment', 'NN')
('shifted', 'VBN')
('entertainment', 'NN')
('environment', 'NN')
('shifted', 'VBN')
('something', 'NN')
('environment', 'NN')
('shifted', 'VBN')
('improves', 'NNS')
('environment', 'NN')
('shifted', 'VBN')
('people', 'NNS')
('environment', 'NN')
('shifted', 'VBN')
('s', 'NNS')
('environment', 'NN')
('shifted', 'VBN')
('quality', 'NN')
('environment', 'NN')
('shifted', 'VBN')
('life', 'NN')
('environment', 'NN')
('shifted', 'VBN')
('QOL', 'NNP')
('environment', 'NN')
('shifted', 'VBN')
('ways', 'NNS')
('environment', 'NN')
('shifted', 'VBN')
('expand', 'NN')
('environment', 'NN')
('shifted', 'VBN')
('areas', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('times', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('entertainment', 'NN')
('business', 'NN')
('shifted', 'VBN')
('something', 'NN')
('business', 'NN')
('shifted', 'VBN')
('improves', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('people', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('s', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('quality', 'NN')
('business', 'NN')
('shifted', 'VBN')
('life', 'NN')
('business', 'NN')
('shifted', 'VBN')
('QOL', 'NNP')
('business', 'NN')
('shifted', 'VBN')
('ways', 'NNS')
('business', 'NN')
('shifted', 'VBN')
('expand', 'NN')
('business', 'NN')
('shifted', 'VBN')
('areas', 'NNS')
('addition', 'NN')
('have', 'VBP')
('entertainment', 'NN')
('addition', 'NN')
('have', 'VBP')
('something', 'NN')
('addition', 'NN')
('have', 'VBP')
('improves', 'NNS')
('addition', 'NN')
('have', 'VBP')
('people', 'NNS')
('addition', 'NN')
('have', 'VBP')
('s', 'NNS')
('addition', 'NN')
('have', 'VBP')
('quality', 'NN')
('addition', 'NN')
('have', 'VBP')
('life', 'NN')
('addition', 'NN')
('have', 'VBP')
('QOL', 'NNP')
('addition', 'NN')
('have', 'VBP')
('ways', 'NNS')
('addition', 'NN')
('have', 'VBP')
('expand', 'NN')
('addition', 'NN')
('have', 'VBP')
('areas', 'NNS')
('business', 'NN')
('have', 'VBP')
('entertainment', 'NN')
('business', 'NN')
('have', 'VBP')
('something', 'NN')
('business', 'NN')
('have', 'VBP')
('improves', 'NNS')
('business', 'NN')
('have', 'VBP')
('people', 'NNS')
('business', 'NN')
('have', 'VBP')
('s', 'NNS')
('business', 'NN')
('have', 'VBP')
('quality', 'NN')
('business', 'NN')
('have', 'VBP')
('life', 'NN')
('business', 'NN')
('have', 'VBP')
('QOL', 'NNP')
('business', 'NN')
('have', 'VBP')
('ways', 'NNS')
('business', 'NN')
('have', 'VBP')
('expand', 'NN')
('business', 'NN')
('have', 'VBP')
('areas', 'NNS')
('environment', 'NN')
('have', 'VBP')
('entertainment', 'NN')
('environment', 'NN')
('have', 'VBP')
('something', 'NN')
('environment', 'NN')
('have', 'VBP')
('improves', 'NNS')
('environment', 'NN')
('have', 'VBP')
('people', 'NNS')
('environment', 'NN')
('have', 'VBP')
('s', 'NNS')
('environment', 'NN')
('have', 'VBP')
('quality', 'NN')
('environment', 'NN')
('have', 'VBP')
('life', 'NN')
('environment', 'NN')
('have', 'VBP')
('QOL', 'NNP')
('environment', 'NN')
('have', 'VBP')
('ways', 'NNS')
('environment', 'NN')
('have', 'VBP')
('expand', 'NN')
('environment', 'NN')
('have', 'VBP')
('areas', 'NNS')
('times', 'NNS')
('have', 'VBP')
('entertainment', 'NN')
('times', 'NNS')
('have', 'VBP')
('something', 'NN')
('times', 'NNS')
('have', 'VBP')
('improves', 'NNS')
('times', 'NNS')
('have', 'VBP')
('people', 'NNS')
('times', 'NNS')
('have', 'VBP')
('s', 'NNS')
('times', 'NNS')
('have', 'VBP')
('quality', 'NN')
('times', 'NNS')
('have', 'VBP')
('life', 'NN')
('times', 'NNS')
('have', 'VBP')
('QOL', 'NNP')
('times', 'NNS')
('have', 'VBP')
('ways', 'NNS')
('times', 'NNS')
('have', 'VBP')
('expand', 'NN')
('times', 'NNS')
('have', 'VBP')
('areas', 'NNS')
('business', 'NN')
('have', 'VBP')
('entertainment', 'NN')
('business', 'NN')
('have', 'VBP')
('something', 'NN')
('business', 'NN')
('have', 'VBP')
('improves', 'NNS')
('business', 'NN')
('have', 'VBP')
('people', 'NNS')
('business', 'NN')
('have', 'VBP')
('s', 'NNS')
('business', 'NN')
('have', 'VBP')
('quality', 'NN')
('business', 'NN')
('have', 'VBP')
('life', 'NN')
('business', 'NN')
('have', 'VBP')
('QOL', 'NNP')
('business', 'NN')
('have', 'VBP')
('ways', 'NNS')
('business', 'NN')
('have', 'VBP')
('expand', 'NN')
('business', 'NN')
('have', 'VBP')
('areas', 'NNS')
('addition', 'NN')
('decided', 'VBN')
('entertainment', 'NN')
('addition', 'NN')
('decided', 'VBN')
('something', 'NN')
('addition', 'NN')
('decided', 'VBN')
('improves', 'NNS')
('addition', 'NN')
('decided', 'VBN')
('people', 'NNS')
('addition', 'NN')
('decided', 'VBN')
('s', 'NNS')
('addition', 'NN')
('decided', 'VBN')
('quality', 'NN')
('addition', 'NN')
('decided', 'VBN')
('life', 'NN')
('addition', 'NN')
('decided', 'VBN')
('QOL', 'NNP')
('addition', 'NN')
('decided', 'VBN')
('ways', 'NNS')
('addition', 'NN')
('decided', 'VBN')
('expand', 'NN')
('addition', 'NN')
('decided', 'VBN')
('areas', 'NNS')
('business', 'NN')
('decided', 'VBN')
('entertainment', 'NN')
('business', 'NN')
('decided', 'VBN')
('something', 'NN')
('business', 'NN')
('decided', 'VBN')
('improves', 'NNS')
('business', 'NN')
('decided', 'VBN')
('people', 'NNS')
('business', 'NN')
('decided', 'VBN')
('s', 'NNS')
('business', 'NN')
('decided', 'VBN')
('quality', 'NN')
('business', 'NN')
('decided', 'VBN')
('life', 'NN')
('business', 'NN')
('decided', 'VBN')
('QOL', 'NNP')
('business', 'NN')
('decided', 'VBN')
('ways', 'NNS')
('business', 'NN')
('decided', 'VBN')
('expand', 'NN')
('business', 'NN')
('decided', 'VBN')
('areas', 'NNS')
('environment', 'NN')
('decided', 'VBN')
('entertainment', 'NN')
('environment', 'NN')
('decided', 'VBN')
('something', 'NN')
('environment', 'NN')
('decided', 'VBN')
('improves', 'NNS')
('environment', 'NN')
('decided', 'VBN')
('people', 'NNS')
('environment', 'NN')
('decided', 'VBN')
('s', 'NNS')
('environment', 'NN')
('decided', 'VBN')
('quality', 'NN')
('environment', 'NN')
('decided', 'VBN')
('life', 'NN')
('environment', 'NN')
('decided', 'VBN')
('QOL', 'NNP')
('environment', 'NN')
('decided', 'VBN')
('ways', 'NNS')
('environment', 'NN')
('decided', 'VBN')
('expand', 'NN')
('environment', 'NN')
('decided', 'VBN')
('areas', 'NNS')
('times', 'NNS')
('decided', 'VBN')
('entertainment', 'NN')
('times', 'NNS')
('decided', 'VBN')
('something', 'NN')
('times', 'NNS')
('decided', 'VBN')
('improves', 'NNS')
('times', 'NNS')
('decided', 'VBN')
('people', 'NNS')
('times', 'NNS')
('decided', 'VBN')
('s', 'NNS')
('times', 'NNS')
('decided', 'VBN')
('quality', 'NN')
('times', 'NNS')
('decided', 'VBN')
('life', 'NN')
('times', 'NNS')
('decided', 'VBN')
('QOL', 'NNP')
('times', 'NNS')
('decided', 'VBN')
('ways', 'NNS')
('times', 'NNS')
('decided', 'VBN')
('expand', 'NN')
('times', 'NNS')
('decided', 'VBN')
('areas', 'NNS')
('business', 'NN')
('decided', 'VBN')
('entertainment', 'NN')
('business', 'NN')
('decided', 'VBN')
('something', 'NN')
('business', 'NN')
('decided', 'VBN')
('improves', 'NNS')
('business', 'NN')
('decided', 'VBN')
('people', 'NNS')
('business', 'NN')
('decided', 'VBN')
('s', 'NNS')
('business', 'NN')
('decided', 'VBN')
('quality', 'NN')
('business', 'NN')
('decided', 'VBN')
('life', 'NN')
('business', 'NN')
('decided', 'VBN')
('QOL', 'NNP')
('business', 'NN')
('decided', 'VBN')
('ways', 'NNS')
('business', 'NN')
('decided', 'VBN')
('expand', 'NN')
('business', 'NN')
('decided', 'VBN')
('areas', 'NNS')
('addition', 'NN')
('redefine', 'VB')
('entertainment', 'NN')
('addition', 'NN')
('redefine', 'VB')
('something', 'NN')
('addition', 'NN')
('redefine', 'VB')
('improves', 'NNS')
('addition', 'NN')
('redefine', 'VB')
('people', 'NNS')
('addition', 'NN')
('redefine', 'VB')
('s', 'NNS')
('addition', 'NN')
('redefine', 'VB')
('quality', 'NN')
('addition', 'NN')
('redefine', 'VB')
('life', 'NN')
('addition', 'NN')
('redefine', 'VB')
('QOL', 'NNP')
('addition', 'NN')
('redefine', 'VB')
('ways', 'NNS')
('addition', 'NN')
('redefine', 'VB')
('expand', 'NN')
('addition', 'NN')
('redefine', 'VB')
('areas', 'NNS')
('business', 'NN')
('redefine', 'VB')
('entertainment', 'NN')
('business', 'NN')
('redefine', 'VB')
('something', 'NN')
('business', 'NN')
('redefine', 'VB')
('improves', 'NNS')
('business', 'NN')
('redefine', 'VB')
('people', 'NNS')
('business', 'NN')
('redefine', 'VB')
('s', 'NNS')
('business', 'NN')
('redefine', 'VB')
('quality', 'NN')
('business', 'NN')
('redefine', 'VB')
('life', 'NN')
('business', 'NN')
('redefine', 'VB')
('QOL', 'NNP')
('business', 'NN')
('redefine', 'VB')
('ways', 'NNS')
('business', 'NN')
('redefine', 'VB')
('expand', 'NN')
('business', 'NN')
('redefine', 'VB')
('areas', 'NNS')
('environment', 'NN')
('redefine', 'VB')
('entertainment', 'NN')
('environment', 'NN')
('redefine', 'VB')
('something', 'NN')
('environment', 'NN')
('redefine', 'VB')
('improves', 'NNS')
('environment', 'NN')
('redefine', 'VB')
('people', 'NNS')
('environment', 'NN')
('redefine', 'VB')
('s', 'NNS')
('environment', 'NN')
('redefine', 'VB')
('quality', 'NN')
('environment', 'NN')
('redefine', 'VB')
('life', 'NN')
('environment', 'NN')
('redefine', 'VB')
('QOL', 'NNP')
('environment', 'NN')
('redefine', 'VB')
('ways', 'NNS')
('environment', 'NN')
('redefine', 'VB')
('expand', 'NN')
('environment', 'NN')
('redefine', 'VB')
('areas', 'NNS')
('times', 'NNS')
('redefine', 'VB')
('entertainment', 'NN')
('times', 'NNS')
('redefine', 'VB')
('something', 'NN')
('times', 'NNS')
('redefine', 'VB')
('improves', 'NNS')
('times', 'NNS')
('redefine', 'VB')
('people', 'NNS')
('times', 'NNS')
('redefine', 'VB')
('s', 'NNS')
('times', 'NNS')
('redefine', 'VB')
('quality', 'NN')
('times', 'NNS')
('redefine', 'VB')
('life', 'NN')
('times', 'NNS')
('redefine', 'VB')
('QOL', 'NNP')
('times', 'NNS')
('redefine', 'VB')
('ways', 'NNS')
('times', 'NNS')
('redefine', 'VB')
('expand', 'NN')
('times', 'NNS')
('redefine', 'VB')
('areas', 'NNS')
('business', 'NN')
('redefine', 'VB')
('entertainment', 'NN')
('business', 'NN')
('redefine', 'VB')
('something', 'NN')
('business', 'NN')
('redefine', 'VB')
('improves', 'NNS')
('business', 'NN')
('redefine', 'VB')
('people', 'NNS')
('business', 'NN')
('redefine', 'VB')
('s', 'NNS')
('business', 'NN')
('redefine', 'VB')
('quality', 'NN')
('business', 'NN')
('redefine', 'VB')
('life', 'NN')
('business', 'NN')
('redefine', 'VB')
('QOL', 'NNP')
('business', 'NN')
('redefine', 'VB')
('ways', 'NNS')
('business', 'NN')
('redefine', 'VB')
('expand', 'NN')
('business', 'NN')
('redefine', 'VB')
('areas', 'NNS')
('Nintendo', 'NNP')
('try', 'VB')
('years', 'NNS')
('Nintendo', 'NNP')
('try', 'VB')
('platform', 'NN')
('Nintendo', 'NNP')
('try', 'VB')
('business', 'NN')
('Nintendo', 'NNP')
('try', 'VB')
('people', 'NNS')
('Nintendo', 'NNP')
('try', 'VB')
('s', 'NNS')
('Nintendo', 'NNP')
('try', 'VB')
('QOL', 'NNP')
('Nintendo', 'NNP')
('try', 'VB')
('ways', 'NNS')
('Nintendo', 'NNP')
('achieve', 'VB')
('years', 'NNS')
('Nintendo', 'NNP')
('achieve', 'VB')
('platform', 'NN')
('Nintendo', 'NNP')
('achieve', 'VB')
('business', 'NN')
('Nintendo', 'NNP')
('achieve', 'VB')
('people', 'NNS')
('Nintendo', 'NNP')
('achieve', 'VB')
('s', 'NNS')
('Nintendo', 'NNP')
('achieve', 'VB')
('QOL', 'NNP')
('Nintendo', 'NNP')
('achieve', 'VB')
('ways', 'NNS')
('Nintendo', 'NNP')
('is', 'VBZ')
('platform', 'NN')
('Nintendo', 'NNP')
('is', 'VBZ')
('business', 'NN')
('Nintendo', 'NNP')
('is', 'VBZ')
('people', 'NNS')
('Nintendo', 'NNP')
('is', 'VBZ')
('s', 'NNS')
('Nintendo', 'NNP')
('is', 'VBZ')
('QOL', 'NNP')
('Nintendo', 'NNP')
('is', 'VBZ')
('ways', 'NNS')
('years', 'NNS')
('is', 'VBZ')
('platform', 'NN')
('years', 'NNS')
('is', 'VBZ')
('business', 'NN')
('years', 'NNS')
('is', 'VBZ')
('people', 'NNS')
('years', 'NNS')
('is', 'VBZ')
('s', 'NNS')
('years', 'NNS')
('is', 'VBZ')
('QOL', 'NNP')
('years', 'NNS')
('is', 'VBZ')
('ways', 'NNS')
('Nintendo', 'NNP')
('improves', 'VBZ')
('people', 'NNS')
('Nintendo', 'NNP')
('improves', 'VBZ')
('s', 'NNS')
('Nintendo', 'NNP')
('improves', 'VBZ')
('QOL', 'NNP')
('Nintendo', 'NNP')
('improves', 'VBZ')
('ways', 'NNS')
('years', 'NNS')
('improves', 'VBZ')
('people', 'NNS')
('years', 'NNS')
('improves', 'VBZ')
('s', 'NNS')
('years', 'NNS')
('improves', 'VBZ')
('QOL', 'NNP')
('years', 'NNS')
('improves', 'VBZ')
('ways', 'NNS')
('platform', 'NN')
('improves', 'VBZ')
('people', 'NNS')
('platform', 'NN')
('improves', 'VBZ')
('s', 'NNS')
('platform', 'NN')
('improves', 'VBZ')
('QOL', 'NNP')
('platform', 'NN')
('improves', 'VBZ')
('ways', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('people', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('s', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('QOL', 'NNP')
('business', 'NN')
('improves', 'VBZ')
('ways', 'NNS')
('strengths', 'NNS')
('integrated', 'VBD')
('platform', 'NN')
('strengths', 'NNS')
('integrated', 'VBD')
('business', 'NN')
('strengths', 'NNS')
('integrated', 'VBD')
('type', 'NN')
('strengths', 'NNS')
('integrated', 'VBD')
('video', 'NN')
('strengths', 'NNS')
('integrated', 'VBD')
('game', 'NN')
('strengths', 'NNS')
('integrated', 'VBD')
('platforms', 'NNS')
('strengths', 'NNS')
('integrated', 'VBD')
('core', 'NN')
('strengths', 'NNS')
('integrated', 'VBD')
('focus', 'NN')
('hardware', 'NN')
('integrated', 'VBD')
('platform', 'NN')
('hardware', 'NN')
('integrated', 'VBD')
('business', 'NN')
('hardware', 'NN')
('integrated', 'VBD')
('type', 'NN')
('hardware', 'NN')
('integrated', 'VBD')
('video', 'NN')
('hardware', 'NN')
('integrated', 'VBD')
('game', 'NN')
('hardware', 'NN')
('integrated', 'VBD')
('platforms', 'NNS')
('hardware', 'NN')
('integrated', 'VBD')
('core', 'NN')
('hardware', 'NN')
('integrated', 'VBD')
('focus', 'NN')
('software', 'NN')
('integrated', 'VBD')
('platform', 'NN')
('software', 'NN')
('integrated', 'VBD')
('business', 'NN')
('software', 'NN')
('integrated', 'VBD')
('type', 'NN')
('software', 'NN')
('integrated', 'VBD')
('video', 'NN')
('software', 'NN')
('integrated', 'VBD')
('game', 'NN')
('software', 'NN')
('integrated', 'VBD')
('platforms', 'NNS')
('software', 'NN')
('integrated', 'VBD')
('core', 'NN')
('software', 'NN')
('integrated', 'VBD')
('focus', 'NN')
('strengths', 'NNS')
('dedicated', 'VBN')
('video', 'NN')
('strengths', 'NNS')
('dedicated', 'VBN')
('game', 'NN')
('strengths', 'NNS')
('dedicated', 'VBN')
('platforms', 'NNS')
('strengths', 'NNS')
('dedicated', 'VBN')
('core', 'NN')
('strengths', 'NNS')
('dedicated', 'VBN')
('focus', 'NN')
('hardware', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('hardware', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('hardware', 'NN')
('dedicated', 'VBN')
('platforms', 'NNS')
('hardware', 'NN')
('dedicated', 'VBN')
('core', 'NN')
('hardware', 'NN')
('dedicated', 'VBN')
('focus', 'NN')
('software', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('software', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('software', 'NN')
('dedicated', 'VBN')
('platforms', 'NNS')
('software', 'NN')
('dedicated', 'VBN')
('core', 'NN')
('software', 'NN')
('dedicated', 'VBN')
('focus', 'NN')
('platform', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('platform', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('platform', 'NN')
('dedicated', 'VBN')
('platforms', 'NNS')
('platform', 'NN')
('dedicated', 'VBN')
('core', 'NN')
('platform', 'NN')
('dedicated', 'VBN')
('focus', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('platforms', 'NNS')
('business', 'NN')
('dedicated', 'VBN')
('core', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('focus', 'NN')
('type', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('type', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('type', 'NN')
('dedicated', 'VBN')
('platforms', 'NNS')
('type', 'NN')
('dedicated', 'VBN')
('core', 'NN')
('type', 'NN')
('dedicated', 'VBN')
('focus', 'NN')
('strengths', 'NNS')
('remain', 'VB')
('core', 'NN')
('strengths', 'NNS')
('remain', 'VB')
('focus', 'NN')
('hardware', 'NN')
('remain', 'VB')
('core', 'NN')
('hardware', 'NN')
('remain', 'VB')
('focus', 'NN')
('software', 'NN')
('remain', 'VB')
('core', 'NN')
('software', 'NN')
('remain', 'VB')
('focus', 'NN')
('platform', 'NN')
('remain', 'VB')
('core', 'NN')
('platform', 'NN')
('remain', 'VB')
('focus', 'NN')
('business', 'NN')
('remain', 'VB')
('core', 'NN')
('business', 'NN')
('remain', 'VB')
('focus', 'NN')
('type', 'NN')
('remain', 'VB')
('core', 'NN')
('type', 'NN')
('remain', 'VB')
('focus', 'NN')
('video', 'NN')
('remain', 'VB')
('core', 'NN')
('video', 'NN')
('remain', 'VB')
('focus', 'NN')
('game', 'NN')
('remain', 'VB')
('core', 'NN')
('game', 'NN')
('remain', 'VB')
('focus', 'NN')
('platforms', 'NNS')
('remain', 'VB')
('core', 'NN')
('platforms', 'NNS')
('remain', 'VB')
('focus', 'NN')
('spirit', 'NN')
('described', 'VBN')
('motto', 'NN')
('spirit', 'NN')
('described', 'VBN')
('True', 'NNP')
('spirit', 'NN')
('described', 'VBN')
('Value', 'NNP')
('spirit', 'NN')
('described', 'VBN')
('Entertainment', 'NNP')
('spirit', 'NN')
('described', 'VBN')
('Lies', 'NNPS')
('spirit', 'NN')
('described', 'VBN')
('Individuality', 'NNP')
('spirit', 'NN')
('described', 'VBN')
(',"', 'NNP')
('spirit', 'NN')
('described', 'VBN')
('products', 'NNS')
('spirit', 'NN')
('described', 'VBN')
('services', 'NNS')
('spirit', 'NN')
('described', 'VBN')
('people', 'NNS')
('originality', 'NN')
('described', 'VBN')
('motto', 'NN')
('originality', 'NN')
('described', 'VBN')
('True', 'NNP')
('originality', 'NN')
('described', 'VBN')
('Value', 'NNP')
('originality', 'NN')
('described', 'VBN')
('Entertainment', 'NNP')
('originality', 'NN')
('described', 'VBN')
('Lies', 'NNPS')
('originality', 'NN')
('described', 'VBN')
('Individuality', 'NNP')
('originality', 'NN')
('described', 'VBN')
(',"', 'NNP')
('originality', 'NN')
('described', 'VBN')
('products', 'NNS')
('originality', 'NN')
('described', 'VBN')
('services', 'NNS')
('originality', 'NN')
('described', 'VBN')
('people', 'NNS')
('spirit', 'NN')
('provide', 'VB')
('products', 'NNS')
('spirit', 'NN')
('provide', 'VB')
('services', 'NNS')
('spirit', 'NN')
('provide', 'VB')
('people', 'NNS')
('originality', 'NN')
('provide', 'VB')
('products', 'NNS')
('originality', 'NN')
('provide', 'VB')
('services', 'NNS')
('originality', 'NN')
('provide', 'VB')
('people', 'NNS')
('motto', 'NN')
('provide', 'VB')
('products', 'NNS')
('motto', 'NN')
('provide', 'VB')
('services', 'NNS')
('motto', 'NN')
('provide', 'VB')
('people', 'NNS')
('True', 'NNP')
('provide', 'VB')
('products', 'NNS')
('True', 'NNP')
('provide', 'VB')
('services', 'NNS')
('True', 'NNP')
('provide', 'VB')
('people', 'NNS')
('Value', 'NNP')
('provide', 'VB')
('products', 'NNS')
('Value', 'NNP')
('provide', 'VB')
('services', 'NNS')
('Value', 'NNP')
('provide', 'VB')
('people', 'NNS')
('Entertainment', 'NNP')
('provide', 'VB')
('products', 'NNS')
('Entertainment', 'NNP')
('provide', 'VB')
('services', 'NNS')
('Entertainment', 'NNP')
('provide', 'VB')
('people', 'NNS')
('Lies', 'NNPS')
('provide', 'VB')
('products', 'NNS')
('Lies', 'NNPS')
('provide', 'VB')
('services', 'NNS')
('Lies', 'NNPS')
('provide', 'VB')
('people', 'NNS')
('Individuality', 'NNP')
('provide', 'VB')
('products', 'NNS')
('Individuality', 'NNP')
('provide', 'VB')
('services', 'NNS')
('Individuality', 'NNP')
('provide', 'VB')
('people', 'NNS')
(',"', 'NNP')
('provide', 'VB')
('products', 'NNS')
(',"', 'NNP')
('provide', 'VB')
('services', 'NNS')
(',"', 'NNP')
('provide', 'VB')
('people', 'NNS')
('spirit', 'NN')
('surprise', 'VBP')
('people', 'NNS')
('originality', 'NN')
('surprise', 'VBP')
('people', 'NNS')
('motto', 'NN')
('surprise', 'VBP')
('people', 'NNS')
('True', 'NNP')
('surprise', 'VBP')
('people', 'NNS')
('Value', 'NNP')
('surprise', 'VBP')
('people', 'NNS')
('Entertainment', 'NNP')
('surprise', 'VBP')
('people', 'NNS')
('Lies', 'NNPS')
('surprise', 'VBP')
('people', 'NNS')
('Individuality', 'NNP')
('surprise', 'VBP')
('people', 'NNS')
(',"', 'NNP')
('surprise', 'VBP')
('people', 'NNS')
('products', 'NNS')
('surprise', 'VBP')
('people', 'NNS')
('services', 'NNS')
('surprise', 'VBP')
('people', 'NNS')
('platform', 'NN')
('improves', 'VBZ')
('people', 'NNS')
('platform', 'NN')
('improves', 'VBZ')
('s', 'NNS')
('platform', 'NN')
('improves', 'VBZ')
('QOL', 'NNP')
('platform', 'NN')
('improves', 'VBZ')
('ways', 'NNS')
('platform', 'NN')
('improves', 'VBZ')
('area', 'NN')
('platform', 'NN')
('improves', 'VBZ')
('apart', 'NN')
('platform', 'NN')
('improves', 'VBZ')
('video', 'NN')
('platform', 'NN')
('improves', 'VBZ')
('game', 'NN')
('business', 'NN')
('improves', 'VBZ')
('people', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('s', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('QOL', 'NNP')
('business', 'NN')
('improves', 'VBZ')
('ways', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('area', 'NN')
('business', 'NN')
('improves', 'VBZ')
('apart', 'NN')
('business', 'NN')
('improves', 'VBZ')
('video', 'NN')
('business', 'NN')
('improves', 'VBZ')
('game', 'NN')
('business', 'NN')
('improves', 'VBZ')
('people', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('s', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('QOL', 'NNP')
('business', 'NN')
('improves', 'VBZ')
('ways', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('area', 'NN')
('business', 'NN')
('improves', 'VBZ')
('apart', 'NN')
('business', 'NN')
('improves', 'VBZ')
('video', 'NN')
('business', 'NN')
('improves', 'VBZ')
('game', 'NN')
('business', 'NN')
('improves', 'VBZ')
('people', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('s', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('QOL', 'NNP')
('business', 'NN')
('improves', 'VBZ')
('ways', 'NNS')
('business', 'NN')
('improves', 'VBZ')
('area', 'NN')
('business', 'NN')
('improves', 'VBZ')
('apart', 'NN')
('business', 'NN')
('improves', 'VBZ')
('video', 'NN')
('business', 'NN')
('improves', 'VBZ')
('game', 'NN')
('platform', 'NN')
('attempt', 'VB')
('area', 'NN')
('platform', 'NN')
('attempt', 'VB')
('apart', 'NN')
('platform', 'NN')
('attempt', 'VB')
('video', 'NN')
('platform', 'NN')
('attempt', 'VB')
('game', 'NN')
('business', 'NN')
('attempt', 'VB')
('area', 'NN')
('business', 'NN')
('attempt', 'VB')
('apart', 'NN')
('business', 'NN')
('attempt', 'VB')
('video', 'NN')
('business', 'NN')
('attempt', 'VB')
('game', 'NN')
('people', 'NNS')
('attempt', 'VB')
('area', 'NN')
('people', 'NNS')
('attempt', 'VB')
('apart', 'NN')
('people', 'NNS')
('attempt', 'VB')
('video', 'NN')
('people', 'NNS')
('attempt', 'VB')
('game', 'NN')
('s', 'NNS')
('attempt', 'VB')
('area', 'NN')
('s', 'NNS')
('attempt', 'VB')
('apart', 'NN')
('s', 'NNS')
('attempt', 'VB')
('video', 'NN')
('s', 'NNS')
('attempt', 'VB')
('game', 'NN')
('QOL', 'NNP')
('attempt', 'VB')
('area', 'NN')
('QOL', 'NNP')
('attempt', 'VB')
('apart', 'NN')
('QOL', 'NNP')
('attempt', 'VB')
('video', 'NN')
('QOL', 'NNP')
('attempt', 'VB')
('game', 'NN')
('ways', 'NNS')
('attempt', 'VB')
('area', 'NN')
('ways', 'NNS')
('attempt', 'VB')
('apart', 'NN')
('ways', 'NNS')
('attempt', 'VB')
('video', 'NN')
('ways', 'NNS')
('attempt', 'VB')
('game', 'NN')
('business', 'NN')
('attempt', 'VB')
('area', 'NN')
('business', 'NN')
('attempt', 'VB')
('apart', 'NN')
('business', 'NN')
('attempt', 'VB')
('video', 'NN')
('business', 'NN')
('attempt', 'VB')
('game', 'NN')
('business', 'NN')
('attempt', 'VB')
('area', 'NN')
('business', 'NN')
('attempt', 'VB')
('apart', 'NN')
('business', 'NN')
('attempt', 'VB')
('video', 'NN')
('business', 'NN')
('attempt', 'VB')
('game', 'NN')
('platform', 'NN')
('establish', 'VB')
('area', 'NN')
('platform', 'NN')
('establish', 'VB')
('apart', 'NN')
('platform', 'NN')
('establish', 'VB')
('video', 'NN')
('platform', 'NN')
('establish', 'VB')
('game', 'NN')
('business', 'NN')
('establish', 'VB')
('area', 'NN')
('business', 'NN')
('establish', 'VB')
('apart', 'NN')
('business', 'NN')
('establish', 'VB')
('video', 'NN')
('business', 'NN')
('establish', 'VB')
('game', 'NN')
('people', 'NNS')
('establish', 'VB')
('area', 'NN')
('people', 'NNS')
('establish', 'VB')
('apart', 'NN')
('people', 'NNS')
('establish', 'VB')
('video', 'NN')
('people', 'NNS')
('establish', 'VB')
('game', 'NN')
('s', 'NNS')
('establish', 'VB')
('area', 'NN')
('s', 'NNS')
('establish', 'VB')
('apart', 'NN')
('s', 'NNS')
('establish', 'VB')
('video', 'NN')
('s', 'NNS')
('establish', 'VB')
('game', 'NN')
('QOL', 'NNP')
('establish', 'VB')
('area', 'NN')
('QOL', 'NNP')
('establish', 'VB')
('apart', 'NN')
('QOL', 'NNP')
('establish', 'VB')
('video', 'NN')
('QOL', 'NNP')
('establish', 'VB')
('game', 'NN')
('ways', 'NNS')
('establish', 'VB')
('area', 'NN')
('ways', 'NNS')
('establish', 'VB')
('apart', 'NN')
('ways', 'NNS')
('establish', 'VB')
('video', 'NN')
('ways', 'NNS')
('establish', 'VB')
('game', 'NN')
('business', 'NN')
('establish', 'VB')
('area', 'NN')
('business', 'NN')
('establish', 'VB')
('apart', 'NN')
('business', 'NN')
('establish', 'VB')
('video', 'NN')
('business', 'NN')
('establish', 'VB')
('game', 'NN')
('business', 'NN')
('establish', 'VB')
('area', 'NN')
('business', 'NN')
('establish', 'VB')
('apart', 'NN')
('business', 'NN')
('establish', 'VB')
('video', 'NN')
('business', 'NN')
('establish', 'VB')
('game', 'NN')
('platform', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('platform', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('people', 'NNS')
('dedicated', 'VBN')
('video', 'NN')
('people', 'NNS')
('dedicated', 'VBN')
('game', 'NN')
('s', 'NNS')
('dedicated', 'VBN')
('video', 'NN')
('s', 'NNS')
('dedicated', 'VBN')
('game', 'NN')
('QOL', 'NNP')
('dedicated', 'VBN')
('video', 'NN')
('QOL', 'NNP')
('dedicated', 'VBN')
('game', 'NN')
('ways', 'NNS')
('dedicated', 'VBN')
('video', 'NN')
('ways', 'NNS')
('dedicated', 'VBN')
('game', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('area', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('area', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('apart', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('apart', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('video', 'NN')
('business', 'NN')
('dedicated', 'VBN')
('game', 'NN')
('health', 'NN')
('try', 'VB')
('strength', 'NN')
('health', 'NN')
('try', 'VB')
('entertainment', 'NN')
('health', 'NN')
('try', 'VB')
('company', 'NN')
('health', 'NN')
('try', 'VB')
('approaches', 'NNS')
('health', 'NN')
('try', 'VB')
('expand', 'NN')
('health', 'NN')
('try', 'VB')
('business', 'NN')
('theme', 'NN')
('try', 'VB')
('strength', 'NN')
('theme', 'NN')
('try', 'VB')
('entertainment', 'NN')
('theme', 'NN')
('try', 'VB')
('company', 'NN')
('theme', 'NN')
('try', 'VB')
('approaches', 'NNS')
('theme', 'NN')
('try', 'VB')
('expand', 'NN')
('theme', 'NN')
('try', 'VB')
('business', 'NN')
('step', 'NN')
('try', 'VB')
('strength', 'NN')
('step', 'NN')
('try', 'VB')
('entertainment', 'NN')
('step', 'NN')
('try', 'VB')
('company', 'NN')
('step', 'NN')
('try', 'VB')
('approaches', 'NNS')
('step', 'NN')
('try', 'VB')
('expand', 'NN')
('step', 'NN')
('try', 'VB')
('business', 'NN')
('health', 'NN')
('use', 'VB')
('strength', 'NN')
('health', 'NN')
('use', 'VB')
('entertainment', 'NN')
('health', 'NN')
('use', 'VB')
('company', 'NN')
('health', 'NN')
('use', 'VB')
('approaches', 'NNS')
('health', 'NN')
('use', 'VB')
('expand', 'NN')
('health', 'NN')
('use', 'VB')
('business', 'NN')
('theme', 'NN')
('use', 'VB')
('strength', 'NN')
('theme', 'NN')
('use', 'VB')
('entertainment', 'NN')
('theme', 'NN')
('use', 'VB')
('company', 'NN')
('theme', 'NN')
('use', 'VB')
('approaches', 'NNS')
('theme', 'NN')
('use', 'VB')
('expand', 'NN')
('theme', 'NN')
('use', 'VB')
('business', 'NN')
('step', 'NN')
('use', 'VB')
('strength', 'NN')
('step', 'NN')
('use', 'VB')
('entertainment', 'NN')
('step', 'NN')
('use', 'VB')
('company', 'NN')
('step', 'NN')
('use', 'VB')
('approaches', 'NNS')
('step', 'NN')
('use', 'VB')
('expand', 'NN')
('step', 'NN')
('use', 'VB')
('business', 'NN')
('health', 'NN')
('create', 'VB')
('approaches', 'NNS')
('health', 'NN')
('create', 'VB')
('expand', 'NN')
('health', 'NN')
('create', 'VB')
('business', 'NN')
('theme', 'NN')
('create', 'VB')
('approaches', 'NNS')
('theme', 'NN')
('create', 'VB')
('expand', 'NN')
('theme', 'NN')
('create', 'VB')
('business', 'NN')
('step', 'NN')
('create', 'VB')
('approaches', 'NNS')
('step', 'NN')
('create', 'VB')
('expand', 'NN')
('step', 'NN')
('create', 'VB')
('business', 'NN')
('strength', 'NN')
('create', 'VB')
('approaches', 'NNS')
('strength', 'NN')
('create', 'VB')
('expand', 'NN')
('strength', 'NN')
('create', 'VB')
('business', 'NN')
('entertainment', 'NN')
('create', 'VB')
('approaches', 'NNS')
('entertainment', 'NN')
('create', 'VB')
('expand', 'NN')
('entertainment', 'NN')
('create', 'VB')
('business', 'NN')
('company', 'NN')
('create', 'VB')
('approaches', 'NNS')
('company', 'NN')
('create', 'VB')
('expand', 'NN')
('company', 'NN')
('create', 'VB')
('business', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('platform', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('strategy', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('user', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('base', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('environment', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('people', 'NNS')
('endeavors', 'NNS')
('improving', 'VBG')
('health', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('turn', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('expand', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('Nintendo', 'NNP')
('endeavors', 'NNS')
('improving', 'VBG')
('user', 'NN')
('endeavors', 'NNS')
('improving', 'VBG')
('base', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('platform', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('strategy', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('user', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('base', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('environment', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('people', 'NNS')
('QOL', 'NNP')
('improving', 'VBG')
('health', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('turn', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('expand', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('Nintendo', 'NNP')
('QOL', 'NNP')
('improving', 'VBG')
('user', 'NN')
('QOL', 'NNP')
('improving', 'VBG')
('base', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('strategy', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('user', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('base', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('environment', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('people', 'NNS')
('endeavors', 'NNS')
('strive', 'VBP')
('health', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('turn', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('expand', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('Nintendo', 'NNP')
('endeavors', 'NNS')
('strive', 'VBP')
('user', 'NN')
('endeavors', 'NNS')
('strive', 'VBP')
('base', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('strategy', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('user', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('base', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('environment', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('people', 'NNS')
('QOL', 'NNP')
('strive', 'VBP')
('health', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('turn', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('expand', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('Nintendo', 'NNP')
('QOL', 'NNP')
('strive', 'VBP')
('user', 'NN')
('QOL', 'NNP')
('strive', 'VBP')
('base', 'NN')
('platform', 'NN')
('strive', 'VBP')
('strategy', 'NN')
('platform', 'NN')
('strive', 'VBP')
('user', 'NN')
('platform', 'NN')
('strive', 'VBP')
('base', 'NN')
('platform', 'NN')
('strive', 'VBP')
('environment', 'NN')
('platform', 'NN')
('strive', 'VBP')
('people', 'NNS')
('platform', 'NN')
('strive', 'VBP')
('health', 'NN')
('platform', 'NN')
('strive', 'VBP')
('turn', 'NN')
('platform', 'NN')
('strive', 'VBP')
('expand', 'NN')
('platform', 'NN')
('strive', 'VBP')
('Nintendo', 'NNP')
('platform', 'NN')
('strive', 'VBP')
('user', 'NN')
('platform', 'NN')
('strive', 'VBP')
('base', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('strategy', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('user', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('base', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('environment', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('people', 'NNS')
('endeavors', 'NNS')
('promote', 'VB')
('health', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('turn', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('expand', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('Nintendo', 'NNP')
('endeavors', 'NNS')
('promote', 'VB')
('user', 'NN')
('endeavors', 'NNS')
('promote', 'VB')
('base', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('strategy', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('user', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('base', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('environment', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('people', 'NNS')
('QOL', 'NNP')
('promote', 'VB')
('health', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('turn', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('expand', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('Nintendo', 'NNP')
('QOL', 'NNP')
('promote', 'VB')
('user', 'NN')
('QOL', 'NNP')
('promote', 'VB')
('base', 'NN')
('platform', 'NN')
('promote', 'VB')
('strategy', 'NN')
('platform', 'NN')
('promote', 'VB')
('user', 'NN')
('platform', 'NN')
('promote', 'VB')
('base', 'NN')
('platform', 'NN')
('promote', 'VB')
('environment', 'NN')
('platform', 'NN')
('promote', 'VB')
('people', 'NNS')
('platform', 'NN')
('promote', 'VB')
('health', 'NN')
('platform', 'NN')
('promote', 'VB')
('turn', 'NN')
('platform', 'NN')
('promote', 'VB')
('expand', 'NN')
('platform', 'NN')
('promote', 'VB')
('Nintendo', 'NNP')
('platform', 'NN')
('promote', 'VB')
('user', 'NN')
('platform', 'NN')
('promote', 'VB')
('base', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('strategy', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('user', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('base', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('environment', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('people', 'NNS')
('endeavors', 'NNS')
('existing', 'VBG')
('health', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('turn', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('expand', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('Nintendo', 'NNP')
('endeavors', 'NNS')
('existing', 'VBG')
('user', 'NN')
('endeavors', 'NNS')
('existing', 'VBG')
('base', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('strategy', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('user', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('base', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('environment', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('people', 'NNS')
('QOL', 'NNP')
('existing', 'VBG')
('health', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('turn', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('expand', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('Nintendo', 'NNP')
('QOL', 'NNP')
('existing', 'VBG')
('user', 'NN')
('QOL', 'NNP')
('existing', 'VBG')
('base', 'NN')
('platform', 'NN')
('existing', 'VBG')
('strategy', 'NN')
('platform', 'NN')
('existing', 'VBG')
('user', 'NN')
('platform', 'NN')
('existing', 'VBG')
('base', 'NN')
('platform', 'NN')
('existing', 'VBG')
('environment', 'NN')
('platform', 'NN')
('existing', 'VBG')
('people', 'NNS')
('platform', 'NN')
('existing', 'VBG')
('health', 'NN')
('platform', 'NN')
('existing', 'VBG')
('turn', 'NN')
('platform', 'NN')
('existing', 'VBG')
('expand', 'NN')
('platform', 'NN')
('existing', 'VBG')
('Nintendo', 'NNP')
('platform', 'NN')
('existing', 'VBG')
('user', 'NN')
('platform', 'NN')
('existing', 'VBG')
('base', 'NN')
('endeavors', 'NNS')
('expanding', 'VBG')
('user', 'NN')
('endeavors', 'NNS')
('expanding', 'VBG')
('base', 'NN')
('endeavors', 'NNS')
('expanding', 'VBG')
('environment', 'NN')
('endeavors', 'NNS')
('expanding', 'VBG')
('people', 'NNS')
('endeavors', 'NNS')
('expanding', 'VBG')
('health', 'NN')
('endeavors', 'NNS')
('expanding', 'VBG')
('turn', 'NN')
('endeavors', 'NNS')
('expanding', 'VBG')
('expand', 'NN')
('endeavors', 'NNS')
('expanding', 'VBG')
('Nintendo', 'NNP')
('endeavors', 'NNS')
('expanding', 'VBG')
('user', 'NN')
('endeavors', 'NNS')
('expanding', 'VBG')
('base', 'NN')
('QOL', 'NNP')
('expanding', 'VBG')
('user', 'NN')
('QOL', 'NNP')
('expanding', 'VBG')
('base', 'NN')
('QOL', 'NNP')
('expanding', 'VBG')
('environment', 'NN')
('QOL', 'NNP')
('expanding', 'VBG')
('people', 'NNS')
('QOL', 'NNP')
('expanding', 'VBG')
('health', 'NN')
('QOL', 'NNP')
('expanding', 'VBG')
('turn', 'NN')
('QOL', 'NNP')
('expanding', 'VBG')
('expand', 'NN')
('QOL', 'NNP')
('expanding', 'VBG')
('Nintendo', 'NNP')
('QOL', 'NNP')
('expanding', 'VBG')
('user', 'NN')
('QOL', 'NNP')
('expanding', 'VBG')
('base', 'NN')
('platform', 'NN')
('expanding', 'VBG')
('user', 'NN')
('platform', 'NN')
('expanding', 'VBG')
('base', 'NN')
('platform', 'NN')
('expanding', 'VBG')
('environment', 'NN')
('platform', 'NN')
('expanding', 'VBG')
('people', 'NNS')
('platform', 'NN')
('expanding', 'VBG')
('health', 'NN')
('platform', 'NN')
('expanding', 'VBG')
('turn', 'NN')
('platform', 'NN')
('expanding', 'VBG')
('expand', 'NN')
('platform', 'NN')
('expanding', 'VBG')
('Nintendo', 'NNP')
('platform', 'NN')
('expanding', 'VBG')
('user', 'NN')
('platform', 'NN')
('expanding', 'VBG')
('base', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('user', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('base', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('environment', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('people', 'NNS')
('strategy', 'NN')
('expanding', 'VBG')
('health', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('turn', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('expand', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('Nintendo', 'NNP')
('strategy', 'NN')
('expanding', 'VBG')
('user', 'NN')
('strategy', 'NN')
('expanding', 'VBG')
('base', 'NN')
('endeavors', 'NNS')
('create', 'VB')
('environment', 'NN')
('endeavors', 'NNS')
('create', 'VB')
('people', 'NNS')
('endeavors', 'NNS')
('create', 'VB')
('health', 'NN')
('endeavors', 'NNS')
('create', 'VB')
('turn', 'NN')
('endeavors', 'NNS')
('create', 'VB')
('expand', 'NN')
('endeavors', 'NNS')
('create', 'VB')
('Nintendo', 'NNP')
('QOL', 'NNP')
('create', 'VB')
('environment', 'NN')
('QOL', 'NNP')
('create', 'VB')
('people', 'NNS')
('QOL', 'NNP')
('create', 'VB')
('health', 'NN')
('QOL', 'NNP')
('create', 'VB')
('turn', 'NN')
('QOL', 'NNP')
('create', 'VB')
('expand', 'NN')
('QOL', 'NNP')
('create', 'VB')
('Nintendo', 'NNP')
('platform', 'NN')
('create', 'VB')
('environment', 'NN')
('platform', 'NN')
('create', 'VB')
('people', 'NNS')
('platform', 'NN')
('create', 'VB')
('health', 'NN')
('platform', 'NN')
('create', 'VB')
('turn', 'NN')
('platform', 'NN')
('create', 'VB')
('expand', 'NN')
('platform', 'NN')
('create', 'VB')
('Nintendo', 'NNP')
('strategy', 'NN')
('create', 'VB')
('environment', 'NN')
('strategy', 'NN')
('create', 'VB')
('people', 'NNS')
('strategy', 'NN')
('create', 'VB')
('health', 'NN')
('strategy', 'NN')
('create', 'VB')
('turn', 'NN')
('strategy', 'NN')
('create', 'VB')
('expand', 'NN')
('strategy', 'NN')
('create', 'VB')
('Nintendo', 'NNP')
('user', 'NN')
('create', 'VB')
('environment', 'NN')
('user', 'NN')
('create', 'VB')
('people', 'NNS')
('user', 'NN')
('create', 'VB')
('health', 'NN')
('user', 'NN')
('create', 'VB')
('turn', 'NN')
('user', 'NN')
('create', 'VB')
('expand', 'NN')
('user', 'NN')
('create', 'VB')
('Nintendo', 'NNP')
('base', 'NN')
('create', 'VB')
('environment', 'NN')
('base', 'NN')
('create', 'VB')
('people', 'NNS')
('base', 'NN')
('create', 'VB')
('health', 'NN')
('base', 'NN')
('create', 'VB')
('turn', 'NN')
('base', 'NN')
('create', 'VB')
('expand', 'NN')
('base', 'NN')
('create', 'VB')
('Nintendo', 'NNP')
('user', 'NN')
('create', 'VB')
('environment', 'NN')
('user', 'NN')
('create', 'VB')
('people', 'NNS')
('user', 'NN')
('create', 'VB')
('health', 'NN')
('user', 'NN')
('create', 'VB')
('turn', 'NN')
('user', 'NN')
('create', 'VB')
('expand', 'NN')
('user', 'NN')
('create', 'VB')
('Nintendo', 'NNP')
('base', 'NN')
('create', 'VB')
('environment', 'NN')
('base', 'NN')
('create', 'VB')
('people', 'NNS')
('base', 'NN')
('create', 'VB')
('health', 'NN')
('base', 'NN')
('create', 'VB')
('turn', 'NN')
('base', 'NN')
('create', 'VB')
('expand', 'NN')
('base', 'NN')
('create', 'VB')
('Nintendo', 'NNP')
('endeavors', 'NNS')
('are', 'VBP')
('health', 'NN')
('endeavors', 'NNS')
('are', 'VBP')
('turn', 'NN')
('endeavors', 'NNS')
('are', 'VBP')
('expand', 'NN')
('endeavors', 'NNS')
('are', 'VBP')
('Nintendo', 'NNP')
('QOL', 'NNP')
('are', 'VBP')
('health', 'NN')
('QOL', 'NNP')
('are', 'VBP')
('turn', 'NN')
('QOL', 'NNP')
('are', 'VBP')
('expand', 'NN')
('QOL', 'NNP')
('are', 'VBP')
('Nintendo', 'NNP')
('platform', 'NN')
('are', 'VBP')
('health', 'NN')
('platform', 'NN')
('are', 'VBP')
('turn', 'NN')
('platform', 'NN')
('are', 'VBP')
('expand', 'NN')
('platform', 'NN')
('are', 'VBP')
('Nintendo', 'NNP')
('strategy', 'NN')
('are', 'VBP')
('health', 'NN')
('strategy', 'NN')
('are', 'VBP')
('turn', 'NN')
('strategy', 'NN')
('are', 'VBP')
('expand', 'NN')
('strategy', 'NN')
('are', 'VBP')
('Nintendo', 'NNP')
('user', 'NN')
('are', 'VBP')
('health', 'NN')
('user', 'NN')
('are', 'VBP')
('turn', 'NN')
('user', 'NN')
('are', 'VBP')
('expand', 'NN')
('user', 'NN')
('are', 'VBP')
('Nintendo', 'NNP')
('base', 'NN')
('are', 'VBP')
('health', 'NN')
('base', 'NN')
('are', 'VBP')
('turn', 'NN')
('base', 'NN')
('are', 'VBP')
('expand', 'NN')
('base', 'NN')
('are', 'VBP')
('Nintendo', 'NNP')
('environment', 'NN')
('are', 'VBP')
('health', 'NN')
('environment', 'NN')
('are', 'VBP')
('turn', 'NN')
('environment', 'NN')
('are', 'VBP')
('expand', 'NN')
('environment', 'NN')
('are', 'VBP')
('Nintendo', 'NNP')
('people', 'NNS')
('are', 'VBP')
('health', 'NN')
('people', 'NNS')
('are', 'VBP')
('turn', 'NN')
('people', 'NNS')
('are', 'VBP')
('expand', 'NN')
('people', 'NNS')
('are', 'VBP')
('Nintendo', 'NNP')
('user', 'NN')
('are', 'VBP')
('health', 'NN')
('user', 'NN')
('are', 'VBP')
('turn', 'NN')
('user', 'NN')
('are', 'VBP')
('expand', 'NN')
('user', 'NN')
('are', 'VBP')
('Nintendo', 'NNP')
('base', 'NN')
('are', 'VBP')
('health', 'NN')
('base', 'NN')
('are', 'VBP')
('turn', 'NN')
('base', 'NN')
('are', 'VBP')
('expand', 'NN')
('base', 'NN')
('are', 'VBP')
('Nintendo', 'NNP')
('Nintendo', 'NNP')
('started', 'VBD')
('manufacture', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('sale', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('Hanafuda', 'NNP')
('Nintendo', 'NNP')
('started', 'VBD')
('(', 'NNP')
('Nintendo', 'NNP')
('started', 'VBD')
('playing', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('cards', 'NNS')
('Nintendo', 'NNP')
('started', 'VBD')
('years', 'NNS')
('Nintendo', 'NNP')
('started', 'VBD')
('playing', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('card', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('company', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('toy', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('company', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('toy', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('company', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('toy', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('company', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('toy', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('company', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('company', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('video', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('game', 'NN')
('Nintendo', 'NNP')
('started', 'VBD')
('platforms', 'NNS')
('Nintendo', 'NNP')
('has', 'VBZ')
('card', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('video', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('game', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('platforms', 'NNS')
('manufacture', 'NN')
('has', 'VBZ')
('card', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('company', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('toy', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('company', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('toy', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('company', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('toy', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('company', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('toy', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('company', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('company', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('video', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('game', 'NN')
('manufacture', 'NN')
('has', 'VBZ')
('platforms', 'NNS')
('sale', 'NN')
('has', 'VBZ')
('card', 'NN')
('sale', 'NN')
('has', 'VBZ')
('company', 'NN')
('sale', 'NN')
('has', 'VBZ')
('toy', 'NN')
('sale', 'NN')
('has', 'VBZ')
('company', 'NN')
('sale', 'NN')
('has', 'VBZ')
('toy', 'NN')
('sale', 'NN')
('has', 'VBZ')
('company', 'NN')
('sale', 'NN')
('has', 'VBZ')
('toy', 'NN')
('sale', 'NN')
('has', 'VBZ')
('company', 'NN')
('sale', 'NN')
('has', 'VBZ')
('toy', 'NN')
('sale', 'NN')
('has', 'VBZ')
('company', 'NN')
('sale', 'NN')
('has', 'VBZ')
('company', 'NN')
('sale', 'NN')
('has', 'VBZ')
('video', 'NN')
('sale', 'NN')
('has', 'VBZ')
('game', 'NN')
('sale', 'NN')
('has', 'VBZ')
('platforms', 'NNS')
('Hanafuda', 'NNP')
('has', 'VBZ')
('card', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('company', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('video', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('game', 'NN')
('Hanafuda', 'NNP')
('has', 'VBZ')
('platforms', 'NNS')
('(', 'NNP')
('has', 'VBZ')
('card', 'NN')
('(', 'NNP')
('has', 'VBZ')
('company', 'NN')
('(', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('(', 'NNP')
('has', 'VBZ')
('company', 'NN')
('(', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('(', 'NNP')
('has', 'VBZ')
('company', 'NN')
('(', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('(', 'NNP')
('has', 'VBZ')
('company', 'NN')
('(', 'NNP')
('has', 'VBZ')
('toy', 'NN')
('(', 'NNP')
('has', 'VBZ')
('company', 'NN')
('(', 'NNP')
('has', 'VBZ')
('company', 'NN')
('(', 'NNP')
('has', 'VBZ')
('video', 'NN')
('(', 'NNP')
('has', 'VBZ')
('game', 'NN')
('(', 'NNP')
('has', 'VBZ')
('platforms', 'NNS')
('playing', 'NN')
('has', 'VBZ')
('card', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('toy', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('toy', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('toy', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('toy', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('video', 'NN')
('playing', 'NN')
('has', 'VBZ')
('game', 'NN')
('playing', 'NN')
('has', 'VBZ')
('platforms', 'NNS')
('cards', 'NNS')
('has', 'VBZ')
('card', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('company', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('toy', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('company', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('toy', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('company', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('toy', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('company', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('toy', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('company', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('company', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('video', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('game', 'NN')
('cards', 'NNS')
('has', 'VBZ')
('platforms', 'NNS')
('years', 'NNS')
('has', 'VBZ')
('card', 'NN')
('years', 'NNS')
('has', 'VBZ')
('company', 'NN')
('years', 'NNS')
('has', 'VBZ')
('toy', 'NN')
('years', 'NNS')
('has', 'VBZ')
('company', 'NN')
('years', 'NNS')
('has', 'VBZ')
('toy', 'NN')
('years', 'NNS')
('has', 'VBZ')
('company', 'NN')
('years', 'NNS')
('has', 'VBZ')
('toy', 'NN')
('years', 'NNS')
('has', 'VBZ')
('company', 'NN')
('years', 'NNS')
('has', 'VBZ')
('toy', 'NN')
('years', 'NNS')
('has', 'VBZ')
('company', 'NN')
('years', 'NNS')
('has', 'VBZ')
('company', 'NN')
('years', 'NNS')
('has', 'VBZ')
('video', 'NN')
('years', 'NNS')
('has', 'VBZ')
('game', 'NN')
('years', 'NNS')
('has', 'VBZ')
('platforms', 'NNS')
('playing', 'NN')
('has', 'VBZ')
('card', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('toy', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('toy', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('toy', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('toy', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('company', 'NN')
('playing', 'NN')
('has', 'VBZ')
('video', 'NN')
('playing', 'NN')
('has', 'VBZ')
('game', 'NN')
('playing', 'NN')
('has', 'VBZ')
('platforms', 'NNS')
('Nintendo', 'NNP')
('innovated', 'VBN')
('card', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('video', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('game', 'NN')
('Nintendo', 'NNP')
('innovated', 'VBN')
('platforms', 'NNS')
('manufacture', 'NN')
('innovated', 'VBN')
('card', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('company', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('company', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('company', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('company', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('company', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('company', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('video', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('game', 'NN')
('manufacture', 'NN')
('innovated', 'VBN')
('platforms', 'NNS')
('sale', 'NN')
('innovated', 'VBN')
('card', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('company', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('company', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('company', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('company', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('company', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('company', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('video', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('game', 'NN')
('sale', 'NN')
('innovated', 'VBN')
('platforms', 'NNS')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('card', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('video', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('game', 'NN')
('Hanafuda', 'NNP')
('innovated', 'VBN')
('platforms', 'NNS')
('(', 'NNP')
('innovated', 'VBN')
('card', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('toy', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('company', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('video', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('game', 'NN')
('(', 'NNP')
('innovated', 'VBN')
('platforms', 'NNS')
('playing', 'NN')
('innovated', 'VBN')
('card', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('video', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('game', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('platforms', 'NNS')
('cards', 'NNS')
('innovated', 'VBN')
('card', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('toy', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('toy', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('toy', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('toy', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('video', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('game', 'NN')
('cards', 'NNS')
('innovated', 'VBN')
('platforms', 'NNS')
('years', 'NNS')
('innovated', 'VBN')
('card', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('toy', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('toy', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('toy', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('toy', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('company', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('video', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('game', 'NN')
('years', 'NNS')
('innovated', 'VBN')
('platforms', 'NNS')
('playing', 'NN')
('innovated', 'VBN')
('card', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('toy', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('company', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('video', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('game', 'NN')
('playing', 'NN')
('innovated', 'VBN')
('platforms', 'NNS')
('Nintendo', 'NNP')
('developing', 'VBG')
('video', 'NN')
('Nintendo', 'NNP')
('developing', 'VBG')
('game', 'NN')
('Nintendo', 'NNP')
('developing', 'VBG')
('platforms', 'NNS')
('manufacture', 'NN')
('developing', 'VBG')
('video', 'NN')
('manufacture', 'NN')
('developing', 'VBG')
('game', 'NN')
('manufacture', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('sale', 'NN')
('developing', 'VBG')
('video', 'NN')
('sale', 'NN')
('developing', 'VBG')
('game', 'NN')
('sale', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('Hanafuda', 'NNP')
('developing', 'VBG')
('video', 'NN')
('Hanafuda', 'NNP')
('developing', 'VBG')
('game', 'NN')
('Hanafuda', 'NNP')
('developing', 'VBG')
('platforms', 'NNS')
('(', 'NNP')
('developing', 'VBG')
('video', 'NN')
('(', 'NNP')
('developing', 'VBG')
('game', 'NN')
('(', 'NNP')
('developing', 'VBG')
('platforms', 'NNS')
('playing', 'NN')
('developing', 'VBG')
('video', 'NN')
('playing', 'NN')
('developing', 'VBG')
('game', 'NN')
('playing', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('cards', 'NNS')
('developing', 'VBG')
('video', 'NN')
('cards', 'NNS')
('developing', 'VBG')
('game', 'NN')
('cards', 'NNS')
('developing', 'VBG')
('platforms', 'NNS')
('years', 'NNS')
('developing', 'VBG')
('video', 'NN')
('years', 'NNS')
('developing', 'VBG')
('game', 'NN')
('years', 'NNS')
('developing', 'VBG')
('platforms', 'NNS')
('playing', 'NN')
('developing', 'VBG')
('video', 'NN')
('playing', 'NN')
('developing', 'VBG')
('game', 'NN')
('playing', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('card', 'NN')
('developing', 'VBG')
('video', 'NN')
('card', 'NN')
('developing', 'VBG')
('game', 'NN')
('card', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('company', 'NN')
('developing', 'VBG')
('video', 'NN')
('company', 'NN')
('developing', 'VBG')
('game', 'NN')
('company', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('toy', 'NN')
('developing', 'VBG')
('video', 'NN')
('toy', 'NN')
('developing', 'VBG')
('game', 'NN')
('toy', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('company', 'NN')
('developing', 'VBG')
('video', 'NN')
('company', 'NN')
('developing', 'VBG')
('game', 'NN')
('company', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('toy', 'NN')
('developing', 'VBG')
('video', 'NN')
('toy', 'NN')
('developing', 'VBG')
('game', 'NN')
('toy', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('company', 'NN')
('developing', 'VBG')
('video', 'NN')
('company', 'NN')
('developing', 'VBG')
('game', 'NN')
('company', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('toy', 'NN')
('developing', 'VBG')
('video', 'NN')
('toy', 'NN')
('developing', 'VBG')
('game', 'NN')
('toy', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('company', 'NN')
('developing', 'VBG')
('video', 'NN')
('company', 'NN')
('developing', 'VBG')
('game', 'NN')
('company', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('toy', 'NN')
('developing', 'VBG')
('video', 'NN')
('toy', 'NN')
('developing', 'VBG')
('game', 'NN')
('toy', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('company', 'NN')
('developing', 'VBG')
('video', 'NN')
('company', 'NN')
('developing', 'VBG')
('game', 'NN')
('company', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('company', 'NN')
('developing', 'VBG')
('video', 'NN')
('company', 'NN')
('developing', 'VBG')
('game', 'NN')
('company', 'NN')
('developing', 'VBG')
('platforms', 'NNS')
('Nintendo', 'NNP')
('has', 'VBZ')
('try', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('things', 'NNS')
('Nintendo', 'NNP')
('has', 'VBZ')
('history', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('failures', 'NNS')
('Nintendo', 'NNP')
('has', 'VBZ')
('successes', 'NNS')
('Nintendo', 'NNP')
('has', 'VBZ')
('pioneer', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('home', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('video', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('game', 'NN')
('Nintendo', 'NNP')
('has', 'VBZ')
('market', 'NN')
('Nintendo', 'NNP')
('continued', 'VBN')
('try', 'NN')
('Nintendo', 'NNP')
('continued', 'VBN')
('things', 'NNS')
('Nintendo', 'NNP')
('continued', 'VBN')
('history', 'NN')
('Nintendo', 'NNP')
('continued', 'VBN')
('failures', 'NNS')
('Nintendo', 'NNP')
('continued', 'VBN')
('successes', 'NNS')
('Nintendo', 'NNP')
('continued', 'VBN')
('pioneer', 'NN')
('Nintendo', 'NNP')
('continued', 'VBN')
('home', 'NN')
('Nintendo', 'NNP')
('continued', 'VBN')
('video', 'NN')
('Nintendo', 'NNP')
('continued', 'VBN')
('game', 'NN')
('Nintendo', 'NNP')
('continued', 'VBN')
('market', 'NN')
('Nintendo', 'NNP')
('experiencing', 'VBG')
('failures', 'NNS')
('Nintendo', 'NNP')
('experiencing', 'VBG')
('successes', 'NNS')
('Nintendo', 'NNP')
('experiencing', 'VBG')
('pioneer', 'NN')
('Nintendo', 'NNP')
('experiencing', 'VBG')
('home', 'NN')
('Nintendo', 'NNP')
('experiencing', 'VBG')
('video', 'NN')
('Nintendo', 'NNP')
('experiencing', 'VBG')
('game', 'NN')
('Nintendo', 'NNP')
('experiencing', 'VBG')
('market', 'NN')
('try', 'NN')
('experiencing', 'VBG')
('failures', 'NNS')
('try', 'NN')
('experiencing', 'VBG')
('successes', 'NNS')
('try', 'NN')
('experiencing', 'VBG')
('pioneer', 'NN')
('try', 'NN')
('experiencing', 'VBG')
('home', 'NN')
('try', 'NN')
('experiencing', 'VBG')
('video', 'NN')
('try', 'NN')
('experiencing', 'VBG')
('game', 'NN')
('try', 'NN')
('experiencing', 'VBG')
('market', 'NN')
('things', 'NNS')
('experiencing', 'VBG')
('failures', 'NNS')
('things', 'NNS')
('experiencing', 'VBG')
('successes', 'NNS')
('things', 'NNS')
('experiencing', 'VBG')
('pioneer', 'NN')
('things', 'NNS')
('experiencing', 'VBG')
('home', 'NN')
('things', 'NNS')
('experiencing', 'VBG')
('video', 'NN')
('things', 'NNS')
('experiencing', 'VBG')
('game', 'NN')
('things', 'NNS')
('experiencing', 'VBG')
('market', 'NN')
('history', 'NN')
('experiencing', 'VBG')
('failures', 'NNS')
('history', 'NN')
('experiencing', 'VBG')
('successes', 'NNS')
('history', 'NN')
('experiencing', 'VBG')
('pioneer', 'NN')
('history', 'NN')
('experiencing', 'VBG')
('home', 'NN')
('history', 'NN')
('experiencing', 'VBG')
('video', 'NN')
('history', 'NN')
('experiencing', 'VBG')
('game', 'NN')
('history', 'NN')
('experiencing', 'VBG')
('market', 'NN')
('Nintendo', 'NNP')
('managed', 'VBD')
('pioneer', 'NN')
('Nintendo', 'NNP')
('managed', 'VBD')
('home', 'NN')
('Nintendo', 'NNP')
('managed', 'VBD')
('video', 'NN')
('Nintendo', 'NNP')
('managed', 'VBD')
('game', 'NN')
('Nintendo', 'NNP')
('managed', 'VBD')
('market', 'NN')
('try', 'NN')
('managed', 'VBD')
('pioneer', 'NN')
('try', 'NN')
('managed', 'VBD')
('home', 'NN')
('try', 'NN')
('managed', 'VBD')
('video', 'NN')
('try', 'NN')
('managed', 'VBD')
('game', 'NN')
('try', 'NN')
('managed', 'VBD')
('market', 'NN')
('things', 'NNS')
('managed', 'VBD')
('pioneer', 'NN')
('things', 'NNS')
('managed', 'VBD')
('home', 'NN')
('things', 'NNS')
('managed', 'VBD')
('video', 'NN')
('things', 'NNS')
('managed', 'VBD')
('game', 'NN')
('things', 'NNS')
('managed', 'VBD')
('market', 'NN')
('history', 'NN')
('managed', 'VBD')
('pioneer', 'NN')
('history', 'NN')
('managed', 'VBD')
('home', 'NN')
('history', 'NN')
('managed', 'VBD')
('video', 'NN')
('history', 'NN')
('managed', 'VBD')
('game', 'NN')
('history', 'NN')
('managed', 'VBD')
('market', 'NN')
('failures', 'NNS')
('managed', 'VBD')
('pioneer', 'NN')
('failures', 'NNS')
('managed', 'VBD')
('home', 'NN')
('failures', 'NNS')
('managed', 'VBD')
('video', 'NN')
('failures', 'NNS')
('managed', 'VBD')
('game', 'NN')
('failures', 'NNS')
('managed', 'VBD')
('market', 'NN')
('successes', 'NNS')
('managed', 'VBD')
('pioneer', 'NN')
('successes', 'NNS')
('managed', 'VBD')
('home', 'NN')
('successes', 'NNS')
('managed', 'VBD')
('video', 'NN')
('successes', 'NNS')
('managed', 'VBD')
('game', 'NN')
('successes', 'NNS')
('managed', 'VBD')
('market', 'NN')
('something', 'NN')
('improve', 'VB')
('people', 'NNS')
('something', 'NN')
('improve', 'VB')
('s', 'NNS')
('something', 'NN')
('improve', 'VB')
('QOL', 'NNP')
('something', 'NN')
('improve', 'VB')
('ways', 'NNS')
('materials', 'NNS')
('improve', 'VB')
('people', 'NNS')
('materials', 'NNS')
('improve', 'VB')
('s', 'NNS')
('materials', 'NNS')
('improve', 'VB')
('QOL', 'NNP')
('materials', 'NNS')
('improve', 'VB')
('ways', 'NNS')
('technologies', 'NNS')
('improve', 'VB')
('people', 'NNS')
('technologies', 'NNS')
('improve', 'VB')
('s', 'NNS')
('technologies', 'NNS')
('improve', 'VB')
('QOL', 'NNP')
('technologies', 'NNS')
('improve', 'VB')
('ways', 'NNS')
('time', 'NN')
('improve', 'VB')
('people', 'NNS')
('time', 'NN')
('improve', 'VB')
('s', 'NNS')
('time', 'NN')
('improve', 'VB')
('QOL', 'NNP')
('time', 'NN')
('improve', 'VB')
('ways', 'NNS')
('position', 'NN')
('improve', 'VB')
('people', 'NNS')
('position', 'NN')
('improve', 'VB')
('s', 'NNS')
('position', 'NN')
('improve', 'VB')
('QOL', 'NNP')
('position', 'NN')
('improve', 'VB')
('ways', 'NNS')
('entertainment', 'NN')
('improve', 'VB')
('people', 'NNS')
('entertainment', 'NN')
('improve', 'VB')
('s', 'NNS')
('entertainment', 'NN')
('improve', 'VB')
('QOL', 'NNP')
('entertainment', 'NN')
('improve', 'VB')
('ways', 'NNS')
('core', 'NN')
('improve', 'VB')
('people', 'NNS')
('core', 'NN')
('improve', 'VB')
('s', 'NNS')
('core', 'NN')
('improve', 'VB')
('QOL', 'NNP')
('core', 'NN')
('improve', 'VB')
('ways', 'NNS')
('business', 'NN')
('improve', 'VB')
('people', 'NNS')
('business', 'NN')
('improve', 'VB')
('s', 'NNS')
('business', 'NN')
('improve', 'VB')
('QOL', 'NNP')
('business', 'NN')
('improve', 'VB')
('ways', 'NNS')
('Nintendo', 'NNP')
('make', 'VB')
('progress', 'NN')
('Nintendo', 'NNP')
('make', 'VB')
('support', 'NN')
('Nintendo', 'NNP')
('make', 'VB')
('encouragement', 'NN')
('Nintendo', 'NNP')
('make', 'VB')
('shareholders', 'NNS')
('Nintendo', 'NNP')
('make', 'VB')
('investors', 'NNS')
('intends', 'NNS')
('make', 'VB')
('progress', 'NN')
('intends', 'NNS')
('make', 'VB')
('support', 'NN')
('intends', 'NNS')
('make', 'VB')
('encouragement', 'NN')
('intends', 'NNS')
('make', 'VB')
('shareholders', 'NNS')
('intends', 'NNS')
('make', 'VB')
('investors', 'NNS')
>>> len(summe.sentences[0][5])
135
>>> summe.getCandidSubjs()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    summe.getCandidSubjs()
TypeError: getCandidSubjs() missing 2 required positional arguments: 'start' and 'end'
>>> summe.getCandidSubjs(None,None)
>>> len(summe.CandidSVO)
6122
>>> summe.getCandidSubjs(None,10)
>>> len(summe.CandidSVO)
7095
>>> summe.CandidSVO = []
>>> summe.getCandidSVO(None,10)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    summe.getCandidSVO(None,10)
AttributeError: 'module' object has no attribute 'getCandidSVO'
>>> summe.getCandidSubjs(None,10)
>>> len(summe.CandidSVO)
973
>>> for sent in summe.sentences:
	print(len(sent[5]))

	
135
226
1392
261
42
72
58
116
54
251
334
78
32
0
10
>>> for sent in summe.terms:
	print(sent)

	
('launch', 1.1760912590556813)
('Entertainment', 1.7501225267834002)
('System', 1.1760912590556813)
('Nintendo', 2.316952533289971)
('world', 2.0969100130080567)
('unique', 1.1760912590556813)
('entertainment', 2.387640052032226)
('products', 2.0969100130080567)
('development', 1.1760912590556813)
('concept', 1.1760912590556813)
('hardware', 1.7501225267834002)
('software', 1.7501225267834002)
('integration', 1.1760912590556813)
('field', 1.1760912590556813)
('home', 1.7501225267834002)
('industry', 1.1760912590556813)
('industries', 1.1760912590556813)
('Japan', 1.1760912590556813)
('spread', 1.1760912590556813)
('brand', 1.1760912590556813)
('video', 2.385606273598312)
('game', 2.385606273598312)
('culture', 1.1760912590556813)
('belief', 1.1760912590556813)
('raison', 1.1760912590556813)
('d', 1.1760912590556813)
('etre', 1.1760912590556813)
('smiles', 1.1760912590556813)
('people', 2.316952533289971)
('s', 2.385606273598312)
('faces', 1.1760912590556813)
('services', 1.7501225267834002)
('decade', 1.1760912590556813)
('strategy', 1.7501225267834002)
('gaming', 1.1760912590556813)
('population', 1.1760912590556813)
('offering', 1.1760912590556813)
('everyone', 1.1760912590556813)
('regardless', 1.1760912590556813)
('age', 1.1760912590556813)
('gender', 1.1760912590556813)
('experience', 1.1760912590556813)
('addition', 1.1760912590556813)
('environment', 1.7501225267834002)
('times', 1.7501225267834002)
('something', 1.7501225267834002)
('improves', 1.1760912590556813)
('quality', 1.1760912590556813)
('life', 1.1760912590556813)
('QOL', 2.385606273598312)
('ways', 2.2961250709108754)
('expand', 2.0969100130080567)
('business', 2.387640052032226)
('areas', 1.1760912590556813)
('years', 1.7501225267834002)
('platform', 2.2961250709108754)
('strengths', 1.1760912590556813)
('type', 1.1760912590556813)
('platforms', 1.7501225267834002)
('core', 1.7501225267834002)
('focus', 1.1760912590556813)
('spirit', 1.1760912590556813)
('originality', 1.1760912590556813)
('motto', 1.1760912590556813)
('True', 1.1760912590556813)
('Value', 1.1760912590556813)
('Lies', 1.1760912590556813)
('Individuality', 1.1760912590556813)
(',"', 1.1760912590556813)
('area', 1.1760912590556813)
('apart', 1.1760912590556813)
('health', 1.7501225267834002)
('theme', 1.1760912590556813)
('step', 1.1760912590556813)
('strength', 1.1760912590556813)
('company', 1.7501225267834002)
('approaches', 1.1760912590556813)
('endeavors', 1.1760912590556813)
('turn', 1.1760912590556813)
('user', 1.1760912590556813)
('base', 1.1760912590556813)
('manufacture', 1.1760912590556813)
('sale', 1.1760912590556813)
('Hanafuda', 1.1760912590556813)
('(', 1.1760912590556813)
('cards', 1.1760912590556813)
('playing', 1.1760912590556813)
('card', 1.1760912590556813)
('toy', 1.1760912590556813)
('try', 1.1760912590556813)
('things', 1.1760912590556813)
('history', 1.1760912590556813)
('failures', 1.1760912590556813)
('successes', 1.1760912590556813)
('pioneer', 1.1760912590556813)
('market', 1.1760912590556813)
('materials', 1.1760912590556813)
('technologies', 1.1760912590556813)
('time', 1.1760912590556813)
('position', 1.1760912590556813)
('innovation', 1.1760912590556813)
('line', 1.1760912590556813)
('aim', 1.1760912590556813)
('growth', 1.1760912590556813)
('intends', 1.1760912590556813)
('progress', 1.1760912590556813)
('support', 1.1760912590556813)
('encouragement', 1.1760912590556813)
('shareholders', 1.1760912590556813)
('investors', 1.1760912590556813)
>>> summe.terms  = sorted(summe.terms , key= lambda stud : student[1], reverse=True)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    summe.terms  = sorted(summe.terms , key= lambda stud : student[1], reverse=True)
  File "<pyshell#46>", line 1, in <lambda>
    summe.terms  = sorted(summe.terms , key= lambda stud : student[1], reverse=True)
NameError: name 'student' is not defined
>>> summe.terms  = sorted(summe.terms, key lambda stud : stud[1] , reverse = True)
SyntaxError: invalid syntax
>>> summe.terms  = sorted(summe.terms, key = lambda  stud : stud[1] , reverse = True)
>>> summe.terms
[('entertainment', 2.387640052032226), ('business', 2.387640052032226), ('video', 2.385606273598312), ('game', 2.385606273598312), ('s', 2.385606273598312), ('QOL', 2.385606273598312), ('Nintendo', 2.316952533289971), ('people', 2.316952533289971), ('ways', 2.2961250709108754), ('platform', 2.2961250709108754), ('world', 2.0969100130080567), ('products', 2.0969100130080567), ('expand', 2.0969100130080567), ('Entertainment', 1.7501225267834002), ('hardware', 1.7501225267834002), ('software', 1.7501225267834002), ('home', 1.7501225267834002), ('services', 1.7501225267834002), ('strategy', 1.7501225267834002), ('environment', 1.7501225267834002), ('times', 1.7501225267834002), ('something', 1.7501225267834002), ('years', 1.7501225267834002), ('platforms', 1.7501225267834002), ('core', 1.7501225267834002), ('health', 1.7501225267834002), ('company', 1.7501225267834002), ('launch', 1.1760912590556813), ('System', 1.1760912590556813), ('unique', 1.1760912590556813), ('development', 1.1760912590556813), ('concept', 1.1760912590556813), ('integration', 1.1760912590556813), ('field', 1.1760912590556813), ('industry', 1.1760912590556813), ('industries', 1.1760912590556813), ('Japan', 1.1760912590556813), ('spread', 1.1760912590556813), ('brand', 1.1760912590556813), ('culture', 1.1760912590556813), ('belief', 1.1760912590556813), ('raison', 1.1760912590556813), ('d', 1.1760912590556813), ('etre', 1.1760912590556813), ('smiles', 1.1760912590556813), ('faces', 1.1760912590556813), ('decade', 1.1760912590556813), ('gaming', 1.1760912590556813), ('population', 1.1760912590556813), ('offering', 1.1760912590556813), ('everyone', 1.1760912590556813), ('regardless', 1.1760912590556813), ('age', 1.1760912590556813), ('gender', 1.1760912590556813), ('experience', 1.1760912590556813), ('addition', 1.1760912590556813), ('improves', 1.1760912590556813), ('quality', 1.1760912590556813), ('life', 1.1760912590556813), ('areas', 1.1760912590556813), ('strengths', 1.1760912590556813), ('type', 1.1760912590556813), ('focus', 1.1760912590556813), ('spirit', 1.1760912590556813), ('originality', 1.1760912590556813), ('motto', 1.1760912590556813), ('True', 1.1760912590556813), ('Value', 1.1760912590556813), ('Lies', 1.1760912590556813), ('Individuality', 1.1760912590556813), (',"', 1.1760912590556813), ('area', 1.1760912590556813), ('apart', 1.1760912590556813), ('theme', 1.1760912590556813), ('step', 1.1760912590556813), ('strength', 1.1760912590556813), ('approaches', 1.1760912590556813), ('endeavors', 1.1760912590556813), ('turn', 1.1760912590556813), ('user', 1.1760912590556813), ('base', 1.1760912590556813), ('manufacture', 1.1760912590556813), ('sale', 1.1760912590556813), ('Hanafuda', 1.1760912590556813), ('(', 1.1760912590556813), ('cards', 1.1760912590556813), ('playing', 1.1760912590556813), ('card', 1.1760912590556813), ('toy', 1.1760912590556813), ('try', 1.1760912590556813), ('things', 1.1760912590556813), ('history', 1.1760912590556813), ('failures', 1.1760912590556813), ('successes', 1.1760912590556813), ('pioneer', 1.1760912590556813), ('market', 1.1760912590556813), ('materials', 1.1760912590556813), ('technologies', 1.1760912590556813), ('time', 1.1760912590556813), ('position', 1.1760912590556813), ('innovation', 1.1760912590556813), ('line', 1.1760912590556813), ('aim', 1.1760912590556813), ('growth', 1.1760912590556813), ('intends', 1.1760912590556813), ('progress', 1.1760912590556813), ('support', 1.1760912590556813), ('encouragement', 1.1760912590556813), ('shareholders', 1.1760912590556813), ('investors', 1.1760912590556813)]
>>> summe.CandidSVO = []
>>> summe.getCandidSubjs(None,10)
>>> len(summe.CandidSVO)
1558
>>> summe.CandidSVO = []
>>> summe.getCandidSubjs (None,len(summe.terms)/2)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    summe.getCandidSubjs (None,len(summe.terms)/2)
  File "C:\Users\rihanna\Documents\Pol\ThesisIt\SumMe\Summarizer\Summarizer.py", line 156, in getCandidSubjs
    for term in  terms[start:end]:
TypeError: slice indices must be integers or None or have an __index__ method
>>> summe.getCandidSubjs (None,int len(summe.terms)/2)
SyntaxError: invalid syntax
>>> summe.getCandidSubjs (None,int((summe.terms)/2))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    summe.getCandidSubjs (None,int((summe.terms)/2))
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> summe.getCandidSubjs (None,int(len(summe.terms)/2))
>>> len(summe.CandidSVO)
5120
>>> 
