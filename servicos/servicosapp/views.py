from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django import forms

from . models import Servico
from .forms import ServicosForm

def index(request):
       return render(request, 'servicosapp/index.html')

def index_servicos(request):
       servicos = Servico.objects.all()
       context = {
              'servicos': servicos
       }
       return render(request, 'servicosapp/servicos/index.html', context)

def criar_servicos(request):
       # Verifica se a requisição é do tipo POST
       if request.method == "POST":
              # Cria uma instância do formulário e popula com a requisição. Binding no Django!
              form = ServicosForm(request.POST)

              titulo = form['titulo']
              descricao = form['descricao']
              email = form['email']
              telefone_1 = form['telefone_1']
              telefone_2 = form['telefone_2']
              preco = form['preco']
              
              if form.is_valid():
                     # s = Servico(titulo='sd', descricao='fd', email='232', telefone_1='2312', telefone_2='233223')  
                     s = Servico(titulo=f"{titulo}", descricao=f"{descricao}", email=f"{email}", telefone_1=f"{telefone_1}", telefone_2=f"{telefone_2}")
                     s.save()
                     return HttpResponseRedirect("/servicosapp/servicos/criar/sucesso")
       else:
              form = ServicosForm()
      
       return render(request, 'servicosapp/servicos/criar.html', {'form': form})
              
def  sucesso(request):
       return render(request, "servicosapp/servicos/sucesso.html")