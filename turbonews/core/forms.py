from django import forms

class CadastroUsuario(forms.Form):

	username = forms.CharField(label="Username", max_length=50)
	senha = forms.CharField(label="Senha", max_length=50)
	email = forms.CharField(label="Email", max_length=100)