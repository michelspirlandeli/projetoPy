from django.conf.urls import url
from django.contrib import admin

from .views import (
	midia_list,
	midia_new,
	midia_edit,
	midia_remove,
	)

urlpatterns = [
    url(r'^$', midia_list, name='list'),
    url(r'^create/$', midia_new, name='create'),
    url(r'^(?P<slug>[\w-]+)/edit/$', midia_edit, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', midia_remove, name='delete'),
]