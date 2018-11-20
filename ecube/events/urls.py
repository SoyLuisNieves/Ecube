from django.conf.urls import url

from .views import (
	home_events,
	detail_event,
	create_event,
)

urlpatterns = [
	url(r'^create/$', create_event),
	url(r'^$', home_events,name='home_events'),
	url(r'^detail/(?P<id>[\d+]+)/', detail_event, name='detail'),
]