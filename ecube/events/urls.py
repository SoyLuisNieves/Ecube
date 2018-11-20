from django.conf.urls import url

from .views import (
	home_events,
)

urlpatterns = [
	url(r'^$', home_events,name='home_events'),
]