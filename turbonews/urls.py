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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path

from turbonews.core import views

urlpatterns = [
    path('admin/', admin.site.urls),	
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('elements/', views.elements, name="elements"),
    path('ficha-tecnica/', views.fichaTecnica, name="ficha-tecnica"),
    path('ficha-bolt/', views.fichaBolt, name="ficha-bolt"),
    path('ficha-leaf/', views.fichaLeaf, name="ficha-leaf"),
    path('ficha-volvo/', views.fichaVolvo, name="ficha-volvo"),
    # path('\d+', views.fichaTecnica, name="ficha-tecnica")
]