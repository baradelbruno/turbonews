from django.contrib import admin
from .models import Usuario, Carro, Opiniao, Comentario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Carro)
admin.site.register(Opiniao)
admin.site.register(Comentario)