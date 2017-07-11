from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify

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

	def get_absolute_url(self):
		return reverse("midia:update", kwargs={"id": self.id})