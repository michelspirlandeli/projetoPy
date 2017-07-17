from django.conf.urls import url
from django.contrib import admin

from .views import (
	phishing,
	phishing_new,
	phishing_edit,
	phishing_remove,
	)

urlpatterns = [
    url(r'^$', phishing, name='list_phishing'),
    url(r'^create/$', phishing_new, name='create_phishing'),
    url(r'^edit/(?P<pk>\d+)/$', phishing_edit, name='update_phishing'),
    url(r'^delete/(?P<pk>\d+)/$', phishing_remove, name='delete_phishing'),
]
