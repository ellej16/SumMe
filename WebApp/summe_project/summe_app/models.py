from django.db import models

# Create your models here.


class File(models.Model):
    textFile = models.CharField(max_length=200)


    def __str__(self):
        return self.textFile


class UploadFile(models.Model):
    docfile = models.FileField(upload_to='files/%Y/%m/%d')
