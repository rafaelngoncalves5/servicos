from django import forms

# Dava pra usar o ModelForms também para facilitar
class ServicosForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=25)
    descricao = forms.CharField(label="Descrição", min_length=15)
    email = forms.EmailField(label="Email")
    telefone_1 = forms.CharField(label="Telefone 1")
    telefone_2 = forms.CharField(label="Telefone 2")
    preco = forms.IntegerField(label="Preço")

