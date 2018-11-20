# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sponsors.models import Sponsor

from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=60)
	img_event = models.ImageField(upload_to='img_events', blank=True)
	description = models.TextField()
	start = models.DateTimeField()
	finish = models.DateTimeField()
	address = models.TextField()
	place = models.CharField(max_length=150)
	categories = models.TextField()
	official = models.BooleanField(default=0)
	sponsor = models.ForeignKey(Sponsor)

	def __unicode__(self):
		return self.name

	def get_absolute_url():
		return reverse('events:detail', kwargs={"id":self.id})
