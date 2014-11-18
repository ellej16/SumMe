from django.shortcuts import render
from summe_app.models import File

# Create your views here.

def index(request):
    return render(request, "index.html")

def uploadFile(request):
	if request.method == "POST":
		File(textFile=request.POST['title']).save()
		return render(request,"index2.html", {"message":"Successfully summarized!"})
	else:
		return render(request,"index.html",{"message": ""})