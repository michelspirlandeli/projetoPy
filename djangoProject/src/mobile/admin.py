from django.contrib import admin
from .models import Mobile

@admin.register(Mobile)
class MobileModelAdmin(admin.ModelAdmin):
    list_display       = ['analista', 'origemDenuncia', 'identificadoAxur']


    class Meta:
        model = Mobile