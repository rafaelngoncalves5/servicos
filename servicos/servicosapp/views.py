from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.forms import ModelForm
from django.views import generic
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from . models import Servico, Categoria, Estado

def index(request):
       servicos = Servico.objects.order_by("-data_pub")[:15]
       servicos_aleatorios = Servico.objects.order_by("?")[:15]

       return render(request, 'servicosapp/index.html', {'servicos': servicos, 'servicos_aleatorios': servicos_aleatorios, 'estados': Estado.objects.all()})

def index_servicos(request):
       servicos = Servico.objects.all()
       estados = Estado.objects.all()

       context = {
              'servicos': servicos,
              'estados': estados
       }
       return render(request, 'servicosapp/servicos/index.html', context)

@login_required(login_url="/servicosapp/usuario/entrar")
def meus_servicos(request):

       current_user = request.user
       meus_servicos = Servico.objects.filter(fk_usuario = current_user.id)

       # Pegar aqui os objetos do DB que tem fk_usuario = request.user
       context = {
            'current_user': current_user,
            'meus_servicos': meus_servicos
       }

       return render(request, 'servicosapp/usuario/meus_servicos.html', context)

@login_required(login_url="/servicosapp/usuario/entrar")
def criar_servicos(request):
       categorias = Categoria.objects.all()
       estados = Estado.objects.all()

       usuario_atual = request.user
       u = User.objects.get(pk=usuario_atual.id)

       if request.method == "POST":
              categoria = request.POST['categoria']
              estado = request.POST['estado']
              c = Categoria.objects.get(nome_categoria=categoria)
              m = Estado.objects.get(nome_estado=estado)

              f = ServicosForm(request.POST)
              servico_novo = f.save()

              servico_novo.fk_usuario = u
              servico_novo.save()

              servico_novo.fk_categoria_id = c
              servico_novo.save()

              servico_novo.fk_estado_id = m
              servico_novo.save()

              HttpResponseRedirect('servicosapp/servicos/index.html')

       return render(request, 'servicosapp/servicos/criar.html', {'form': ServicosForm(), 'categorias': categorias, 'estados': estados})

class ServicosForm(ModelForm):
       class Meta:
              model = Servico
              fields = ['titulo', 'descricao', 'email', 'telefone_1', 'telefone_2', 'preco']
              
def sucesso(request):
       return render(request, "servicosapp/servicos/sucesso.html")

class DetailView(generic.DetailView):
    model = Servico
    template_name = 'servicosapp/servicos/detalhes.html'

@login_required(login_url="/servicosapp/usuario/entrar")
def excluir_servico(request, id_servico):
       servico = get_object_or_404(Servico, pk=id_servico)
       servico.delete()

       return render(request, 'servicosapp/servicos/excluir.html', {'id_servico': id_servico, 'servico': servico})

class EditarForm(generic.UpdateView):
       model = Servico
       fields = ['titulo', 'descricao', 'email', 'telefone_1', 'telefone_2', 'preco']
       template_name = "servicosapp/servicos/editar.html"
       success_url ="/servicosapp/servicos/usuario/meus_servicos"

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
                     #new_user.get_username
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
                     return HttpResponseRedirect(reverse('servicosapp:index'))
                     
              else:
                     # Tratar esse erro tamb??m na fase de testes
                     pass

       return render(request, 'servicosapp/usuario/entrar.html')

def sair(request):
       logout(request)
       return redirect('servicosapp:index')

def buscar(request):
       query_check = request.GET.get('titulo')
       query_estado = request.GET.get('filtro-estado')

       if not query_check:
              pass
       
       else:
              servicos = Servico.objects.filter(titulo__icontains = query_check)

              context = {
                     'query_check': query_check,
                     'servicos': servicos,
              }
              return render(request, 'servicosapp/servicos/buscar.html', context)
       
       if not query_estado:
              pass
       else:
              se = Estado.objects.get(nome_estado = query_estado)
              estados = Servico.objects.filter(fk_estado = se.id_estado)

              context = {
                     'query_estado': query_estado,
                     'estados': estados
              }
              return render(request, 'servicosapp/servicos/buscar.html', context) 

       return render(request, 'servicosapp/servicos/buscar.html')
