from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'HortaDigital/home.html', context={
        'name':'Vinicius Marques',
    })

def contato(request):
    return HttpResponse('Contatos :)')

def sobre(request):
    return HttpResponse('Sobre :)')