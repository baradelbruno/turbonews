from django import forms

class CadastroUsuario(forms.Form):

<<<<<<< HEAD
	username = forms.CharField(label="Username", max_length=50, 
	widget=forms.TextInput(attrs={'placeholder':'Nome de usuário', 'class':'form-control input_user'}))
	
	email = forms.CharField(label="Email", max_length=100,
	widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control input_user'}))
	
	senha = forms.CharField(label="Senha", max_length=50,
	widget=forms.TextInput(attrs={'placeholder':'Senha', 'class':'form-control input_user'}))
=======
	username = forms.CharField(label="Username", max_length=50)
	senha = forms.CharField(label="Senha", max_length=50)
	email = forms.CharField(label="Email", max_length=100)
>>>>>>> master
