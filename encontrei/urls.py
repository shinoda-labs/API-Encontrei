"""encontrei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from categoria.api.viewsets import CategoriaViewSet
from estabelecimento.api.viewsets import EstabelecimentoViewSet, EstabelecimentoPreviewViewSet

routers = routers.DefaultRouter(trailing_slash=False)
routers.register(r'api/v1/categoria', CategoriaViewSet, base_name='Categoria')
routers.register(r'api/v1/estabelecimento', EstabelecimentoViewSet, base_name='Estabelecimento')
routers.register(r'api/v1/estabelecimento-preview', EstabelecimentoPreviewViewSet, base_name='EstabelecimentoPreview')

urlpatterns = [
    path('', include(routers.urls)),
    path('api-token-auth', obtain_auth_token),
    path('admin', admin.site.urls),
]
