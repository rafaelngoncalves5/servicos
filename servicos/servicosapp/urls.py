from django.urls import path
from . import views

app_name = 'servicosapp'
urlpatterns = [
   path('', views.index, name='index'),
]
