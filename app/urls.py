from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('forum/', views.forum, name='forum'),  # Página do fórum
    path('casosbase/', views.casosbase, name='casosbase'),  # Página de casos base
    path('login/', views.login, name='login'),  # Página de login
    path('investigar/', views.investigar, name='investigar'),  # Página de investigar
    path('sobre/', views.sobre, name='sobre'),  # Página sobre
    path('investigacoes/', views.investigacoes, name='investigacoes'),  # Página de investigações
    path('salvar-caso/', views.salvar_caso, name='salvar_caso'),  # Endpoint para salvar caso
    path('api/casos/<str:categoria>/', views.listar_casos, name='listar_casos'),  # API para listar casos por categoria
]
