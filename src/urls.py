from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include

from src.midia import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.midia, name='midia_list'),
    url(r'^', include('src.midia.urls')),
    url(r'^accounts/', include('allauth.urls')), # Django-Allauth
    url(r'^mobile/', include('src.mobile.urls')),
    url(r'^phishing/', include('src.phishing.urls')),

]
