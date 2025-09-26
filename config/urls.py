from django.contrib import admin
from django.urls import path
from app import views  # ajuste "app" para o nome real do seu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('forum/', views.forum, name='forum'),
    path('casosbase/', views.casosbase, name='casosbase'),
    path('login/', views.login, name='login'),
    path('investigar/', views.investigar, name='investigar'),
    path('sobre/', views.sobre, name='sobre'),
]
