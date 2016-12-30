from __future__ import unicode_literals

from django.db import models
from app.utils import get_upload_file_path
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class FileUpload(models.Model):
	file = models.ImageField(_('Upload File'), upload_to=get_upload_file_path)

	def __unicode__(self):
		return str(self.file.name)
