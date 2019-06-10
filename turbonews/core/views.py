from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Carro, Opiniao, Comentario
from .forms import CadastroUsuario, CadastroOpiniao
from .fusioncharts import FusionCharts

def home(request):

	return render(request, "index.html", {"logado" : True})

def login(request):
	loginInvalido = False

	if request.method == "POST":
		username = form.cleaned_data['username']
		senha = form.cleaned_data['senha']

		if Usuario.objects.filter(username=username, senha=senha).exists():
			return redirect('/log')

		else:
			loginInvalido = True

	context = {
		"loginInvalido" : loginInvalido
	}

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
	carroEscolhido = get_object_or_404(Carro, pk=carro_pk)
	opinioes = Opiniao.objects.filter(carro=carroEscolhido)
	medias = []

	for carro in opinioes:
		medias.append((carro.estilo + carro.acabamento + carro.interior + carro.desempenho
					+ carro.consumo) / 5)

	lista = zip(opinioes, medias)

	context = {
		"carros" : Carro.objects.all(),
		"opinioes" : lista,
		"marca" : carroEscolhido.marca,
		"modelo" : carroEscolhido.modelo,
		"imagem" : carroEscolhido.imagem
	}

	return render(request, "elements.html", context)

def fichaTecnica(request):

	carros = [Carro.objects.get(modelo="Bolt"), 
			  Carro.objects.get(modelo="S90 Inscription"),
			  Carro.objects.get(modelo="Leaf")]

	context = {
		"carros" : carros,
		"imagemBolt" : carros[0].imagem,
		"imagemS90" : carros[1].imagem,
		"imagemLeaf" : carros[2].imagem,
		"bolt" : True,
		"s90" : True,
		"leaf" : True
	}

	return render(request, "ficha-tecnica.html", context)

def fichaTecnica_details(request, carro_pk):

	bolt = False
	s90 = False
	leaf = False

	carros = [Carro.objects.get(modelo="Bolt"), 
			  Carro.objects.get(modelo="S90 Inscription"),
			  Carro.objects.get(modelo="Leaf")]

	if carro_pk == 5:
		bolt = True

	elif carro_pk == 6:
		s90 = True

	elif carro_pk == 7:
		leaf = True

	context = {
		"carros" : carros,
		"imagemBolt" : carros[0].imagem,
		"imagemS90" : carros[1].imagem,
		"imagemLeaf" : carros[2].imagem,
		"bolt" : bolt,
		"s90" : s90,
		"leaf" : leaf
	}

	return render(request, "ficha-tecnica.html", context)

def fichaBolt(request):
	return render(request, "ficha-bolt.html")

def fichaLeaf(request):
	return render(request, "ficha-leaf.html")

def fichaVolvo(request):
	return render(request, "ficha-volvo.html")

def noticiaCorolla(request):
	comentarios = Comentario.objects.all()

	context = {
		"comentarios" : comentarios
	}

	return render(request, "noticia-corolla.html", context)

def noticiaGti(request):
	comentarios = Comentario.objects.all()

	context = {
		"comentarios" : comentarios
	}

	return render(request, "noticia-gti.html", context)

def noticiaHrv(request):
	comentarios = Comentario.objects.all()

	context = {
		"comentarios" : comentarios
	}

	return render(request, "noticia-hrv.html", context)

def cadastroOpiniao(request):
	formValido = False

	if request.method == 'POST':
		form = CadastroOpiniao(request.POST)

		if form.is_valid():
			formValido = True
			novaOpiniao = Opiniao()
			
			novaOpiniao.carro = Carro.objects.get(id=form.cleaned_data['modelos'])
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

@csrf_exempt
def graficoPreco(request):
        
	if request.is_ajax():
		modelo = request.POST['modelo']
		carro = Carro.objects.get(modelo=modelo)

		precos = [carro.precoFipeFev, carro.precoFipeMar, carro.precoFipeAbr,
				  carro.precoFipeMai, carro.precoFipeJun]

		return JsonResponse({'result' : 'success', 'precos': precos})

	return render(request, "graficos.html")

@csrf_exempt
def graficoVendas(request):

	if request.is_ajax():
		segmento = request.POST['segmento']
		carros = Carro.objects.filter(segmento=segmento)
		vendas = []

		for c in carros:
			vendas.append({"label": c.modelo, "value": c.numVendas})

		return JsonResponse({'result' : 'success', 'vendas': vendas})

	return render(request, "grafico-vendas.html")

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
	comentarios = Comentario.objects.all()

	context = {
		"comentarios" : lista
	}

	return render(request, "logado/noticia-corolla-log.html", context)

def noticiaGtiLog(request):
	comentarios = Comentario.objects.all()

	context = {
		"comentarios" : comentarios
	}

	return render(request, "logado/noticia-corolla-log.html", context)

def noticiaHrvLog(request):
	comentarios = Comentario.objects.all()

	context = {
		"comentarios" : comentarios
	}

	return render(request, "logado/noticia-corolla-log.html", context)