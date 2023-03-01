# Arquivo para semear o banco de dados, na tabela categoria com a lista ramos_de_atividade.txt

# Fonte para a tabela de categoria -> https://gist.github.com/prodis/857240
# Fonte para a tabela de municípios -> https://www.gov.br/economia/pt-br/assuntos/patrimonio-da-uniao/destinacao-de-imoveis/arquivos/2018/lista-municipios-excel.xls/view
# Na tabela de municípios eu peguei D2:D291
from servicosapp.models import Categoria

def seed(ramo_de_atividade):
    ramo_de_atividade = Categoria(nome_categoria=ramo_de_atividade)
    # Salvando no banco de dados a tabela
    ramo_de_atividade.save()

with open("seed.txt", "r", encoding='utf-8') as atividades:
    for atividade in atividades:
        seed(f"{atividade}")

'''
Para executar o seed.py

ATENÇÃO, EXECUTE UMA VEZ E COMENTE O CÓDIGO APÓS USO, POR SEGURANÇA

- python manage.py seed
- import seed
'''

'''
O primeiro item eu alterei da seguinte forma

SELECT * FROM servicosapp_categoria;

UPDATE servicosapp_categoria SET nome_categoria = "Outro" WHERE id_categoria = 1;
'''