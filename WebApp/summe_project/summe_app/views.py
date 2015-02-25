from django.shortcuts import render
from summe_app.models import File
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from summe_app.forms import UploadFileForm
from summe_app.models import UploadFile
from summe_app.models import GetText
from summe_app.forms import GetTextForm, GetUrlForm
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
import io
from django.core.servers.basehttp import FileWrapper

import unicodedata
import summe_app.Summarizer.Summarizer as sumMe

# Create your views here.


def index(request):
    return render(request, "index.html")


def index_3(request):
    return render(request, "index3.html")


def index_2(request):
    return render(request, "index2.html")


def index_4(request):
    return render(request, "index4.html")


def dummy(request):
    return render(request, "dummy.html")


def waiting(request):
    return render(request, "waiting.html")


def get_here(text):
    return text

'''LAHAT NG NASA BABA,CALL MO LANG SILA SA FUNCTION MO PARA MAKUHA UNG VALUES NILA'''
'''ITO PARA SA WEB CRAWL FUNCTION'''


def text_from_web_crawler(text):
    return text

'''ITO PARA SA UPLOAD FILE, DITO NYA BINASA UNG FILE,JUST CALL THIS FUNCTION'''


def get_file(fail):
    con = " "
    newfile = None
    with open('static/files/%s' % fail, 'r') as f:
        temp = f.readlines()
        newfile = con.join(temp)
        #unicodedata.normalize('NFKD', newfile).encode('utf8','ignore')
            
        sumMe.clearMem()
        sumMe.getSentences(newfile)
        sumMe.doGetAll()

    return sumMe.gvActSum()

'''TAWAGIN MO LANG TONG FUNCTION NA TO PARA MAKUHA MO UNG VALUE NG TEXTAREA'''


def get_text(text):
    #unicodedata.normalize('NFKD', str(text)).encode('utf-8','ignore')
    sumMe.clearMem()
    sumMe.getSentences(text)



'''LAHAT NG NASA TAAS,DITO MO IPAPASA UNG VALUE'''


def download(request):
    myfile = io.StringIO()
    text = request.POST['text']
    #print(function_ni_paul_kuno(text))
    myfile.write(get_here(text))
    myfile.flush()
    myfile.seek(0)
    response = HttpResponse(FileWrapper(myfile), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=Test_file.txt'
    return response


def upload_file(request):
    text =""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadFile(docfile=request.FILES['docfile'])
            instance.save()
            print(request.FILES['docfile'])
            #return HttpResponse("uploaded %s" % request.FILES['docfile'])
            test = get_file(request.FILES['docfile'])
            '''^^^^^JUST PASS THE VALUE HERE!!!'''
            for tx in test:
                text = text+" "+tx
            return render(request, "testOutput.html", {"text" : text})
    else:
        form = UploadFileForm()

    '''NO NEED, DUMMY LANG TONG BABA. TEST
    args = {}
    args.update(csrf(request))

    args['form'] = form
    '''

    return render(request, 'index2.html')




def get_text_holder(request):
    text=""

    if request.method == 'POST':
        print("another")
        form = GetTextForm(request.POST)
        if form.is_valid():
            text_from_form = form.cleaned_data['txt']
            print(text_from_form)
            get_text(text_from_form)
       # '''^^^^^JUST PASS THE VALUE HERE!!!'''
            sumMe.doGetAll()
            test = sumMe.gvActSum()
            for tx in test:
                text = text+" "+tx
           #return HttpResponse(text['txt'])
            
    return render(request, "testOutput.html", {"text" : text})
    #else:
     #   return render(request, "testOutput.html", {"text" : text})
    #return render(request, "testOutput.html", {"text" : "fml"})



def web_crawler(request):
    if request.method == 'POST':
        form = GetUrlForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data
            url = text['txt']
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text)
            # web crawl
            text_list = [""]
            con = '\n'
            output = [""]
            for paragraph in soup.findAll('p'):
                #text = paragraph.string
                text_list.append(paragraph.string)
                new = [(x if x is not None else '') for x in text_list]
                new2 = con.join(new)
                #new = con.join(text)
                print(new2)
                output = text_from_web_crawler(new2)
                '''^^^^^JUST PASS THE VALUE HERE!!!'''
            return render(request, "testOutput.html", {"text" : output})
            #return render(request, "testOutput2.html")
            #return HttpResponse("success")
        else:
            return HttpResponse("fail")


'''NEVERMIND THIS SHIT SA BABA'''

'''
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['title'])
        return HttpResponse("uploaded %s"%request.FILES['title'])
    else:
        form = UploadFileForm()
        return render(request, 'index3.html', {'form': form})

def handle_uploaded_file(f):
    import datetime as dt
    from summe_project import settings
    now = dt.datetime.now()
    with open("%s\\%s%s%s%s%s%s_%s"%(settings.MEDIA_ROOT, now.year, now.month, now.day, now.hour, now.minute, now.second, f), 'w+') as destination:
        print(f.readlines())
        destination.writelines(f.readlines())
'''

'''
new
'''
'''

def f_form(request):
    if request.method == 'POST':
        form = (request.POST, request.FILES)
        handle_get_text_form(request.FILES['texttext'])
        return HttpResponse("uploaded file")
    else:
        form = UploadFileForm()
        return render(request, 'index3.html', {'form': form})


def handle_get_text_form(g):

    from summe_project import settings
    form = cgi.FieldStorage()
    with open('fileToWrite.txt' % settings.MEDIA_ROOT, 'w+') as fileOutput:
        fileOutput.write(form.getValue('texttext'))
'''