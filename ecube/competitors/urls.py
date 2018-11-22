from django.conf.urls import url

from .views import (
	competitor_list,
	competitor_detail,
)

urlpatterns = [
	url(r'^$', competitor_list,name='competitor_list'),
	url(r'^(?P<id>[\d+]+)/', competitor_detail, name='competitor_detail'),
]