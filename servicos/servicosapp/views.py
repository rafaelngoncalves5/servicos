from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . models import Servico

def index(request):
       return render(request, 'servicosapp/index.html')

def index_servicos(request):
       servicos = Servico.objects.all()
       context = {
              'servicos': servicos
       }
       return render(request, 'servicosapp/servicos/index.html', context)

def criar_servicos(request):
       return render(request, 'servicosapp/servicos/criar.html')