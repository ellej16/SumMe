from django.contrib import admin
from summe_app.models import *
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
import csv

# Register your models here.

admin.site.register(File)