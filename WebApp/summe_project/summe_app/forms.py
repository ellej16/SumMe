from summe_app.models import UploadFile
from django import forms


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('docfile',)