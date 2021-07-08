from django.conf.urls import url
from django.contrib import admin

from .views import (
	mobile,
	mobile_new,
	mobile_edit,
	mobile_remove,
	)

urlpatterns = [
    url(r'^$', mobile, name='list_mobile'),
    url(r'^create/$', mobile_new, name='create_mobile'),
    url(r'^edit/(?P<pk>\d+)/$', mobile_edit, name='update_mobile'),
    url(r'^delete/(?P<pk>\d+)/$', mobile_remove, name='delete_mobile'),
]
