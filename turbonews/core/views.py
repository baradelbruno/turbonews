from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .forms import CadastroUsuario

# Create your views here.
def home(request):
	return render(request, "index.html")

def cadastro(request):
	templateName = "cadastro.html"
	formValido = False

	if request.method == "POST":
		form = CadastroUsuario(request.POST)

		if form.is_valid():
			formValido = True
			novoUsuario = Usuario()
			novoUsuario.username = form.cleaned_data['username']
			novoUsuario.senha = form.cleaned_data['senha']
			novoUsuario.email = form.cleaned_data['email']
			novoUsuario.save()
			form = CadastroUsuario()

	else: 
		form = CadastroUsuario()

	context = {
		"form": form,
		"formValido" : formValido
	}

	return render(request, templateName, context)

def login(request):
	templateName = "login.html"
	loginValido = True

	if request.method == "POST":
		username = request.POST['username']
		senha = request.POST['senha']
		templateName = "index_log.html"

		if Usuario.objects.filter(username=username, senha=senha).exists():
			return render(request, templateName)

		else:
			loginValido = False

	context = {
		"loginValido" : loginValido
	}

	return render(request, templateName, context)

def elements(request):
	return render(request, "elements.html")

def fichaTecnica(request):
	return render(request, "ficha-tecnica.html")

def fichaBolt(request):
	return render(request, "ficha-bolt.html")

def fichaLeaf(request):
	return render(request, "ficha-leaf.html")

def fichaVolvo(request):
	return render(request, "ficha-volvo.html")