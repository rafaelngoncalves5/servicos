# Generated by Django 4.1.7 on 2023-03-08 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicosapp', '0007_municipio_servico_fk_municipio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Municipio',
            new_name='Estado',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='id_municipio',
            new_name='id_estado',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='nome_municipio',
            new_name='nome_estado',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='fk_municipio',
            new_name='fk_estado',
        ),
    ]
