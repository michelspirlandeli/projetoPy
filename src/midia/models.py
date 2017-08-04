from django.db import models
from django.utils.translation import ugettext_lazy as _

class Midia(models.Model):
    analista = models.CharField(max_length=50)
    denuncia = models.CharField(max_length=50)
    linkDenuncia = models.CharField(max_length=500)
    ticketAxur = models.CharField(max_length=50)
    numeroFacebook = models.IntegerField(null=True)
    status = models.CharField(max_length=50)

    class Meta:
        ordering = ["-analista", "-denuncia"]

    def __str__(self):
        return self.analista
