from django import forms
from django.contrib import auth
from app.models import FileUpload

class FileUploadForm(forms.ModelForm):

	class Meta:
		model = FileUpload
		fields = ['file']
