from django.contrib import admin
from .models import Phishing

@admin.register(Phishing)
class PhishingModelAdmin(admin.ModelAdmin):
    list_display       = ['analista', 'primeiraNotificacao', 'origemDenuncia']


    class Meta:
        model = Phishing