from django.db import models

class Midia(models.Model):
    analista = models.CharField(max_length=50)
    denuncia = models.CharField(max_length=50)
    linkDenuncia = models.CharField(max_length=500)
    ticketAxur = models.CharField(max_length=50)
    numeroFacebook = models.IntegerField(null=True)

    class Meta:
        ordering = ["-analista", "-denuncia"]

    def __str__(self):
        return self.analista
