from django.db import models
from django.utils.translation import ugettext_lazy as _

class Phishing(models.Model):
    analista = models.CharField(max_length=50)
    primeiraNotificacao = models.CharField(max_length=50)
    origemDenuncia = models.CharField(max_length=500)
    identificadoAxur = models.CharField(max_length=50)
    ticketAxur = models.CharField(max_length=50)
    origemProvedor = models.CharField(max_length=50)
    provedorResponsavel = models.CharField(max_length=50)
    urlFalsa = models.CharField(max_length=500)
    dominioAtacado = models.CharField(max_length=500)
    tipoTratamento = models.CharField(max_length=500)

    class Meta:
        ordering = ["-analista", "-primeiraNotificacao"]

    def __str__(self):
        return self.analista
