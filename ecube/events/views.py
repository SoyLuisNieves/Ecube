# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect

from .models import Event
from .forms import EventForm

from django.shortcuts import render

def home_events(request):
	queryset = Event.objects.all()
	context = {
		'events': queryset,
	}
	return render(request, 'index.html', context)

def detail_event(request, id):

	queryset = Event.objects.get(id=id)
	context = {
		'event': queryset,
	}
	return render(request, 'detail_event.html', context)

def create_event(request):
	form = EventForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, 'create_form.html', context)