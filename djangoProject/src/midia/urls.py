from django.conf.urls import url
from django.contrib import admin

from .views import (
	midia,
	midia_new,
	midia_edit,
	midia_remove,
	)

urlpatterns = [
    url(r'^$', midia, name='list'),
    url(r'^create/$', midia_new, name='create'),
    url(r'^edit/(?P<pk>\d+)/$', midia_edit, name='update'),
    url(r'^delete/(?P<pk>\d+)/$', midia_remove, name='delete'),
]
