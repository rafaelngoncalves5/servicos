# Generated by Django 4.1.7 on 2023-02-22 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome_categoria', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id_servico', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('telefone_1', models.CharField(max_length=50)),
                ('telefone_2', models.CharField(max_length=50)),
                ('fk_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicosapp.categoria')),
                ('fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
