from django import forms
from .models import Phishing

class PhishingForm(forms.ModelForm):
	class Meta:
		model = Phishing
		fields = [
			'analista', 
			'primeiraNotificacao', 
			'origemDenuncia', 
			'identificadoAxur', 
			'ticketAxur',
			'origemProvedor',
			'provedorResponsavel',
			'urlFalsa',
			'dominioAtacado',
			'tipoTratamento',
			'status',
		]