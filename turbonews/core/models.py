from django.db import models

class UsuarioManager(models.Manager):
	def select(self, query):
		return self.get_queryset()

class Usuario(models.Model):

	def __str__(self):
		return self.username

	username = models.CharField('Username', max_length=50, default="admin")
	senha = models.CharField('Senha', max_length=50, default="123")
	email = models.CharField('Email', max_length=100, default="admin@turbonews.com")
	createdAt = models.DateTimeField('Criado em', auto_now_add=True)
	updatedAt = models.DateTimeField('Atualizado em', auto_now=True)

	objects = UsuarioManager()