from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include

from src.midia import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^midia/', include('src.midia.urls')),
    url(r'^mobile/', include('src.mobile.urls')),
    url(r'^phishing/', include('src.phishing.urls')),
]
