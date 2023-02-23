from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db import models
from django.forms import ModelForm

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

       if request.method == "POST":
              f = ServicosForm(request.POST)
              servico_novo = f.save()

       return render(request, 'servicosapp/servicos/criar.html', {'form': ServicosForm()})

class ServicosForm(ModelForm):
       class Meta:
              model = Servico
              fields = ['titulo', 'descricao', 'email', 'telefone_1', 'telefone_2', 'preco']
              
def sucesso(request):
       return render(request, "servicosapp/servicos/sucesso.html")