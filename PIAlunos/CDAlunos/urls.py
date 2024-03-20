from django.urls import path
from . import views

urlpatterns = [
   path('', views.base, name = 'base'),
   path('inicio', views.base, name = 'base'),
   path('cadastro', views.pagina_cadastro, name='cadastro'),
   path('concorrentes', views.mostrar_cadastros, name='concorrentes')
]
