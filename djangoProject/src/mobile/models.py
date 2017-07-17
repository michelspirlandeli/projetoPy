from django.db import models
from django.utils.translation import ugettext_lazy as _

class Mobile(models.Model):
    analista = models.CharField(max_length=50)
    origemDenuncia = models.CharField(max_length=50)
    identificadoAxur = models.CharField(max_length=500)
    ticketAxur = models.CharField(max_length=50)
    urlApp = models.CharField(max_length=500)
    emailDenuncia = models.CharField(max_length=100)

    class Meta:
        ordering = ["-analista", "-origemDenuncia"]

    def __str__(self):
        return self.analista
