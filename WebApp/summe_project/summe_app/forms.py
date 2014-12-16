from summe_app.models import UploadFile, GetText, GetUrl
from django import forms


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('docfile',)


class GetTextForm(forms.ModelForm):
    class Meta:
        model = GetText
        fields = ('txt',)


class GetUrlForm(forms.ModelForm):
    class Meta:
        model = GetUrl
        fields = ('txt',)