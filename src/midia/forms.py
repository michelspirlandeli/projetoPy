from django import forms
from .models import Midia

class MidiaForm(forms.ModelForm):
	class Meta:
		model = Midia
		fields = [
			'analista', 
			'denuncia', 
			'linkDenuncia', 
			'ticketAxur', 
			'numeroFacebook',
			'status',
		]