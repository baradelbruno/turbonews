"""turbonews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path

from turbonews.core import views

urlpatterns = [
    path('admin/', admin.site.urls),	
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('elements', views.elements, name="elements"),
    path('elements/<int:carro_pk>', views.elements_details, name="elements_details"),
    path('ficha-tecnica', views.fichaTecnica, name="ficha-tecnica"),
    path('ficha-tecnica/<int:carro_pk>', views.fichaTecnica_details, name="ficha-tecnica_details"),
    path('ficha-bolt', views.fichaBolt, name="ficha-bolt"),
    path('ficha-leaf', views.fichaLeaf, name="ficha-leaf"),
    path('ficha-volvo', views.fichaVolvo, name="ficha-volvo"),
    path('noticia-corolla', views.noticiaCorolla, name="noticia-corolla"),
    path('noticia-gti', views.noticiaGti, name="noticia-gti"),
    path('noticia-hrv', views.noticiaHrv, name="noticia-hrv"),  
    path('cadastro-opiniao', views.cadastroOpiniao, name="cadastro-opiniao"),
    path('grafico-preco', views.graficoPreco, name="grafico-preco"),
    path('grafico-vendas', views.graficoVendas, name="grafico-vendas"),
    
    # path('log', views.homeLog, name="home-log"),
    # path('elements-log', views.elementsLog, name="elements-log"),
    # path('ficha-tecnica-log', views.fichaTecnicaLog, name="ficha-tecnica-log"),
    # path('ficha-bolt-log', views.fichaBoltLog, name="ficha-bolt-log"),
    # path('ficha-leaf-log', views.fichaLeafLog, name="ficha-leaf-log"),
    # path('ficha-volvo-log', views.fichaVolvoLog, name="ficha-volvo-log"),
    # path('noticia-corolla-log', views.noticiaCorollaLog, name="noticia-corolla-log"),
    # path('noticia-gti-log', views.noticiaGtiLog, name="noticia-gti-log"),
    # path('noticia-hrv-log', views.noticiaHrvLog, name="noticia-hrv-log"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
