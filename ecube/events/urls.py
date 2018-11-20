from django.conf.urls import url

from .views import (
	home_events,
	detail_event,
	create_event,
	event_update,
)

urlpatterns = [
	url(r'^create/$', create_event),
	url(r'^$', home_events,name='home_events'),
	url(r'^detail/(?P<id>[\d+]+)/', detail_event, name='detail'),
	url(r'^update/(?P<id>[\d+]+)/', event_update, name='update'),
]