# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Competitor

def competitor_list(request):
	queryset = Competitor.objects.all()
	context = {
		"competitors": queryset
	}
	return render(request, 'competitors_list.html', context)

def competitor_detail(request, id=None):
	queryset = get_object_or_404(Competitor, id=id)
	context = {
		"competitor": queryset,
	}
	return render(request, 'competitor_detail.html', context)