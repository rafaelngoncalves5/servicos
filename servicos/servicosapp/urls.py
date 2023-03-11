from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'servicosapp'
urlpatterns = [
   path('', views.index, name='index'),
   path('servicos/', views.index_servicos, name="index_servicos"),
   path('servicos/criar/', views.criar_servicos, name="criar_servicos"),
   path('servicos/criar/sucesso/', views.sucesso, name="sucesso"),
   path('servicos/<int:pk>/detalhes/', views.DetailView.as_view(), name="detalhes_servicos"),
   path('servicos/<int:id_servico>/excluir/', views.excluir_servico, name="excluir_servico"),
   path('servicos/<pk>/editar/', login_required(views.EditarForm.as_view(), login_url="/servicosapp/usuario/entrar"), name="editar_form"),
   path('usuario/cadastrar/', views.cadastrar_form, name="cadastrar_form"),
   path('usuario/entrar/', views.entrar_form, name='entrar_form'),
   path('usuario/sair/', views.sair, name="sair"),
   path('servicos/buscar/', views.buscar, name='buscar'),
   path('servicos/usuario/meus_servicos/', views.meus_servicos, name='meus_servicos'),
]
