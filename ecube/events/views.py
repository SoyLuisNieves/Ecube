# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Event

from django.shortcuts import render

def home_events(request):
	queryset = Event.objects.all()
	context = {
		'events': queryset,
	}
	return render(request, 'index.html', context)