from django.conf.urls import url
from django.contrib import admin

from .views import (
	midia_new,
	midia_edit,
	midia_remove,
	)

urlpatterns = [
    url(r'^create/$', midia_new, name='midia_create'),
    url(r'^(?P<pk>\d+)/edit/$', midia_edit, name='midia_update'),
    url(r'^(?P<pk>\d+)/delete/$', midia_remove, name='midia_delete'),
]
