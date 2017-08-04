from django.conf.urls import url
from django.contrib import admin

from .views import (

	phishing_new,
	phishing_edit,
	phishing_remove,
	)

urlpatterns = [


    url(r'^create/$', phishing_new, name='phishing_create'),
    url(r'^(?P<pk>\d+)/edit/$', phishing_edit, name='phishing_update'),
    url(r'^(?P<pk>\d+)/delete/$', phishing_remove, name='phishing_delete'),
]
