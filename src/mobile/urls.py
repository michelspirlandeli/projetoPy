from django.conf.urls import url
from django.contrib import admin

from .views import (
	mobile,
	mobile_new,
	mobile_edit,
	mobile_remove,
	)

urlpatterns = [
    url(r'^$', mobile, name='mobile_list'),
    url(r'^create/$', mobile_new, name='mobile_create'),
    url(r'^(?P<pk>\d+)/edit/$', mobile_edit, name='mobile_update'),
    url(r'^(?P<pk>\d+)/delete/$', mobile_remove, name='mobile_delete'),
]

