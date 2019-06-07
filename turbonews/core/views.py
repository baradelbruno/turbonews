from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Carro
from .forms import CadastroUsuario, CadastroOpiniao

def home(request):
	return render(request, "index.html")

def login(request):
	loginInvalido = False

	if request.method == "POST":
		username = request.POST['username'] # form.cleaned_data['username']?
		senha = request.POST['senha']       # form.cleaned_data['senha']?

		if Usuario.objects.filter(username=username, senha=senha).exists():
			return redirect('/log')

		else:
			loginInvalido = True

	context = {
		"loginInvalido" : loginInvalido
	}

	print(loginInvalido)
	return render(request, "login.html", context)

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

def noticiaCorolla(request):
	return render(request, "noticia-corolla.html")

def noticiaGti(request):
	return render(request, "noticia-gti.html")

def noticiaHrv(request):
	return render(request, "noticia-hrv.html")

def cadastroOpiniao(request):

	if request.method == 'POST':
		form = CadastroOpiniao(request.POST)
		pau = request.POST['modelos']
		penis = request.POST['notas']

		print(pau)
		print(penis) 

	else:
		form = CadastroOpiniao()

	context = {
		"form" : form
	}

	return render(request, "cadastro-opiniao.html", context)

# Views do usuário logado

def homeLog(request):
	return render(request, "logado/index-log.html")

def elementsLog(request):
	return render(request, "logado/elements-log.html")

def fichaTecnicaLog(request):
	return render(request, "logado/ficha-tecnica-log.html")

def fichaBoltLog(request):
	return render(request, "logado/ficha-bolt-log.html")

def fichaLeafLog(request):
	return render(request, "logado/ficha-leaf-log.html")

def fichaVolvoLog(request):
	return render(request, "logado/ficha-volvo-log.html")

def noticiaCorollaLog(request):
	return render(request, "logado/noticia-corolla-log.html")

def noticiaGtiLog(request):
	return render(request, "logado/noticia-gti-log.html")

def noticiaHrvLog(request):
	return render(request, "logado/noticia-hrv-log.html")