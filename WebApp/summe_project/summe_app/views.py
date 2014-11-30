from django.shortcuts import render
from summe_app.models import File
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from summe_app.forms import UploadFileForm
from summe_app.models import UploadFile
from django.core.context_processors import csrf


# Create your views here.


def index(request):
    return render(request, "index.html")


def index_3(request):
    return render(request, "index3.html")


def index_2(request):
    return render(request, "index2.html")


def uploadFile(request):
	if request.method == "POST":
		File(textFile=request.POST['title']).save()
		return render(request,"index2.html", {"message":"Successfully summarized!"})
	else:
		return render(request,"index.html",{"message": ""})


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