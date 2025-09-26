from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def forum(request):
    return render(request, 'forum.html')

def casosbase(request):
    return render(request, 'casosbase.html')

def login(request):
    return render(request, 'login.html')

def investigar(request):
    return render(request, 'investigar.html')

def sobre(request):
    return render(request, 'sobre.html')

def investigações(request):
    return render(request, 'investigacoes.html')
