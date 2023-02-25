from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.forms import ModelForm
from django.views import generic
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

from . models import Servico, Categoria

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
              HttpResponseRedirect('servicosapp/servicos/index.html')

       return render(request, 'servicosapp/servicos/criar.html', {'form': ServicosForm()})

class ServicosForm(ModelForm):
       class Meta:
              model = Servico
              fields = ['titulo', 'descricao', 'email', 'telefone_1', 'telefone_2', 'preco']
              
def sucesso(request):
       return render(request, "servicosapp/servicos/sucesso.html")

class DetailView(generic.DetailView):
    model = Servico
    template_name = 'servicosapp/servicos/detalhes.html'

def categorias(request):
       return render(request, "servicosapp/servicos/categorias.html", {'categorias': Categoria.objects.all()})

def excluir_servico(request, id_servico):
       servico = get_object_or_404(Servico, pk=id_servico)
       servico.delete()

       return render(request, 'servicosapp/servicos/excluir.html', {'id_servico': id_servico, 'servico': servico})


class EditarForm(generic.UpdateView):
       model = Servico
       fields = ['titulo', 'descricao', 'email', 'telefone_1', 'telefone_2', 'preco']
       template_name = "servicosapp/servicos/editar.html"
       success_url ="/servicosapp/servicos/"

def cadastrar_form(request):
       if request.method == 'POST':
              primeiro_nome = request.POST['primeiro_nome']
              ultimo_nome = request.POST['ultimo_nome']
              usuario = request.POST['usuario']
              email = request.POST['email']
              senha = request.POST['senha']

              try:
                     new_user = User.objects.create_user(f"{usuario}", f"{email}", f"{senha}")
                     new_user.first_name = primeiro_nome
                     new_user.last_name = ultimo_nome
                     new_user.date_joined = timezone.now()
                     new_user.save()


              except IntegrityError:
                     # Tratar isso aqui na fase de testes
                     pass

       return render(request, 'servicosapp/usuario/cadastrar.html')

def entrar_form(request):

       if request.method == 'POST':
              usuario = request.POST['usuario']
              senha = request.POST['senha']

              user = authenticate(request, username=usuario, password=senha)
              if user is not None:
                     login(request, user)
                     
              else:
                     # Tratar esse erro também na fase de testes
                     pass

       return render(request, 'servicosapp/usuario/entrar.html')

def sair(request):
       logout(request)
       return redirect('servicosapp:index')

