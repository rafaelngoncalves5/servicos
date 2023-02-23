from django.urls import path
from . import views

app_name = 'servicosapp'
urlpatterns = [
   path('', views.index, name='index'),
   path('servicos/', views.index_servicos, name="index_servicos"),
   path('servicos/criar', views.criar_servicos, name="criar_servicos"),
   path('servicos/criar/sucesso', views.sucesso, name="sucesso"),
   path('servicos/<int:pk>/detalhes', views.DetailView.as_view(), name="detalhes_servicos"),
   path('servicos/categorias', views.categorias, name='categorias'),
]
