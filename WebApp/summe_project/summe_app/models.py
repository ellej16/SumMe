from django.db import models

# Create your models here.


class File(models.Model):
    textFile = models.CharField(max_length=200)


    def __str__(self):
        return self.textFile


class UploadFile(models.Model):
    docfile = models.FileField(upload_to='files')


class GetText(models.Model):
    txt = models.CharField(max_length =200)

class GetUrl(models.Model):
    txt = models.CharField(max_length =200)