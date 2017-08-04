from django.contrib import admin
from .models import Midia

@admin.register(Midia)
class MidiaModelAdmin(admin.ModelAdmin):
    list_display       = ['analista', 'denuncia', 'linkDenuncia']


    class Meta:
        model = Midia