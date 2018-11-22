# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

class Competitor(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	age = models.PositiveIntegerField()
	avatar = models.ImageField(upload_to='avatars_competitors')
	country = models.CharField(max_length=120)
	wca_id = models.CharField(max_length=10)
	gender = models.CharField(max_length=6)
	competitions = models.PositiveIntegerField(default=0)
	solves = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "%s - %s" %(self.first_name, self.last_name)

	def get_absolute_url(request):
		return reverse("competitors:competitor_detail", kwargs={"id": id})