from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Apk(models.Model):
	created = models.DateTimeField(_('Created date'), null=True, blank=True, auto_now_add=True)
	file = models.FileField(_('File'), upload_to='apk/%Y/%m/')
	name = models.CharField(_('Name'), max_length=255, null=True, blank=True)
	os = models.CharField(_('Os'), max_length=255, null=True, blank=True)
	port = models.CharField(_('Port'), max_length=255, null=True, blank=True)
	domain = models.CharField(_('Domain'), max_length=255, null=True, blank=True)
	type = models.CharField(_('Type'), max_length=255, null=True, blank=True)
	description = models.TextField(_('Description'), null=True, blank=True)


	

