# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Sponsor(models.Model):
	name = models.CharField(max_length=50)
	img_sponsor = models.ImageField(upload_to='img_sponsors')
	country = models.CharField(max_length=60)

	def __unicode__(self):
		return self.name