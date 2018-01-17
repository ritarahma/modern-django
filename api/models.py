# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bucketlist(models.Model):
	"""docstring for Bucketlist"""
	name = models.CharField(max_length=255, blank=False, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""return isi model dlm bntuk string"""
		return "{}".format(self.name)

