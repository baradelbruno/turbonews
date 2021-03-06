from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Carro, Opiniao, Comentario
from .forms import CadastroUsuario
from .fusioncharts import FusionCharts

usuario = {
	"username" : "default", 
	"logado" : False
}

def home(request):

    context = {
        "usuario" : usuario['username'],
        "logado" : usuario['logado']
    }
    
    return render(request, "index.html", context)
    
def login(request):
	loginInvalido = False

	if request.method == "POST":
		username = request.POST['username']
		senha = request.POST['senha']

		if Usuario.objects.filter(username=username, senha=senha).exists():
			usuario['username'] = username
			usuario['logado'] = True
			
			context = {
				"usuario" : usuario['username'],
				"logado" : usuario['logado']
			}

			return render(request, "index.html", context)

		else:
			loginInvalido = True

	context = {
		"loginInvalido" : loginInvalido
	}

	return render(request, "login.html", context)

def logout(request):
	usuario['username'] = "default"
	usuario['logado'] = False

	return redirect("home")

def cadastro(request):
	templateName = "cadastro.html"
	formValido = False

	if request.method == "POST":
		form = CadastroUsuario(request.POST)

		if form.is_valid():
			novoUsuario = Usuario()
			novoUsuario.username = form.cleaned_data['username']
			novoUsuario.senha = form.cleaned_data['senha']
			novoUsuario.email = form.cleaned_data['email']

			if not Usuario.objects.filter(username=novoUsuario.username).exists():
				novoUsuario.save()
				formValido = True
			
			form = CadastroUsuario()

	else: 
		form = CadastroUsuario()

	context = {
		"form" : form,
		"formValido" : formValido,
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
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
		"imagem" : carroEscolhido.imagem,
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
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
		"leaf" : True,
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
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
		"leaf" : leaf,
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}

	return render(request, "ficha-tecnica.html", context)

def fichaBolt(request):
	context = {
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}

	return render(request, "ficha-bolt.html", context)

def fichaLeaf(request):
	context = {
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}

	return render(request, "ficha-leaf.html", context)

def fichaVolvo(request):
	context = {
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}

	return render(request, "ficha-volvo.html", context)

@csrf_exempt
def noticiaCorolla(request):
	comentarios = Comentario.objects.filter(noticia=1)

	if request.method == "POST":
		novoComentario = Comentario()

		if request.POST['comentario'] != "":
			if Usuario.objects.filter(username=usuario['username']).exists():
				username = Usuario.objects.get(username=usuario['username'])
				novoComentario.usuario = username
				novoComentario.noticia = 1
				novoComentario.comentario = request.POST['comentario']
				novoComentario.save()
			else:
				return redirect('login')

	context = {
		"comentarios" : comentarios,
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}

	return render(request, "noticia-corolla.html", context)

def noticiaGti(request):
	comentarios = Comentario.objects.filter(noticia=2)

	if request.method == "POST":
		novoComentario = Comentario()

		if request.POST['comentario'] != "":
			if Usuario.objects.filter(username=usuario['username']).exists():
				username = Usuario.objects.get(username=usuario['username'])
				novoComentario.usuario = username
				novoComentario.noticia = 2
				novoComentario.comentario = request.POST['comentario']
				novoComentario.save()
			else:
				return redirect('login')

	context = {
		"comentarios" : comentarios,
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}
	return render(request, "noticia-gti.html", context)

def noticiaHrv(request):
	comentarios = Comentario.objects.filter(noticia=3)

	if request.method == "POST":
		novoComentario = Comentario()

		if request.POST['comentario'] != "":
			if Usuario.objects.filter(username=usuario['username']).exists():
				username = Usuario.objects.get(username=usuario['username'])
				novoComentario.usuario = username
				novoComentario.noticia = 3
				novoComentario.comentario = request.POST['comentario']
				novoComentario.save()
			else:
				return redirect('login')

	context = {
		"comentarios" : comentarios,
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}

	return render(request, "noticia-hrv.html", context)

def cadastroOpiniao(request):
	formValido = False  

	if usuario['logado'] == False:
		return redirect('login')

	carros = Carro.objects.all()

	if request.method == 'POST':
		if request.POST['opiniao'] != "":
			novaOpiniao = Opiniao()
			novaOpiniao.carro = Carro.objects.get(modelo=request.POST['carro'])
			novaOpiniao.opiniao = request.POST['opiniao']
			novaOpiniao.estilo = request.POST['estilo']
			novaOpiniao.acabamento = request.POST['acabamento']
			novaOpiniao.interior = request.POST['interior']
			novaOpiniao.desempenho = request.POST['desempenho']
			novaOpiniao.consumo = request.POST['consumo']
				
			novaOpiniao.save()
			formValido = True

	context = {
		"carros" : carros,
		"formValido" : formValido,
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
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

	context = {
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}
        
	return render(request, "grafico-preco.html", context)

@csrf_exempt
def graficoVendas(request):

	if request.is_ajax():
		segmento = request.POST['segmento']

		print(request.POST)

		if 'marca' not in request.POST:
			carros = Carro.objects.filter(segmento=segmento)
		else:
			marca = request.POST['marca']
			carros = Carro.objects.filter(segmento=segmento, marca=marca)
		
		vendas = []

		for c in carros:
			vendas.append({"label": c.modelo, "value": c.numVendas})

		return JsonResponse({'result' : 'success', 'vendas': vendas})

	context = {
		"usuario" : usuario['username'],
		"logado" : usuario['logado']
	}
        
	return render(request, "grafico-vendas.html", context)