from django import forms
from .models import Carro

class CadastroUsuario(forms.Form):

	username = forms.CharField(label="Username", max_length=50, 
	widget=forms.TextInput(attrs={'placeholder':'Nome de usuário', 'class':'form-control input_user'}))
	
	email = forms.CharField(label="Email", max_length=100,
	widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control input_user'}))
	
	senha = forms.CharField(label="Senha", max_length=50,
	widget=forms.TextInput(attrs={'placeholder':'Senha', 'class':'form-control input_user'}))

class CadastroOpiniao(forms.Form):

	queryset = Carro.objects.all()
	modelos = [[q.id, q] for q in queryset]
	notas = [[i, i] for i in range(0, 11)]

	modelos = forms.CharField(widget=forms.Select(choices=modelos))
	pau = forms.CharField(widget=forms.Select(choices=notas))
	titulo = forms.CharField(label="Titulo", widget=forms.Textarea)
	pros = forms.CharField(label="Pros", widget=forms.Textarea)
	contras = forms.CharField(label="Contras", widget=forms.Textarea)
	geral = forms.CharField(label="Geral", widget=forms.Textarea)