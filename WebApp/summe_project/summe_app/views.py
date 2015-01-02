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

'''
def uploadFile(request):
	if request.method == "POST":
		File(textFile=request.POST['title']).save()
		return render(request,"index2.html", {"message":"Successfully summarized!"})
	else:
		return render(request,"index.html",{"message": ""})
'''

'''added January 1,2015'''
'''working right now'''

def function_ni_paul_kuno(text):
    return text.upper()


def sample_text():
    text = "justin ay pogi"
    return text

def get_here(text):
    return text

def download(request):
    myfile = io.StringIO()
    text = request.POST['text']
    #print(function_ni_paul_kuno(text))
    myfile.write(function_ni_paul_kuno(text))
    myfile.flush()
    myfile.seek(0)
    response = HttpResponse(FileWrapper(myfile), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=Test_file.txt'
    return response

'''end here'''

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadFile(docfile=request.FILES['docfile'])
            instance.save()
            #return HttpResponse("uploaded %s" % request.FILES['docfile'])
            return render(request, "testOutput.html")
    else:
        form = UploadFileForm()

    '''NO NEED, DUMMY LANG TONG BABA. TEST
    args = {}
    args.update(csrf(request))

    args['form'] = form
    '''

    return render(request, 'index2.html')

'''NEW METHOD FOR READ/WRITE FILE'''

'''
def read_file():
    f = open("static/files/Jokes_2.txt", "w")
    f.write(str(p))
    f.close()
    p.close()
'''

'''END HERE'''


def get_text(request):
    if request.method == 'POST':
        form = GetTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['txt']
            print(text)
            #return HttpResponse(text['txt'])
            return render(request, "testOutput.html", {"text" : text})
    else:
        return HttpResponse("fail")


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
            for paragraph in soup.findAll('p'):
                result = paragraph.string
                print(result)
            return render(request, "testOutput2.html")
            #return HttpResponse("success")
        else:
            return HttpResponse("fail")



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

def get_text_form(request):
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