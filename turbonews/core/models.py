from django.db import models

class Usuario(models.Model):

	def __str__(self):
		return self.username

	username = models.CharField('Username', max_length=50, default="admin")
	senha = models.CharField('Senha', max_length=50, default="123")
	email = models.CharField('Email', max_length=100, default="admin@turbonews.com")
	createdAt = models.DateTimeField('Criado em', auto_now_add=True)
	updatedAt = models.DateTimeField('Atualizado em', auto_now=True)


class Carro(models.Model):

	def __str__(self):
		return self.modelo

	modelo = models.CharField('Modelo', max_length=50)
	marca = models.CharField('Marca', max_length=50)
	ano = models.IntegerField('Ano', blank=True, null=True)
	segmento = models.CharField('Segmento', max_length=50, blank=True, null=True)
	numVendas = models.IntegerField('numVendas', blank=True, null=True)
	imagem = models.ImageField(upload_to="", blank=True, null=True)
	precoFipeFev = models.FloatField('PrecoFipeFev', blank=True, null=True)
	precoFipeMar = models.FloatField('PrecoFipeMar', blank=True, null=True)
	precoFipeAbr = models.FloatField('precoFipeAbr', blank=True, null=True)
	precoFipeMai = models.FloatField('precoFipeMai', blank=True, null=True)
	precoFipeJun = models.FloatField('precoFipeJun', blank=True, null=True)

class Opiniao(models.Model):

	def __Carro__(self):
		return self.carro

	carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
	opiniao = models.TextField('Titulo', default="dummy")

	# Notas
	estilo = models.IntegerField('Estilo', default=0)
	acabamento = models.IntegerField('Acabamento', default=0)
	interior = models.IntegerField('Interior', default=0)
	desempenho = models.IntegerField('Desempenho', default=0)
	consumo = models.IntegerField('Consumo', default=0)

class Comentario(models.Model):

	def __Usuario__(self):
		return self.usuario

	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	comentario = models.TextField('Comentario', default="dummy")