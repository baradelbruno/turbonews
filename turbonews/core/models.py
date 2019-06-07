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
	precoFipe = models.FloatField('PrecoFipe', blank=True, null=True)

class Opiniao(models.Model):

	def __str__(self):
		return self.idCarro

	idCarro = models.IntegerField('idCarro')
	titulo = models.TextField('Titulo')
	pros = models.TextField('Pros')
	contras = models.TextField('Contras')
	geral = models.TextField('Geral')

	# Notas
	estilo = models.IntegerField('Estilo')
	acabamento =  models.IntegerField('Acabamento')