from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Carro, Opiniao
from .forms import CadastroUsuario, CadastroOpiniao
from .fusioncharts import FusionCharts

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
		"form" : form,
		"formValido" : formValido
	}

	return render(request, templateName, context)

def elements(request):

	return elements_details(request, 1)

def elements_details(request, carro_pk):
	carroEscolhido = Carro.objects.filter(pk=carro_pk)
	opinioes = Opiniao.objects.filter(idCarro=carroEscolhido[0])
	medias = []

	for carro in opinioes:
		medias.append((carro.estilo + carro.acabamento + carro.interior + carro.desempenho
					+ carro.consumo) / 5)

	lista = zip(opinioes, medias)

	context = {
		"carros" : Carro.objects.all(),
		"opinioes" : lista,
		"marca" : carroEscolhido[0].marca,
		"modelo" : carroEscolhido[0].modelo
	}

	return render(request, "elements.html", context)

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
	formValido = False

	if request.method == 'POST':
		form = CadastroOpiniao(request.POST)

		if form.is_valid():
			formValido = True
			novaOpiniao = Opiniao()
			carro = Carro.objects.filter(id=form.cleaned_data['modelos'])
			
			novaOpiniao.idCarro = carro[0]
			novaOpiniao.opiniao = form.cleaned_data['opiniao']
			novaOpiniao.estilo = form.cleaned_data['estilo']
			novaOpiniao.acabamento = form.cleaned_data['acabamento']
			novaOpiniao.interior = form.cleaned_data['interior']
			novaOpiniao.desempenho = form.cleaned_data['desempenho']
			novaOpiniao.consumo = form.cleaned_data['consumo']
			novaOpiniao.save()
			
			form = CadastroOpiniao()

	else:
		form = CadastroOpiniao()

	context = {
		"form" : form,
		"formValido" : formValido
	}

	return render(request, "cadastro-opiniao.html", context)

def graficos(request):
        
    if request.method == 'POST':
    	modelo = request.POST['filtro']
    	print(modelo)

    	carro = Carro.objects.filter(modelo=modelo)

    	dataSource = {
	      "chart": {
	        "caption": "Tabela FIPE",
	        "xAxisName": "Data",
	        "yAxisName": "Preço",
	        "theme": "fusion"
	      },

	      "data": [
	        {
	          "label": "FEV/2019",
	          "value": carro[0].precoFipeFev
	        },
	        {
	          "label": "MAR/2019",
	          "value": carro[0].precoFipeMar
	        },
	        {
	          "label": "ABR/2019",
	          "value": carro[0].precoFipeAbr
	        },
	        {
	          "label": "MAI/2019",
	          "value": carro[0].precoFipeMai
	        },
	        {
	          "label": "JUN/2019",
	          "value": carro[0].precoFipeJun
	        }]
	    }

    	graficoPreco = FusionCharts("line", "graficoPreco", "600", "400", "grafico-container", "json", dataSource)

    	return render(request, "graficos.html", {
        	'output' : graficoPreco.render(),
    	})

    return render(request, "graficos.html")

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