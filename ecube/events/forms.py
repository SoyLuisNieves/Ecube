from django import forms

from .models import Event

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = [
			"name",
			"img_event",
			"description",
			"start",
			"finish",
			"address",
			"place",
			"categories",
			"official",
			"sponsor",
		]