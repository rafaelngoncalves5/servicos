from django.contrib import admin
from .models import Categoria, Municipio, Servico

# Register your models here.
admin.site.register(Servico)

class ServicosAdmin(admin.ModelAdmin):
    list_filter = ('titulo')