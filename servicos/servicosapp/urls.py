from django.urls import path
from . import views

app_name = 'servicosapp'
urlpatterns = [
   path('', views.index, name='index'),
   path('servicos/', views.index_servicos, name="index_servicos"),
   path('servicos/criar', views.criar_servicos, name="criar_servicos"),
]
