from django.shortcuts import render
from summe_app.models import File
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.

def index(request):
    return render(request, "index.html")

def index_3(request):
    return render(request, "index3.html")

def uploadFile(request):
	if request.method == "POST":
		File(textFile=request.POST['title']).save()
		return render(request,"index2.html", {"message":"Successfully summarized!"})
	else:
		return render(request,"index.html",{"message": ""})