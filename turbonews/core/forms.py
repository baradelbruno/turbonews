from django import forms
from .models import Carro

class CadastroUsuario(forms.Form):

	username = forms.CharField(label="Username", max_length=50, 
	widget=forms.TextInput(attrs={'placeholder':'Nome de usuário', 'class':'form-control input_user'}))
	
	email = forms.CharField(label="Email", max_length=100,
	widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control input_user'}))
	
	senha = forms.CharField(label="Senha", max_length=50,
	widget=forms.TextInput(attrs={'type': 'password', 'placeholder':'Senha', 'class':'form-control input_user'}))